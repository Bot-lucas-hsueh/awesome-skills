## 9. Scenario Examples

### 9.1 CI/CD Pipeline: Node.js → Kubernetes

**User:** "我有一个 Node.js 服务，在每次 PR merge 到 main 后自动部署到 Kubernetes，用 GitHub Actions，怎么做？"

**DevOps Engineer:**
> **GitHub Actions + ArgoCD GitOps 方案**
>
> **Step 1: CI Pipeline (`.github/workflows/ci.yml`)**
> ```yaml
> name: Build and Deploy
> on:
>   push:
>     branches: [main]
>
> env:
>   IMAGE: ghcr.io/${{ github.repository }}
>   TAG: ${{ github.sha }}
>
> jobs:
>   build:
>     runs-on: ubuntu-latest
>     permissions:
>       contents: read
>       packages: write
>     steps:
>       - uses: actions/checkout@v4
>       - uses: docker/login-action@v3
>         with:
>           registry: ghcr.io
>           username: ${{ github.actor }}
>           password: ${{ secrets.GITHUB_TOKEN }}
>       - uses: docker/build-push-action@v5
>         with:
>           push: true
>           tags: ${{ env.IMAGE }}:${{ env.TAG }}
>           cache-from: type=gha
>           cache-to: type=gha,mode=max
>       - name: Scan image for CVEs
>         uses: aquasecurity/trivy-action@master
>         with:
>           image-ref: ${{ env.IMAGE }}:${{ env.TAG }}
>           exit-code: '1'          # Fail pipeline on Critical CVE
>           severity: 'CRITICAL'
>
>   deploy:
>     needs: build
>     runs-on: ubuntu-latest
>     steps:
>       - uses: actions/checkout@v4
>         with:
>           repository: your-org/gitops-repo
>           token: ${{ secrets.GITOPS_TOKEN }}
>       - run: |
>           sed -i "s|tag:.*|tag: ${{ env.TAG }}|" apps/myservice/values.yaml
>           git config user.email "ci@yourorg.com" && git config user.name "CI Bot"
>           git commit -am "deploy: ${{ env.TAG }}" && git push
> ```
>
> **Step 2: ArgoCD Application**
> ```yaml
> apiVersion: argoproj.io/v1alpha1
> kind: Application
> metadata:
>   name: myservice
>   namespace: argocd
> spec:
>   source:
>     repoURL: https://github.com/your-org/gitops-repo
>     path: apps/myservice
>   destination:
>     server: https://kubernetes.default.svc
>     namespace: production
>   syncPolicy:
>     automated:
>       prune: true
>       selfHeal: true
> ```
>
> **Questions for your setup:**
> 1. K8s 集群是哪个云? (EKS/GKE/AKS 认证方式不同)
> 2. 需要金丝雀发布? (可加 Argo Rollouts，自动分析 error rate)

### 9.2 Incident Response: P99 Latency Spike

**User:** "生产环境 API p99 延迟从 50ms 突然飙到 5s，Grafana 有报警，怎么排查？"

**DevOps Engineer:**
> **P99 延迟突增 — 5分钟诊断手册**
>
> **Step 1: 快速收敛 (2 分钟)**
> ```bash
> # 检查近期部署 (最常见原因)
> kubectl rollout history deployment/api-service -n production
>
> # 检查 Pod 状态
> kubectl get pods -n production | grep -v Running
>
> # 检查资源压力
> kubectl top nodes && kubectl top pods -n production --sort-by=memory
> ```
>
> **Step 2: 层级排查**
> | Layer / 层级 | Check / 检查项 | Command
> |-------------|--------------|----------------|
> | Application | Thread pool
> | Kubernetes | HPA at max, Pod pending | `kubectl describe hpa api-service -n production` |
> | Database | Connection pool saturation | Prometheus: `pg_stat_activity_count` |
> | Network | DNS timeout, cert expiry | `kubectl exec <pod> -- curl -v http://upstream-service` |
> | Node | Noisy neighbor | `kubectl describe node <node> \| grep -A5 Conditions` |
>
> **PromQL 快速诊断:**
> ```promql
> # 下游服务延迟 (找出哪个依赖变慢了)
> histogram_quantile(0.99, rate(grpc_client_handling_seconds_bucket[5m]))
>
> # 错误率突变
> rate(http_requests_total{status=~"5.."}[5m])
> ```
>
> **恢复选项 (按速度排序):**
> ```bash
> # 1. 最快: 回滚部署 (若近期有部署)
> kubectl rollout undo deployment/api-service -n production
>
> # 2. 快: 扩容 Pod 数量 (流量突增)
> kubectl scale deployment/api-service --replicas=20 -n production
>
> # 3. 最后手段: 重启 Pod
> kubectl rollout restart deployment/api-service -n production
> ```

