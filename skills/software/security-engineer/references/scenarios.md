## 9. Scenario Examples

### 9.1 SQL Injection Found in Production API

**User:** "扫描发现生产 API 有 SQL 注入漏洞，数据库包含用户 PII，下一步怎么做？"

**Security Engineer:**
> **紧急响应 (发现后 2 小时内)**
>
> **Step 1: 评估可利用性**
> ```bash
> # 在隔离环境中复现（不要在生产）
> sqlmap -u "https://api.example.com/v1/users/login" \
>   --data='{"email":"test@test.com","password":"test"}' \
>   --level=3 --risk=2 --batch --dbs
> ```
>
> **Step 2: 紧急遏制**
> ```bash
> # 选项A: WAF 级别封锁 (最快)
> # AWS WAF → 添加 AWSManagedRulesSQLiRuleSet 到该路径
>
> # 选项B: 端点下线 (最彻底)
> kubectl patch ingress api-ingress -n production \
>   --type='json' -p='[{"op":"replace","path":"/spec/rules/0","value":{"host":"api.example.com"}}]'
> ```
>
> **Step 3: 代码修复**
> ```python
> # ❌ VULNERABLE — 绝不这样做
> query = f"SELECT * FROM users WHERE email = '{email}'"
> cursor.execute(query)
>
> # ✅ SECURE — 参数化查询
> query = "SELECT * FROM users WHERE email = %s AND password_hash = %s"
> cursor.execute(query, (email, hash_password(password)))
>
> # ✅ BETTER — 使用 ORM
> user = session.query(User).filter(User.email == email).first()
> ```
>
> **合规注意事项 (关键):**
> - **GDPR Art. 33**: 若 PII 可能被访问，72 小时内通知监管机构
> - **PCI-DSS**: 若涉及持卡人数据，强制启动数据泄露通知流程
> - **事件记录**: 保留所有日志以供取证；不要删除任何证据

### 9.2 Cloud Misconfiguration: Public S3 Bucket

**User:** "Prowler 扫描发现一个包含客户数据的 S3 存储桶公开可读，怎么评估和修复？"

**Security Engineer:**
> **暴露评估与修复**
>
> **Step 1: 评估暴露范围**
> ```bash
> # 检查谁访问了这个桶 (关键: 是否有未认证访问？)
> aws cloudtrail lookup-events \
>   --lookup-attributes AttributeKey=ResourceName,AttributeValue=exposed-bucket \
>   --start-time $(date -d '90 days ago' --iso-8601=seconds) \
>   --query 'Events[?Username==`ANONYMOUS_PRINCIPAL`]'
>
> # 评估数据敏感性
> aws s3 ls s3://exposed-bucket --recursive --human-readable | head -50
> ```
>
> **Step 2: 立即修复 (安全，不影响应用)**
> ```bash
> aws s3api put-public-access-block \
>   --bucket exposed-bucket \
>   --public-access-block-configuration \
>   "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
> ```
>
> **Step 3: Terraform 防止再次发生**
> ```hcl
> resource "aws_s3_bucket_public_access_block" "all_buckets" {
>   bucket                  = aws_s3_bucket.app_data.id
>   block_public_acls       = true
>   block_public_policy     = true
>   ignore_public_acls      = true
>   restrict_public_buckets = true
> }
>
> # 组织级 SCP (防止任何账户创建公开桶)
> # 见 §7 Standards & Reference 中的 SCP 模板
> ```

### 9.3 DevSecOps from Scratch: 20-Engineer Startup

**User:** "初创公司 20 名工程师，没有安全体系，如何在不降低开发速度的情况下建立 DevSecOps？"

**Security Engineer:**
> **30/60/90 天 DevSecOps 建设路线图**
>
> **Week 1-2: 零摩擦快速胜利**
> ```yaml
> # .github/dependabot.yml — 自动化依赖更新
> version: 2
> updates:
>   - package-ecosystem: "npm"
>     directory: "/"
>     schedule: { interval: "weekly" }
>   - package-ecosystem: "docker"
>     directory: "/"
>     schedule: { interval: "weekly" }
>
> # .pre-commit-config.yaml — 提交前密钥检测
> repos:
>   - repo: https://github.com/gitleaks/gitleaks
>     rev: v8.18.0
>     hooks:
>       - id: gitleaks
> ```
>
> ```yaml
> # GitHub Actions — CI 安全扫描
> jobs:
>   security:
>     steps:
>       - uses: returntocorp/semgrep-action@v1
>         with: { config: "p/owasp-top-ten p/secrets p/sql-injection" }
>       - uses: aquasecurity/trivy-action@master
>         with: { image-ref: "${{ env.IMAGE }}:${{ github.sha }}", exit-code: "1", severity: "CRITICAL" }
> ```
>
> **Month 1**: MFA 全员强制; IAM 最小权限; AWS GuardDuty 全区域启用
> **Month 2**: 威胁建模研讨 (STRIDE); 漏洞 SLA 制度化; VDP 上线
> **Month 3**: Security Champions 体系 (每团队 1 名); SOC2 Gap Analysis

### 9.4 Anti-Pattern: Trust the Frontend

**User:** "我们的 API 只在前端做了权限校验，后端相信前端传来的 user_id，安全吗？"

**Security Engineer:**
> **❌ 这是严重的安全漏洞 — Broken Access Control (OWASP A01)**
>
> **问题场景:**
> ```http
> GET /api/orders?user_id=123   ← 攻击者修改为 user_id=456
> Authorization: Bearer <valid-token-for-user-123>
>
> # 后端相信 user_id 参数 → 攻击者获取任意用户订单 (IDOR)
> ```
>
> **✅ 正确实现: 后端从认证 Token 中提取用户身份**
> ```python
> # ❌ BAD: 相信客户端传来的 user_id
> @app.get("/api/orders")
> def get_orders(user_id: int = Query(...)):
>     return db.query(Order).filter(Order.user_id == user_id).all()
>
> # ✅ GOOD: 从 JWT 中提取经过认证的用户 ID
> @app.get("/api/orders")
> def get_orders(current_user: User = Depends(get_current_user)):
>     # current_user.id 来自已验证的 JWT, 不来自请求参数
>     return db.query(Order).filter(Order.user_id == current_user.id).all()
>
> # get_current_user 验证 JWT 签名:
> def get_current_user(token: str = Depends(oauth2_scheme)):
>     payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
>     user_id = payload.get("sub")  # 从 Token 中提取, 不可伪造
>     return db.query(User).filter(User.id == user_id).first()
> ```
>
> **规则: 永远不要相信客户端。用户身份必须来自服务端验证的凭证 (JWT/Session)，绝不来自请求参数。**

---

