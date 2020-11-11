#encoding=utf-8
from selenium import  webdriver
import  time
import os

driver=webdriver.Firefox()
driver.maximize_window()
# 当前路径
# file_path='file:///'+os.path.abspath('.')
# 当前路径的上层路径
# file_path='file:///'+os.path.abspath('..')
# 本地绝对路径
file_path='file:///'+os.path.abspath('D:\example_frame.html')
print("文件路径：",file_path)
#访问本地文件
driver.get(file_path)
print(driver.title)
time.sleep(5)
print(driver.current_url)
print(driver.current_window_handle)

#切换到第一个表单中
driver.switch_to.frame("itcast_frame1")
#切换到第二个表单中
driver.switch_to.frame("itcast_frame2")

#定位到第二个表单内部的搜索输入框
el_search=driver.find_element_by_id("sb_form_q")
#print(el_search)
#在输入框中输入内容
el_search.send_keys("自动化selenium")
#定位到第二个表单内部的搜索按钮
el_click=driver.find_element_by_id("sb_form_go")
#print(el_click)
#点击搜索按钮
el_click.click()


#定位到最深层表单中的一个元素(表单中的搜索框)以显示当前处于最深层表单当中
el_inner=driver.find_element_by_id("sb_form_q")
print("当前处于最深层表单之中")

#回到最外层http界面
driver.switch_to.default_content()
try:
    #重新查找之前的内层表单的元素
    el_inner=driver.find_element_by_id("sb_form_q")
except:
    print("已经从最内层表单退出")
time.sleep(3)
driver.close()