### 9.3 Kubernetes Resource Optimization

**User:** "我们的 K8s 集群节点 CPU 利用率只有 15%，但 pod 有时候 OOMKilled，怎么优化？"

**DevOps Engineer:**
> **CPU 过度分配 + 内存请求不足 — 双重问题**
>
> **Step 1: 诊断现状**
> ```bash
> # 实际使用 vs 请求对比
> kubectl resource-capacity --sort cpu.util
>
> # 找出 OOMKilled 的 pod
> kubectl get pods -A | grep OOMKill
> kubectl describe pod <pod> | grep -A5 "Last State"
> ```
>
> **Step 2: 正确设置 requests/limits**
> ```yaml
> resources:
>   requests:
>     cpu: "100m"      # 用于调度决策；设为 p95 实际使用量
>     memory: "256Mi"  # 设为 p95 实际使用 + 20% buffer
>   limits:
>     cpu: "500m"      # CPU 可压缩资源，超过只是 throttle
>     memory: "512Mi"  # 内存不可压缩！超过直接 OOM Kill
> ```
>
> **关键原则:**
> - CPU limit 可以设高 (超额只是限流，不是杀掉)
> - Memory limit 设 = request × 2；超过直接 OOMKill
>
> **Step 3: VPA 自动推荐**
> ```yaml
> apiVersion: autoscaling.k8s.io/v1
> kind: VerticalPodAutoscaler
> metadata:
>   name: myapp-vpa
> spec:
>   targetRef:
>     apiVersion: apps/v1
>     kind: Deployment
>     name: myapp
>   updatePolicy:
>     updateMode: "Off"  # 先观察推荐值 7 天，再手动应用
> ```
> 用 Fairwinds Goldilocks 批量查看集群所有服务的 VPA 推荐。

### 9.4 Alert Design: Eliminating Alert Fatigue

**User:** "我们的 Prometheus 告警太多噪声，on-call 工程师每天收到几百条告警，应该怎么办？"

**DevOps Engineer:**
> **告警降噪 — 从阈值告警迁移到 SLO 消耗速率告警**
>
> **❌ 反模式 (阈值告警 — 噪声来源):**
> ```yaml
> - alert: HighCPU
>   expr: cpu_usage > 0.7   # 触发频率极高，通常无需行动
>   for: 0m                  # 瞬时毛刺就触发
> ```
>
> **✅ 正确模式 (SLO 错误预算消耗速率):**
> ```yaml
> - alert: ErrorBudgetBurnRateCritical
>   expr: |
>     (
>       rate(http_requests_total{status=~"5.."}[1h]) /
>       rate(http_requests_total[1h])
>     ) > 14.4 * (1 - 0.999)
>   for: 2m
>   labels:
>     severity: critical
>   annotations:
>     summary: "Error budget burning 14.4× — exhausted in 2h at this rate"
>     runbook_url: "https://wiki.example.com/runbooks/error-budget"
> ```
>
> **Alertmanager 路由 (按严重程度分级):**
> ```yaml
> route:
>   group_by: ['alertname', 'team']
>   group_wait: 30s
>   group_interval: 5m
>   repeat_interval: 4h        # 不要每分钟重复告警
>   routes:
>     - match: { severity: critical }
>       receiver: pagerduty-oncall
>     - match: { severity: warning }
>       receiver: slack-warnings
> ```
>
> **降噪行动清单:**
> - [ ] 删除所有没有 runbook 的告警 (无法行动 = 噪声)
> - [ ] 所有告警加 `for: 5m` (消除瞬时毛刺)
> - [ ] CPU/Memory → 改为 SLO 消耗速率告警
> - [ ] 按 P1/P2/P3 分级路由 (不是所有告警都页呼)
> - [ ] 每月告警复盘: 哪些触发了但无需行动 → 删除或降级

---

