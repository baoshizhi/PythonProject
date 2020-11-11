#encoding=utf-8
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Firefox()
web_url="https://cn.bing.com"
driver.get(web_url)

#定位到输入框
el_search=driver.find_element_by_id("sb_form_q")

#输入搜索的内容
el_search.send_keys("自动化selenium")
#全选刚刚输入的内容
time.sleep(2)
el_search.send_keys(Keys.CONTROL,"a")
#剪切刚刚输入的内容
el_search.send_keys(Keys.CONTROL,"x")
time.sleep(2)
#黏贴刚刚输入的内容
el_search.send_keys(Keys.CONTROL,"v")
time.sleep(1)

el_search.clear()
el_search.send_keys("seleniumm")
time.sleep(2)
el_search.send_keys(Keys.BACK_SPACE)
time.sleep(3)

driver.quit()




