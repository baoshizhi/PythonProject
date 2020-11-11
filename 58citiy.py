#encoding=utf-8
from  selenium import  webdriver
from time import sleep

web_url="https://fz.58.com/"
driver=webdriver.Firefox()
driver.get(web_url)
sleep(5)
driver.maximize_window()

el=driver.find_element_by_link_text("包吃包住")
el.click()
sleep(5)
driver.close()