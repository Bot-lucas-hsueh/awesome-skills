# CloudBase Standards & Reference

## SDK Installation

### 小程序端
```javascript
// app.js 初始化
App({
  onLaunch() {
    wx.cloud.init({
      env: 'your-env-id',
      traceUser: true
    })
  }
})

// 页面使用
const db = wx.cloud.database()
const _ = db.command
```

### 云函数端
```javascript
const cloud = require('wx-server-sdk')
cloud.init({
  env: cloud.DYNAMIC_CURRENT_ENV
})
```

## Database Operations

### CRUD Operations
```javascript
// 添加数据
await db.collection('todos').add({
  data: {
    title: '学习CloudBase',
    done: false,
    createdAt: db.serverDate()
  }
})

// 查询数据（带条件）
const { data } = await db.collection('todos')
  .where({
    done: false,
    priority: _.gt(1)
  })
  .orderBy('createdAt', 'desc')
  .skip(0)
  .limit(20)
  .get()

// 更新数据
await db.collection('todos').doc('id').update({
  data: { done: true, updatedAt: db.serverDate() }
})

// 删除数据
await db.collection('todos').doc('id').remove()
```

### 聚合查询
```javascript
const { list } = await db.collection('orders')
  .aggregate()
  .match({ status: 'completed' })
  .group({
    _id: '$category',
    total: _.sum('$amount'),
    count: _.sum(1)
  })
  .sort({ total: -1 })
  .end()
```

### 事务
```javascript
await db.runTransaction(async transaction => {
  const userRes = await transaction.collection('users').doc(userId).get()
  const balance = userRes.data.balance - amount
  
  if (balance < 0) throw new Error('Insufficient balance')
  
  await transaction.collection('users').doc(userId).update({
    data: { balance }
  })
  await transaction.collection('transactions').add({
    data: { userId, amount, type: 'debit', createdAt: db.serverDate() }
  })
})
```

## File Storage

```javascript
// 上传文件
const upload = async (filePath) => {
  const cloudPath = `images/${Date.now()}-${Math.random().toString(36).slice(2)}.jpg`
  const { fileID } = await wx.cloud.uploadFile({ cloudPath, filePath })
  return fileID
}

// 获取临时链接
const getUrl = async (fileID) => {
  const { fileList } = await wx.cloud.getTempFileURL({
    fileList: [fileID]
  })
  return fileList[0].tempFileURL
}

// 删除文件
await wx.cloud.deleteFile({ fileList: [fileID] })
```

## Cloud Function Patterns

### Standard Template
```javascript
const cloud = require('wx-server-sdk')
cloud.init({ env: cloud.DYNAMIC_CURRENT_ENV })
const db = cloud.database()
const _ = db.command

exports.main = async (event, context) => {
  const { action, data } = event
  
  try {
    switch(action) {
      case 'create': return await createItem(data)
      case 'query': return await queryItems(data)
      case 'update': return await updateItem(data)
      case 'delete': return await deleteItem(data)
      default: throw new Error(`Unknown action: ${action}`)
    }
  } catch (err) {
    console.error('Cloud function error:', err)
    return { 
      success: false, 
      error: err.message,
      code: err.code || 'INTERNAL_ERROR'
    }
  }
}
```

## Security Best Practices

### Database Rules
```json
{
  "read": "doc.userId == auth.openid",
  "write": "doc.userId == auth.openid",
  "create": "request.auth.openid != null"
}
```

### Authentication Check
```javascript
const { OPENID } = cloud.getWXContext()
if (!OPENID) throw new Error('Unauthorized')
```
