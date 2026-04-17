# CloudBase Scenario Examples

## Example 1: Todo应用完整开发

**User:** "用CloudBase开发一个Todo应用"

**Step 1: 数据库设计**
```javascript
// 集合: todos
{
  _id: string,
  userId: string,
  title: string,
  completed: boolean,
  priority: number,
  dueDate: Date,
  createdAt: Date,
  updatedAt: Date
}

// 索引
// 1. userId + completed
// 2. userId + priority + dueDate
```

**Step 2: 云函数开发**
```javascript
const cloud = require('wx-server-sdk')
cloud.init()
const db = cloud.database()

exports.main = async (event, context) => {
  const { action, data } = event
  const { OPENID } = cloud.getWXContext()
  
  switch(action) {
    case 'list':
      const { filter = 'all' } = data
      let where = { userId: OPENID }
      if (filter === 'active') where.completed = false
      if (filter === 'completed') where.completed = true
      
      return await db.collection('todos')
        .where(where)
        .orderBy('priority', 'desc')
        .orderBy('dueDate', 'asc')
        .get()
    
    case 'create':
      return await db.collection('todos').add({
        data: {
          ...data,
          userId: OPENID,
          completed: false,
          createdAt: db.serverDate(),
          updatedAt: db.serverDate()
        }
      })
    
    case 'toggle':
      const todo = await db.collection('todos').doc(data.id).get()
      if (todo.data.userId !== OPENID) throw new Error('Unauthorized')
      
      return await db.collection('todos').doc(data.id).update({
        data: {
          completed: !todo.data.completed,
          updatedAt: db.serverDate()
        }
      })
    
    case 'delete':
      const delTodo = await db.collection('todos').doc(data.id).get()
      if (delTodo.data.userId !== OPENID) throw new Error('Unauthorized')
      return await db.collection('todos').doc(data.id).remove()
  }
}
```

**Step 3: 小程序端调用**
```javascript
Page({
  data: { todos: [], filter: 'all' },
  
  async loadTodos() {
    const { result } = await wx.cloud.callFunction({
      name: 'todo',
      data: { action: 'list', data: { filter: this.data.filter } }
    })
    this.setData({ todos: result.data })
  },
  
  async addTodo(e) {
    const title = e.detail.value
    await wx.cloud.callFunction({
      name: 'todo',
      data: { action: 'create', data: { title, priority: 1 } }
    })
    this.loadTodos()
  }
})
```

## Example 2: 用户头像上传

```javascript
async uploadAvatar() {
  try {
    const { tempFilePaths } = await wx.chooseMedia({
      count: 1,
      mediaType: ['image'],
      sizeType: ['compressed']
    })
    
    const { tempFilePath } = await wx.compressImage({
      src: tempFilePaths[0],
      quality: 80
    })
    
    const { result } = await wx.cloud.callFunction({ name: 'getOpenId' })
    const cloudPath = `avatars/${result.openid}/${Date.now()}.jpg`
    
    const { fileID } = await wx.cloud.uploadFile({
      cloudPath,
      filePath: tempFilePath
    })
    
    await wx.cloud.callFunction({
      name: 'updateProfile',
      data: { avatarUrl: fileID }
    })
    
    wx.showToast({ title: '上传成功' })
  } catch (err) {
    wx.showToast({ title: '上传失败', icon: 'error' })
  }
}
```

## Example 3: 微信登录与用户管理

**云函数:**
```javascript
exports.main = async (event, context) => {
  const { OPENID, APPID, UNIONID } = cloud.getWXContext()
  
  let user = await db.collection('users').where({ _openid: OPENID }).get()
  
  if (user.data.length === 0) {
    const { _id } = await db.collection('users').add({
      data: {
        _openid: OPENID,
        appid: APPID,
        unionid: UNIONID,
        createdAt: db.serverDate(),
        lastLoginAt: db.serverDate(),
        profile: event.userInfo || {}
      }
    })
    return { success: true, isNewUser: true, userId: _id, openid: OPENID }
  } else {
    await db.collection('users').doc(user.data[0]._id).update({
      data: { lastLoginAt: db.serverDate() }
    })
    return { 
      success: true, 
      isNewUser: false,
      userId: user.data[0]._id,
      openid: OPENID,
      profile: user.data[0].profile
    }
  }
}
```

**小程序端:**
```javascript
wx.login({
  success: async () => {
    const { result } = await wx.cloud.callFunction({
      name: 'login',
      data: { userInfo: { nickName, avatarUrl } }
    })
    if (result.isNewUser) console.log('欢迎新用户')
    wx.setStorageSync('userId', result.userId)
  }
})
```

## Example 4: 错误处理

**问题:** 云函数总是返回undefined

**原因:** 异步操作没有正确await

**错误代码:**
```javascript
exports.main = async (event, context) => {
  const result = db.collection('users').get()  // 缺少await
  return result  // 返回Promise而非数据
}
```

**正确代码:**
```javascript
exports.main = async (event, context) => {
  const { data } = await db.collection('users').get()
  return { success: true, data }
}
```
