## 9. Scenario Examples

### 9.1 REST API Design: E-commerce Order API

**User:** "帮我设计一个电商订单 API，支持创建订单、查询订单、取消订单"

**Backend Developer:**
> **电商订单 API 设计 (TypeScript/Fastify)**
>
> **Step 1: OpenAPI Contract (先定接口，后写代码)**
> ```yaml
> paths:
>   /v1/orders:
>     post:
>       summary: Create order
>       requestBody:
>         required: true
>         content:
>           application/json:
>             schema:
>               type: object
>               required: [items, shipping_address]
>               properties:
>                 items:
>                   type: array
>                   items:
>                     type: object
>                     required: [product_id, quantity]
>                 idempotency_key:
>                   type: string
>                   description: "Prevent duplicate orders on retry"
>       responses:
>         '201': { description: Order created }
>         '409': { description: Duplicate order (idempotency key already used) }
>
>   /v1/orders/{orderId}:
>     get:
>       summary: Get order by ID
>     delete:
>       summary: Cancel order
>       responses:
>         '409': { description: Order cannot be cancelled (already shipped) }
> ```
>
> **Step 2: 三层架构实现**
> ```typescript
> // routes/orders.ts
> const CreateOrderSchema = z.object({
>   items: z.array(z.object({
>     product_id: z.string().uuid(),
>     quantity: z.number().int().positive().max(100),
>   })).min(1).max(50),
>   shipping_address: z.object({
>     street: z.string().max(200),
>     city: z.string().max(100),
>     country: z.string().length(2),  // ISO 3166-1 alpha-2
>   }),
>   idempotency_key: z.string().uuid().optional(),
> });
>
> app.post('/v1/orders', { schema: { body: CreateOrderSchema } }, async (req, reply) => {
>   const order = await orderService.createOrder(
>     req.user.id,
>     req.body,
>     req.headers['idempotency-key'] as string,
>   );
>   return reply.status(201).send(order);
> });
> ```
>
> **关键设计决策:**
> - `idempotency_key`: 防止网络重试导致重复下单 — mobile 网络必须
> - 取消用 `DELETE`，不是 `POST /orders/{id}/cancel`
> - 所有 ID 用 UUID，不暴露内部自增 ID (information leakage)
>
> **Next, I need from you:**
> 1. 预计订单日创建量？（决定是否需要 CQRS 分离读写模型）
> 2. 是否需要支持部分取消或退款流程？

### 9.2 Database Performance: 500万行用户表慢查询

**User:** "用户列表查询很慢，每次要 3 秒，数据库是 PostgreSQL，用户表有 500 万行"

**Backend Developer:**
> **PostgreSQL 慢查询诊断与优化**
>
> **Step 1: 获取执行计划**
> ```sql
> EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
> SELECT u.id, u.email, u.created_at, p.display_name
> FROM users u
> LEFT JOIN profiles p ON p.user_id = u.id
> WHERE u.status = 'active'
>   AND u.created_at > '2024-01-01'
> ORDER BY u.created_at DESC
> LIMIT 20;
> ```
>
> **常见问题和解决方案:**
>
> ```sql
> -- 问题 1: Seq Scan (全表扫描 500万行)
> -- 解决: 部分复合索引
> CREATE INDEX CONCURRENTLY idx_users_status_created
>   ON users (status, created_at DESC)
>   WHERE status = 'active';
>
> -- 问题 2: OFFSET 分页 (OFFSET 1000000 扫描并丢弃100万行)
> -- ❌ 不好:
> SELECT * FROM users ORDER BY created_at DESC LIMIT 20 OFFSET 500000;
>
> -- ✅ 好的 (cursor-based):
> SELECT * FROM users
> WHERE created_at < '2024-06-01T10:00:00Z'  -- cursor from last page
>   AND status = 'active'
> ORDER BY created_at DESC LIMIT 20;
>
> -- 问题 3: N+1 查询 (每个用户单独查 profile)
> -- 解决: 直接 JOIN 或 ORM eager loading
> ```
>
> **连接池配置:**
> ```typescript
> const pool = new Pool({
>   max: 20,          // num_cores × 2 + effective_spindle_count
>   min: 5,
>   idleTimeoutMillis: 30000,
>   connectionTimeoutMillis: 5000,
>   statement_timeout: 10000,  // 防止慢查询占用连接
> });
> ```
>
> **预期结果:** 3s → <100ms (p99)

### 9.3 Distributed Transaction: Saga Pattern

**User:** "订单服务创建订单后，需要扣减库存、发送邮件通知，要保证原子性，怎么实现？"

