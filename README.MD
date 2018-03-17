DogeDoge API


---

**host: https://doge.rapospectre.com**

**api_version: v1**

# 概要

 2. API请求格式：host + "api" + api_version + 请求地址。（eg: https://doge.rapospectre.com/api/v1/goods）
 3. API返回格式：`json:{"status":1,"body":{}}`status返回操作结果码,body包含返回信息，如果无返回信息，body为空。
 4. status结果码对照表：

|status结果码|状态|
| --------------  | :---: |
|0|未知错误|
|1|成功|
|2|权限不足|
|3|帐号不存在|
|4|数据错误|
|5|密码错误|
|6|已存在|
|7|不存在|
|8|已过期|
|10|验证码为空|
|11|验证码错误|


# API认证



## **商城列表**

```
GET /api/v1/goods/
```

### **Parameters**


### **Return**

成功
```
{
　　"body":{
　　　　"page_obj":{

　　　　},
　　　　"is_paginated":false,
　　　　"goods_list":[
　　　　　　{
　　　　　　　　"price":1,
　　　　　　　　"id":1,
　　　　　　　　"name":"屎人"
　　　　　　},
　　　　　　{
　　　　　　　　"price":10,
　　　　　　　　"id":2,
　　　　　　　　"name":"毛绒玩具"
　　　　　　},
　　　　　　{
　　　　　　　　"price":5,
　　　　　　　　"id":3,
　　　　　　　　"name":"仙女棒"
　　　　　　}
　　　　]
　　},
　　"status":1,
　　"msg":"success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```


## **商品购买**

```
POST /api/v1/goods/{gid}/
```

### **Parameters**


### **Return**

成功
```
{
    "body": {
        "user": {
            "nick": "用户昵称",
            "money": 3
        }
    },
    "status": 1,
    "msg": "success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```


## **获取用户信息与宠物**

```
GET /api/v1/user/pet/
```

### **Parameters**


### **Return**

成功
```
{
　　"body":{
　　　　"pet":{
　　　　　　"picture":"2",
　　　　　　"eated":false,
　　　　　　"name":"2",
　　　　　　"showerd":false,
　　　　　　"wish":"2",
　　　　　　"belong":{
　　　　　　　　"province":"1",
　　　　　　　　"city":"1",
　　　　　　　　"user_id":"1",
　　　　　　　　"country":"1",
　　　　　　　　"nick":"1",
　　　　　　　　"avatar":"1",
　　　　　　　　"male":1
　　　　　　},
　　　　　　"character":"2",
　　　　　　"sex":1,
　　　　　　"type":1
　　　　}
　　},
　　"status":1,
　　"msg":"success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```

## **新建|更新 个人信息**

```
POST /api/v1/user/
```

### **Parameters**
* nick(_Optional_|string)-昵称
* avatar(_Optional_|string)-头像
* male(_Optional_|string)-性别
* age(_Optional_|string)-年龄
* sports(_Optional_|string)-运动
* foods(_Optional_|string)-食物
* province(_Optional_|string)-省份
* city(_Optional_|string)-城市
* country(_Optional_|string)-国家
* travel(_Optional_|string)-旅行
* user_id(_Optional_|string)-userid


### **Return**

成功
```
{
    "body": {
        "user": {
            "nick": "用户昵称",
            "token": "8Tpm0LXPAIuxVU4hd6kc3QfHxejywtSZvnGiJB92etvYnlo5EyrjDbMuCqabdfhz",
            "user_id": "123",
            "money": 0
        }
    },
    "status": 1,
    "msg": "success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```

## **查询 个人信息**

```
GET /api/v1/user/
```

### **Parameters**
* user_id(_Optional_|string)-userid


### **Return**

成功
```
{
    "body": {
        "user": {
            "nick": "用户昵称",
            "token": "8Tpm0LXPAIuxVU4hd6kc3QfHxejywtSZvnGiJB92etvYnlo5EyrjDbMuCqabdfhz",
            "user_id": "123",
            "money": 0
        }
    },
    "status": 1,
    "msg": "success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```

## **查询 综合信息（心跳包）**

```
GET /api/v1/user/pet/
```

### **Parameters**


### **Return**

