#encoding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
web_url="https://www.126.com"
driver.get(web_url)
time.sleep(5)
driver.maximize_window()


