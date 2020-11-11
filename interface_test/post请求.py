#encoding=utf-8
import requests

url="http://192.168.65.111:7000/api/v1/user/me"
para={"name":"bsz01","password":"U2FsdGVkX1/Gpe80bPelG5aUw5gAKkfTYaHHvrHaIro="}

#发起post请求，并将返回的数据存放到resp_data变量
resp_data=requests.post(url,data=para)

#打印状态码
print("状态码:",resp_data.status_code)

#打印返回的json数据串
json_data=resp_data.json()
print("返回的json数据串:",json_data)

#打印返回的json数据串中指定的字段值
j_fname=json_data["fname"]
j_sex=json_data["sex"]
j_name=json_data["name"]

print("返回的姓名:\n",j_fname)

print("返回的性别:\n",j_sex)

print("返回的账号:\n",j_name)