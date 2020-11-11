import  requests

#接口测试URL地址
url="http://192.168.65.111:7000/api/v1/sysconf"

#接口测试参数
para={"name":"bsz01","password":"root1234"}

#发起get请求,并将返回的数据存放到变量res_data,注意get函数的参数格式params=
res_data=requests.get(url,params=para)

#获取状态码
code=res_data.status_code
print("状态码:",code)

#获取完整json返回数据
json_data=res_data.json()
print("完整的json返回数据\n",json_data)


#获取返回json串中某个字段的值,json_data[子一级][子二级][子三级]
bs3=json_data["bs3url"]
print("bs3_url:",json_data["bs3url"])




