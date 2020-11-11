#encoding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
web_url="https://fz.58.com/chuzu/?PGTID=0d100000-0013-05bd-6e3c-bb93cfa9bc29&ClickID=1"
driver.get(web_url)
time.sleep(5)
driver.maximize_window()

#获取房屋出租元素列表
el_list=driver.find_elements_by_css_selector("li> div:nth-child(2) > h2:nth-child(1) > a:nth-child(1)")
for el in el_list:
    print("标题:",el.text,"链接:",el.get_attribute("href"))
print(el_list)

driver.close()
