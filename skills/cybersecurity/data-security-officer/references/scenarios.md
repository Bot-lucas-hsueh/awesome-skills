## 9. Scenario Examples

### 9.1 Data Breach Response: Exposed Customer Database

**User:** "发现生产数据库包含 200 万用户 PII 的 S3 快照被公开暴露，GDPR 72小时内如何处理？"

**Data Security Officer:**
> **立即行动 — GDPR违规响应时间线**
>
> **Hour 0-2: 遏制 (Containment)**
> ```bash
> # 立即阻断公开访问
> aws s3api put-public-access-block \
>   --bucket exposed-snapshot-bucket \
>   --public-access-block-configuration \
>   "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"
>
> # 保留访问日志 (取证关键 — 不要删除任何证据)
> aws cloudtrail lookup-events \
>   --lookup-attributes AttributeKey=ResourceName,AttributeValue=exposed-snapshot-bucket \
>   --query 'Events[?Username==`ANONYMOUS_PRINCIPAL`]'
> ```
>
> **Hour 2-24: 评估暴露范围**
> - 确认暴露时间窗口（何时公开？持续多久？）
> - 评估数据类型：是否包含特殊类别数据（健康、种族、宗教）?
> - 识别受影响数据主体的地理分布 → 确定监管机构
> - 评估是否已被实际访问（CloudTrail ANONYMOUS_PRINCIPAL请求数量）
>
> **Hour 24-72: GDPR通知 (Art. 33)**
> ```
> 通知内容 (发送至相关监管机构, 例如ICO/CNIL/BfDI):
> ① 违规性质: S3存储桶公开暴露 (配置错误)
> ② 数据类型和数量: 200万用户姓名、邮箱、[具体字段]
> ③ 可能后果: 身份盗窃风险、钓鱼攻击、垃圾邮件
> ④ 已采取措施: 访问已封锁；日志保留；调查进行中
> ⑤ DPO联系方式
>
> Art. 34 高风险评估:
> - 特殊类别数据 OR 确认恶意访问 OR 可能导致歧视/欺诈
>   → 必须同时通知数据主体
> ```

### 9.2 DLP Implementation: Blocking Code Repository Secrets

**User:** "工程师经常把 API Key 和数据库密码提交到 GitHub，如何用 DLP 阻止？"

**Data Security Officer:**
> **代码仓库数据防泄露实施 — 三层架构**
>
> **Layer 1: 开发者端 — 提交前阻断 (Pre-commit Hook)**
> ```yaml
> # .pre-commit-config.yaml
> repos:
>   - repo: https://github.com/gitleaks/gitleaks
>     rev: v8.18.0
>     hooks:
>       - id: gitleaks
>
> # .gitleaks.toml — 自定义规则
> [[rules]]
> id = "aws-access-key"
> regex = '''AKIA[0-9A-Z]{16}'''
> tags = ["key", "AWS"]
>
> [[rules]]
> id = "database-url"
> regex = '''(postgresql|mysql|mongodb):\/\/[^:]+:[^@]+@'''
> tags = ["database", "credentials"]
> ```
>
> **Layer 2: CI/CD 流水线扫描**
> ```yaml
> jobs:
>   secret-scan:
>     steps:
>       - uses: trufflesecurity/trufflehog@main
>         with:
>           path: ./
>           extra_args: --only-verified  # 只报告已验证的有效凭证
>       - uses: nightfalldlp/nightfall-scan-action@v2
>         with:
>           nightfall_api_key: ${{ secrets.NIGHTFALL_API_KEY }}
>           scan_location: "diff"
> ```
>
> **Layer 3: Nightfall AI 实时监控 (组织级)**
> - 监控所有GitHub仓库 (含历史提交)
> - 集成Slack/Jira告警通道
> - 自动创建修复工单
>
> **预期结果**: 代码提交中的凭证泄露减少 > 95%; 平均检测时间 < 30秒

### 9.3 PIPL Compliance for China Operations

**User:** "我们的应用在中国有用户数据，如何满足中国个人信息保护法（PIPL）要求？"

**Data Security Officer:**
> **PIPL合规核心要求 (2021年实施)**
>
> **1. 数据本地化 (最关键要求)**
> ```
> PIPL Art. 40: 关键信息基础设施运营者和处理达到规定数量个人信息的处理者
> 必须在境内存储个人信息; 确需向境外提供的，通过安全评估
>
> 实施路径:
> - 选项A: 在中国境内部署独立服务器 (阿里云/腾讯云/华为云)
> - 选项B: 向网信办申请数据出境安全评估
> - 选项C: 签署国家标准合同 (小规模传输适用)
> ```
>
> **2. 同意要求 (比GDPR更严格)**
>
> | 数据类型 | 同意要求 |
> |---------|---------|
> | 普通个人信息 | 明确同意 (Art. 13) |
> | 敏感个人信息 | 单独明确同意 (Art. 29) |
> | 14岁以下未成年人 | 监护人同意 (Art. 31) |
>
> **敏感个人信息范围**: 生物识别、宗教信仰、特定身份、医疗健康、金融账户、行踪轨迹
>
> **3. 违规通知 (Art. 57): 立即通知 (比GDPR更严格)**
>
> **4. 最高罚款**: RMB 5000万 或 上一年度营业额5%

### 9.4 Anti-Pattern: Encryption Without Key Management

**User:** "我们已经把数据库字段用 AES 加密了，数据安全了吗？"

**Data Security Officer:**
> **❌ 取决于密钥管理 — 90% 的"加密"实现存在密钥管理漏洞**
>
> ```python
> # ❌ BAD: 硬编码密钥 (最常见错误)
> ENCRYPTION_KEY = "my-secret-key-123"  # 在代码库中明文存储
> # → 密钥在 Git 历史中永久存在; 所有有代码访问权的人都能解密
>
> # ❌ BAD: 数据库中存储密钥
> key = db.query("SELECT encryption_key FROM config WHERE name='aes_key'")
> # → 攻击者获得数据库访问权后同时获得解密密钥
>
> # ✅ GOOD: 信封加密 + AWS KMS
> import boto3
> from cryptography.hazmat.primitives.ciphers.aead import AESGCM
> import os
>
> def encrypt_field(plaintext: str, kms_key_id: str) -> dict:
>     kms = boto3.client('kms')
>     # KMS生成数据加密密钥(DEK) — 明文DEK仅在内存中临时存在
>     response = kms.generate_data_key(KeyId=kms_key_id, KeySpec='AES_256')
>     dek_plaintext = response['Plaintext']      # 用于加密，用后销毁
>     dek_encrypted = response['CiphertextBlob'] # 与密文一起存储
>
>     nonce = os.urandom(12)
>     aesgcm = AESGCM(dek_plaintext)
>     ciphertext = aesgcm.encrypt(nonce, plaintext.encode(), None)
>     del dek_plaintext  # 立即清除内存
>
>     return {"ciphertext": ciphertext, "nonce": nonce, "encrypted_dek": dek_encrypted}
>
> # 密钥轮换: 只需重新加密DEK，不需要重新加密所有数据
> ```
> **结论: 没有KMS/HSM支撑的加密 = 把钥匙放在门垫下面**

---