成功
```
{
　　"body":{
　　　　"pet":{
　　　　　　"picture":"2",
　　　　　　"eated":true,
　　　　　　"name":"2",
　　　　　　"showerd":true,
　　　　　　"wish":"2",
　　　　　　"belong":{
　　　　　　　　"province":"1",
　　　　　　　　"city":"1",
　　　　　　　　"user_id":"1",
　　　　　　　　"money":10,
　　　　　　　　"country":"1",
　　　　　　　　"nick":"1",
　　　　　　　　"avatar":"1",
　　　　　　　　"pick":0,
　　　　　　　　"male":1
　　　　　　},
　　　　　　"character":"2",
　　　　　　"sex":1,
　　　　　　"type":1
　　　　}
　　},
　　"status":1,
　　"msg":"success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```

# **新建宠物**

```
POST /api/v1/user/pet/
```

### **Parameters**
* type(_Optional_|string)-狗子类型
* sex(_Optional_|string)-性别
* character(_Optional_|string)-性格
* wish(_Optional_|string)-希望的性格

### **Return**

成功
```
{
　　"body":{
　　　　"pet":{
　　　　　　"picture":"2",
　　　　　　"eated":true,
　　　　　　"name":"2",
　　　　　　"showerd":true,
　　　　　　"wish":"2",
　　　　　　"belong":{
　　　　　　　　"province":"1",
　　　　　　　　"city":"1",
　　　　　　　　"user_id":"1",
　　　　　　　　"money":10,
　　　　　　　　"country":"1",
　　　　　　　　"nick":"1",
　　　　　　　　"avatar":"1",
　　　　　　　　"pick":0,
　　　　　　　　"male":1
　　　　　　},
　　　　　　"character":"2",
　　　　　　"sex":1,
　　　　　　"type":1
　　　　}
　　},
　　"status":1,
　　"msg":"success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```



# **拥有的礼物接口**

```
POST /api/v1/gifts/
```

### **Parameters**

### **Return**

成功
```
{
　　"body":{
　　　　"gift_list":[
　　　　　　{
　　　　　　　　"picture":"",
　　　　　　　　"use":false,
　　　　　　　　"name":"毛线团",
　　　　　　　　"goods_id":2,
　　　　　　　　"belong_id":4,
　　　　　　　　"create_time":"2018-03-17 21:29:13",
　　　　　　　　"modify_time":"2018-03-17 21:29:13",
　　　　　　　　"id":5
　　　　　　},
　　　　　　{
　　　　　　　　"picture":"",
　　　　　　　　"use":false,
　　　　　　　　"name":"毛线团",
　　　　　　　　"goods_id":2,
　　　　　　　　"belong_id":4,
　　　　　　　　"create_time":"2018-03-17 21:11:11",
　　　　　　　　"modify_time":"2018-03-17 21:11:11",
　　　　　　　　"id":4
　　　　　　},
　　　　　　{
　　　　　　　　"picture":"",
　　　　　　　　"use":false,
　　　　　　　　"name":"毛线团",
　　　　　　　　"goods_id":2,
　　　　　　　　"belong_id":4,
　　　　　　　　"create_time":"2018-03-17 21:11:10",
　　　　　　　　"modify_time":"2018-03-17 21:11:10",
　　　　　　　　"id":3
　　　　　　},
　　　　　　{
　　　　　　　　"picture":"",
　　　　　　　　"use":false,
　　　　　　　　"name":"毛线团",
　　　　　　　　"goods_id":2,
　　　　　　　　"belong_id":4,
　　　　　　　　"create_time":"2018-03-17 21:11:08",
　　　　　　　　"modify_time":"2018-03-17 21:11:08",
　　　　　　　　"id":2
　　　　　　},
　　　　　　{
　　　　　　　　"picture":"",
　　　　　　　　"use":false,
　　　　　　　　"name":"毛线团",
　　　　　　　　"goods_id":2,
　　　　　　　　"belong_id":4,
　　　　　　　　"create_time":"2018-03-17 21:11:03",
　　　　　　　　"modify_time":"2018-03-17 21:11:03",
　　　　　　　　"id":1
　　　　　　}
　　　　],
　　　　"page_obj":{

　　　　},
　　　　"is_paginated":false
　　},
　　"status":1,
　　"msg":"success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```

