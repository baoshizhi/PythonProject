#encoding=utf-8
#导入webdriver包
from selenium import webdriver
from time import sleep
#打开浏览器
driver=webdriver.Firefox()

#网页地址
url01="https://www.baidu.com"
url02="https://zhuanlan.zhihu.com"

#打开网页
driver.get(url01)
print("访问百度:",driver.current_url)
driver.get(url02)
print("访问知乎：",driver.current_url)

sleep(10)
#后退
driver.back();

#前进
driver.forward()