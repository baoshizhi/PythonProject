#encoding=utf-8
from selenium import webdriver
from time import sleep
driver=webdriver.Firefox()
web_url="https://www.baidu.com"
driver.get(web_url)
sleep(3)
driver.maximize_window()

ex_01=driver.find_element_by_id("kw")
ex_01.send_keys("selenium")
ex_02=driver.find_element_by_id("su")
ex_02.click()
#获取搜索结果的组元素
ex_list=driver.find_elements_by_css_selector('div[id="content_left"]>div[id="1"]>h3>a')
print(ex_list)
driver.close()
