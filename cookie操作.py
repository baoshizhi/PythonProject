#encoding=utf-8
from  selenium import  webdriver

driver=webdriver.Firefox()
web_url="http://www.youdao.com"
driver.get(web_url)

#获取cookies值,直接调用，不需要参数
data=driver.get_cookies()
print("data:",data)
#删除所有cookies
driver.delete_all_cookies()
#设置cookies
cookie={"name":"YOUDAO_MOBILE_ACCESS_TYPE","value":"101"}
driver.add_cookie(cookie)
data2=driver.get_cookies()
print("data2:",data2)


