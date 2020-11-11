#encoding=utf-8
from  selenium import webdriver
import time

driver=webdriver.Firefox()
web_url="https://www.hao123.com"
driver.get(web_url)
time.sleep(5)
driver.maximize_window()

#x--水平，y---垂直，滚动条拖动 window.scrollTo(x,y)
js="window.scrollTo(0,1000)"
driver.execute_script(js)