#encoding=utf-8
from selenium import  webdriver
from time import sleep

driver=webdriver.Firefox()
url="https://www.baidu.com"
driver.get(url)
sleep(3)
#定位到搜索框元素
el=driver.find_element_by_id("kw")
print(el)
print(type(el))
#向输入框中输入值
el.send_keys("你好，有缘人")
#定位到搜索按钮
el_click=driver.find_element_by_id("su")
el_click.click()
sleep(5)
driver.close()