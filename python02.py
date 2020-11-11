#encoding=utf-8
from time import sleep
from  selenium import webdriver
driver=webdriver.Firefox()
#driver.maximize_window()
#读取浏览器尺寸
size=driver.get_window_size();
sleep(5)
print(u"浏览器:")
print(size);
#设置浏览器尺寸
driver.set_window_size(800,400)
size=driver.get_window_size()
print(size)

pozition=driver.get_window_position()
print("position:%s",pozition)
driver.set_window_position("10","15")
pozition=driver.get_window_position()
print("_position:%s",pozition)

#print(dir(driver))
driver.close()