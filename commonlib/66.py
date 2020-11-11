import  re
import requests
# json_data_source="{'result': False, 'error': {'code': 1210099, 'message': 'InvocationException: code=400;msg=CommonExceptionData [message=Parameters not valid or types not match.]'}}"
# json_data = re.sub("\s", "", json_data_source)

url="http://10.45.138.39:8380/mkt-planning-microservice/query/qryMarketCaseList"
para='{\
  "pageSize": "1",\
  "curPage": "1",\
  "mktCaseName": "59111107测试营销案名称",\
  "mktCaseType": "1",\
  "mktCaseTmplId": "5910757",\
  "belongGroupId": "10001212",\
  "effectStatus": "1",\
  "auditStatus": "1",\
  "effectTime": "20000101",\
  "expireTime": "30000101",\
  "startCreateTime": "20000101000000",\
  "endCreateTime": "30000101000000",\
  "operatorId": "1110757"\
}'
para1=para.encode("utf-8")
res_data = requests.post(url, data=para1)
json_data_source=res_data.text
print("json_Data_source\n",json_data_source)
json_data = re.sub("\s", "", json_data_source)
print("json_Data\n",json_data)

ss="<?xml443"
print(ss[0:5])