#encoding=utf-8
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
web_url="https://www.tmall.com"
driver.get(web_url)
sleep(5)
driver.maximize_window()

#定位天猫国际元素
#ex=driver.find_element_by_css_selector("#content > div.main-nav > div > div > div > a:nth-child(2) > img")
ex=driver.find_element_by_css_selector("")
ex.click()
sleep(5)
driver.close()
