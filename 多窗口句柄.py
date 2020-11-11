#encoding=utf-8
from selenium import  webdriver
import time

driver=webdriver.Firefox()
web_url="https://fz.58.com"
driver.get(web_url)
time.sleep(5)
driver.maximize_window()

el=driver.find_element_by_link_text("福州房产")
#打印浏览器句柄
print("点击福州房产前的窗口句柄:",driver.window_handles)
print("点击之前的URL：",driver.current_url)
el.click()
time.sleep(10)
print("跳转到福州房产后的窗口句柄1:",driver.window_handles)
print("点击之后的URL：",driver.current_url)
print("当前的窗口:",driver.current_window_handle)
print("当前标题：",driver.title)
#保存句柄列表
hand_list=driver.window_handles

#通过句柄进入相关的窗口
driver.switch_to.window(hand_list[1])
print("切换之后的标题：",driver.title)
print("切换之后的窗口句柄：",driver.current_window_handle)
print("切换之后的URL：",driver.current_url)
driver.close()