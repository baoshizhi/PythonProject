#encoding=utf-8
from selenium import webdriver

driver=webdriver.Firefox()
web_url="https://www.amazon.cn/"
driver.get(web_url)
#隐式等待 在10秒内加载完成，不完成则报错
driver.implicitly_wait(10)