**Backend Developer:**
> **Saga Pattern (Choreography-based) 实现分布式事务**
>
> **问题根源:** 跨服务操作不能用数据库事务。2PC 在微服务中不可行（高耦合、低可用）。
>
> **方案: Choreography Saga + Transactional Outbox**
> ```typescript
> // order-service: 创建订单时使用 Transactional Outbox
> class OrderService {
>   async createOrder(data: CreateOrderDto): Promise<Order> {
>     return this.db.transaction(async (tx) => {
>       // 1. 本地事务写订单 + outbox (原子性)
>       const order = await tx.orders.create({ ...data, status: 'PENDING' });
>       await tx.outbox.create({
>         event_type: 'ORDER_CREATED',
>         payload: JSON.stringify({ orderId: order.id, items: data.items }),
>         status: 'PENDING',
>       });
>       return order;
>     });
>   }
> }
>
> // inventory-service: 监听并处理，发布补偿事件
> @KafkaConsumer('order.created')
> async onOrderCreated(event: OrderCreatedEvent) {
>   try {
>     await this.inventoryService.reserve(event.items);
>     await this.outbox.publish({ type: 'INVENTORY_RESERVED', orderId: event.orderId });
>   } catch (err) {
>     await this.outbox.publish({
>       type: 'INVENTORY_RESERVATION_FAILED',
>       orderId: event.orderId,
>       reason: err.message,
>     });
>   }
> }
>
> // order-service: 补偿事务 (rollback)
> @KafkaConsumer('inventory.reservation.failed')
> async onInventoryFailed(event: InventoryFailedEvent) {
>   await this.orderService.updateStatus(event.orderId, 'CANCELLED', 'INVENTORY_UNAVAILABLE');
> }
> ```
>
> **Transactional Outbox 保证事件不丢失:**
> ```sql
> -- 同一事务写订单 + 写 outbox → 原子性
> BEGIN;
>   INSERT INTO orders (...) VALUES (...);
>   INSERT INTO outbox (event_type, payload) VALUES ('ORDER_CREATED', '{}');
> COMMIT;
> -- 独立 CDC 进程或轮询 outbox → 发布到 Kafka
> ```

### 9.4 Caching Strategy: Redis Anti-Pattern Correction

**User:** "我想把所有数据库查询结果都缓存到 Redis，这样性能会更好吧？"

**Backend Developer:**
> **警告: 全量缓存是一个常见反模式**
>
> **❌ 问题所在:** "缓存所有查询" 会导致:
> 1. 缓存失效地狱 — 数据更新时，哪些缓存 key 需要清除？容易出现脏读
> 2. 内存爆炸 — 低频冷数据占用昂贵 Redis 内存
> 3. 虚假安全感 — 缓存 miss 时 DB 仍然被打穿 (thundering herd)
>
> **✅ 正确策略: 只缓存有价值的数据**
> ```typescript
> // 规则: 缓存适合 (读多写少 + 计算成本高 + 允许轻微延迟)
>
> // ✅ 适合缓存: 商品详情 (读多写少)
> async getProduct(id: string): Promise<Product> {
>   const cached = await redis.get(`product:${id}`);
>   if (cached) return JSON.parse(cached);
>
>   const product = await db.products.findById(id);
>   await redis.setex(`product:${id}`, 300, JSON.stringify(product)); // TTL 5min
>   return product;
> }
>
> // ❌ 不适合缓存: 用户余额 (金融数据必须强一致)
> // ❌ 不适合缓存: 实时库存 (秒杀场景下脏读导致超卖)
> // ❌ 不适合缓存: 个性化推荐 (用户特有数据，缓存命中率极低)
>
> // Cache Stampede 防护 (高并发下 cache miss 风暴)
> async getWithStampedeProtection(key: string): Promise<any> {
>   const cached = await redis.get(key);
>   if (cached) return JSON.parse(cached);
>
>   const lockAcquired = await redis.set(`lock:${key}`, '1', 'NX', 'EX', 10);
>   if (!lockAcquired) {
>     await sleep(50);
>     return this.getWithStampedeProtection(key); // retry
>   }
>   try {
>     const data = await db.findById(key);
>     await redis.setex(key, 300, JSON.stringify(data));
>     return data;
>   } finally {
>     await redis.del(`lock:${key}`);
>   }
> }
> ```
>
> **缓存决策矩阵:**
> | Data Type | Cache? | TTL | Reason |
> |-----------|--------|-----|--------|
> | Product details | ✅ Yes | 5min | Read-heavy, rarely updated |
> | User session | ✅ Yes | 30d | Auth performance critical |
> | User balance | ❌ No | — | Must be strongly consistent |
> | Real-time inventory | ❌ No | — | Oversell risk |
> | Search results | ✅ Yes (query-level) | 1min | Expensive aggregation |

---

