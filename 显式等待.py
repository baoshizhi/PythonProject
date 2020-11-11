#encoding=utf-8
from  selenium import  webdriver
#导入By类
from  selenium.webdriver.common.by import  By
#导入webdriver等待类
from  selenium.webdriver.support.ui import WebDriverWait
#导入webdriver预期条件设置
from  selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
web_url="https://www.baidu.com"
driver.get(web_url)
#在不超过10秒的前提下，每隔0.5秒去检测指定的页面元素是否出现，若出现则停止等待，若不出现超过10秒后停止检测，
#By.NAME  NAME为大写
el=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.NAME,"mp1")))
print(el)
driver.close()