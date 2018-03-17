DogeDoge API


---

**host: https://doge.rapospectre.com**

**api_version: v1**

#概要

 2. API请求格式：host + "api" + api_version + 请求地址。（eg: http://zhz.chafanbao.com/api/v1/tanks）
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

