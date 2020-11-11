import requests
import re  #用于ID正交法匹配查找session_id

#定义个变量用来存储请求会话session，以保证后续的两个请求接口是同一个请求通道
se=requests.session()
url_nav="http://127.0.0.1:1080/webtours/nav.pl?in=home"
para_nav=None
respon_data_nav=se.get(url_nav,params=para_nav)
#打印返回的text内容
print("返回的接口内容:\n",respon_data_nav.text)

#通过正交法匹配respon_data_01.text文本中，左边界为name=userSession value=，右边界为>的会话ID值
#并存放到list类型变量session_id内，通过下标session_id[0]取值
session_id=re.findall("name=userSession value=(.+?)>",respon_data_nav.text)
print("session_id:",session_id)

url_login="http://127.0.0.1:1080/webtours/login.pl"
para_login={"userSession":session_id[0],"username":"bsz","password":"bsz1234","login.x":"57","login.y":"14","JSFormSubmit":"off"}

#发送post请求
respon_data_login=se.post(url_login,data=para_login)

#返回的text值
res_text=respon_data_login.text
print("登陆post请求返回值:\n",res_text)
print("===========================================\n",res_text.title())
res_text.encode()


