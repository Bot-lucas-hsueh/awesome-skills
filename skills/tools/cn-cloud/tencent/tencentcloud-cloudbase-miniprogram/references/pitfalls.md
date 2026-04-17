# CloudBase Common Pitfalls

## Pitfall 1: 数据库权限配置错误

**错误:** 使用开放读写权限
```json
{
  "read": true,
  "write": true
}
```

**风险:** 任何用户都能读写所有数据

**正确:** 基于用户身份验证
```json
{
  "read": "doc.userId == auth.openid",
  "write": "doc.userId == auth.openid"
}
```

## Pitfall 2: 云函数忘记await

**错误:**
```javascript
exports.main = async () => {
  const result = db.collection('users').get()
  return result  // 返回Promise
}
```

**正确:**
```javascript
exports.main = async () => {
  const { data } = await db.collection('users').get()
  return { success: true, data }
}
```

## Pitfall 3: 数据库查询无索引

**问题:** 大数据量查询超时

**解决:** 为常用查询字段创建索引
```javascript
db.collection('orders').createIndex({
  userId: 1,
  status: 1,
  createdAt: -1
})
```

## Pitfall 4: 冷启动未优化

**症状:** 低频云函数响应慢（>3秒）

**解决:**
- 减少依赖包大小
- 使用预留实例
- 合并相关功能到同一云函数

## Pitfall 5: 文件路径冲突

**错误:** 使用固定文件名
```javascript
cloudPath: 'avatar.jpg'  // 所有用户覆盖同一文件
```

**正确:** 使用用户ID+时间戳
```javascript
cloudPath: `avatars/${openid}/${Date.now()}.jpg`
```

## Pitfall 6: 忽略错误处理

**错误:**
```javascript
exports.main = async (event) => {
  return await db.collection('data').add({ data: event })
}
```

**正确:**
```javascript
exports.main = async (event) => {
  try {
    // 参数验证
    if (!event.title) throw new Error('Title required')
    
    return await db.collection('data').add({ data: event })
  } catch (err) {
    return { success: false, error: err.message }
  }
}
```
