#encoding=utf-8
from selenium import webdriver
from time import sleep
web_url="https://www.baidu.com"
driver=webdriver.Firefox()
driver.get(web_url)
sleep(5)
driver.maximize_window()

#通过Xpath元素定位，路径中本身的引号与外引号需不同
el=driver.find_element_by_xpath("//*[@id='u1']/a[6]")
el.click()
sleep(5)
driver.close()