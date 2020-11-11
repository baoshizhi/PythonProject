#encoding=utf-8
from selenium import webdriver
from time import sleep
web_url="https://www.baidu.com"
driver=webdriver.Firefox()
driver.get(web_url)
sleep(3)
driver.maximize_window()

el=driver.find_element_by_partial_link_text("hao")
el.click()
sleep(5)
driver.close()