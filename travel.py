#encoding=utf-8
from selenium import webdriver
from time import sleep
url="https://www.qunar.com/"
driver=webdriver.Firefox()
driver.get(url)
sleep(3)
driver.maximize_window()

#定位到攻略按钮
el01=driver.find_element_by_id("__link_travel__")
el01.click()
sleep(5)

#定位到当地人按钮
el02=driver.find_element_by_id("__link_ddr__")
el02.click()
sleep(5)
driver.close()