# **捡屎接口**

```
GET /api/v1/pick/
```

### **Parameters**

### **Return**

成功
```
{
　　"body":{
　　　　"user":{
　　　　　　"money":4,
　　　　　　"user_id":"123",
　　　　　　"id":4,
　　　　　　"pick":0
　　　　}
　　},
　　"status":1,
　　"msg":"success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```


# **喂食、洗澡接口**

```
GET /api/v1/pet/action/
```

### **Parameters**
* action(_Optional_|string)-1 喂食 2 洗澡

### **Return**

成功
```
{
　　"body":{
　　　　"ttuser":{
　　　　　　"money":0,
　　　　　　"user_id":"123",
　　　　　　"id":4
　　　　}
　　},
　　"status":1,
　　"msg":"success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```


# **邂逅列表接口**

```
GET /api/v1/encounters/
```

### **Parameters**

### **Return**

成功
```
{
　　"body":{
　　　　"petship_list":[
　　　　　　{
　　　　　　　　"receiver_id":4,
　　　　　　　　"read":true,
　　　　　　　　"receiver_gift_id":2,
　　　　　　　　"sender_id":2,
　　　　　　　　"receiver_gift":{
　　　　　　　　　　"picture":"",
　　　　　　　　　　"use":false,
　　　　　　　　　　"name":"毛线团",
　　　　　　　　　　"goods_id":2,
　　　　　　　　　　"belong":{
　　　　　　　　　　　　"province":"青海省",
　　　　　　　　　　　　"city":"西宁",
　　　　　　　　　　　　"user_id":"123",
　　　　　　　　　　　　"money":0,
　　　　　　　　　　　　"last_pick_time":"2018-03-17 21:06:31",
　　　　　　　　　　　　"sports":"羽毛球",
　　　　　　　　　　　　"country":"中国",
　　　　　　　　　　　　"nick":"用户昵称",
　　　　　　　　　　　　"foods":"牛肉",
　　　　　　　　　　　　"create_time":"2018-03-17 21:01:27",
　　　　　　　　　　　　"modify_time":"2018-03-17 22:41:20",
　　　　　　　　　　　　"pick":0,
　　　　　　　　　　　　"male":1,
　　　　　　　　　　　　"travel":"宅1",
　　　　　　　　　　　　"id":4,
　　　　　　　　　　　　"avatar":"http://static.rapospectre.com/bianhua@icon.png"
　　　　　　　　　　},
　　　　　　　　　　"belong_id":4,
　　　　　　　　　　"create_time":"2018-03-17 21:11:08",
　　　　　　　　　　"modify_time":"2018-03-17 21:11:08",
　　　　　　　　　　"id":2
　　　　　　　　},
　　　　　　　　"create_time":"2018-03-17 22:52:44",
　　　　　　　　"modify_time":"2018-03-17 23:17:49",
　　　　　　　　"receiver":{
　　　　　　　　　　"picture":"",
　　　　　　　　　　"name":"用户昵称的狗子",
　　　　　　　　　　"wish":"3",
　　　　　　　　　　"belong":{
　　　　　　　　　　　　"province":"青海省",
　　　　　　　　　　　　"city":"西宁",
　　　　　　　　　　　　"user_id":"123",
　　　　　　　　　　　　"money":0,
　　　　　　　　　　　　"last_pick_time":"2018-03-17 21:06:31",
　　　　　　　　　　　　"sports":"羽毛球",
　　　　　　　　　　　　"country":"中国",
　　　　　　　　　　　　"nick":"用户昵称",
　　　　　　　　　　　　"foods":"牛肉",
　　　　　　　　　　　　"create_time":"2018-03-17 21:01:27",
　　　　　　　　　　　　"modify_time":"2018-03-17 22:41:20",
　　　　　　　　　　　　"pick":0,
　　　　　　　　　　　　"male":1,
　　　　　　　　　　　　"travel":"宅1",
　　　　　　　　　　　　"id":4,
　　　　　　　　　　　　"avatar":"http://static.rapospectre.com/bianhua@icon.png"
　　　　　　　　　　},
　　　　　　　　　　"character":"2",
　　　　　　　　　　"belong_id":4,
　　　　　　　　　　"sex":1,
　　　　　　　　　　"create_time":"2018-03-17 21:06:05",
　　　　　　　　　　"modify_time":"2018-03-17 21:42:27",
　　　　　　　　　　"type":1,
　　　　　　　　　　"id":4
　　　　　　　　},
　　　　　　　　"id":1,
　　　　　　　　"sender_gift_id":1
　　　　　　}
　　　　],
　　　　"page_obj":{

　　　　},
　　　　"is_paginated":false
　　},
　　"status":1,
　　"msg":"success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```


