#encoding=utf-8
from selenium import webdriver
from time import sleep
url="https://www.baidu.com"
driver=webdriver.Firefox()
driver.get(url)
print("当前的url:",driver.current_url)
print("当前的页面标题：",driver.title)

#保存快照
driver.get_screenshot_as_file('baidu.jpg')
print(driver.page_source)
driver.close()