# **邂逅接口**

```
GET /api/v1/encounter/{mid}/
```

### **Parameters**

### **Return**

成功
```
{
　　"body":{
　　　　"petship":{
　　　　　　"receiver_id":4,
　　　　　　"read":true,
　　　　　　"receiver_gift_id":2,
　　　　　　"sender_id":2,
　　　　　　"receiver_gift":{
　　　　　　　　"picture":"",
　　　　　　　　"use":false,
　　　　　　　　"name":"毛线团",
　　　　　　　　"goods_id":2,
　　　　　　　　"belong":{
　　　　　　　　　　"province":"青海省",
　　　　　　　　　　"city":"西宁",
　　　　　　　　　　"user_id":"123",
　　　　　　　　　　"money":0,
　　　　　　　　　　"last_pick_time":"2018-03-17 21:06:31",
　　　　　　　　　　"sports":"羽毛球",
　　　　　　　　　　"country":"中国",
　　　　　　　　　　"nick":"用户昵称",
　　　　　　　　　　"foods":"牛肉",
　　　　　　　　　　"create_time":"2018-03-17 21:01:27",
　　　　　　　　　　"modify_time":"2018-03-17 22:41:20",
　　　　　　　　　　"pick":0,
　　　　　　　　　　"male":1,
　　　　　　　　　　"travel":"宅1",
　　　　　　　　　　"id":4,
　　　　　　　　　　"avatar":"http://static.rapospectre.com/bianhua@icon.png"
　　　　　　　　},
　　　　　　　　"belong_id":4,
　　　　　　　　"create_time":"2018-03-17 21:11:08",
　　　　　　　　"modify_time":"2018-03-17 21:11:08",
　　　　　　　　"id":2
　　　　　　},
　　　　　　"create_time":"2018-03-17 22:52:44",
　　　　　　"modify_time":"2018-03-17 23:26:02",
　　　　　　"receiver":{
　　　　　　　　"picture":"",
　　　　　　　　"name":"用户昵称的狗子",
　　　　　　　　"wish":"3",
　　　　　　　　"belong":{
　　　　　　　　　　"province":"青海省",
　　　　　　　　　　"city":"西宁",
　　　　　　　　　　"user_id":"123",
　　　　　　　　　　"money":0,
　　　　　　　　　　"last_pick_time":"2018-03-17 21:06:31",
　　　　　　　　　　"sports":"羽毛球",
　　　　　　　　　　"country":"中国",
　　　　　　　　　　"nick":"用户昵称",
　　　　　　　　　　"foods":"牛肉",
　　　　　　　　　　"create_time":"2018-03-17 21:01:27",
　　　　　　　　　　"modify_time":"2018-03-17 22:41:20",
　　　　　　　　　　"pick":0,
　　　　　　　　　　"male":1,
　　　　　　　　　　"travel":"宅1",
　　　　　　　　　　"id":4,
　　　　　　　　　　"avatar":"http://static.rapospectre.com/bianhua@icon.png"
　　　　　　　　},
　　　　　　　　"character":"2",
　　　　　　　　"belong_id":4,
　　　　　　　　"sex":1,
　　　　　　　　"create_time":"2018-03-17 21:06:05",
　　　　　　　　"modify_time":"2018-03-17 21:42:27",
　　　　　　　　"type":1,
　　　　　　　　"id":4
　　　　　　},
　　　　　　"id":1,
　　　　　　"sender_gift_id":1
　　　　}
　　},
　　"status":1,
　　"msg":"success"
}
```
失败
```
{
  "body": {},
  "status": 4,
  "msg": "数据缺失"
}
```