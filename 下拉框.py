#encoding=utf-8
from selenium import  webdriver
import time
#导入select类
from selenium.webdriver.support.select import Select

driver=webdriver.Firefox()

web_url="https://www.baidu.com"
driver.get(web_url)
time.sleep(3)
driver.maximize_window()

#定位到设置按钮并点击
el_set=driver.find_element_by_link_text("设置")
el_set.click()
#定位到搜索设置并点击
time.sleep(2)
el_search=driver.find_element_by_css_selector(".setpref")
el_search.click()

#定位到下拉框元素
el_xl=driver.find_element_by_id("nr")
#创建下拉框对象
selobj=Select(el_xl)

#根据索引选择下拉框中的某个值
# selobj.select_by_index(0)
# time.sleep(2)
# selobj.select_by_index(1)
# time.sleep(2)
# selobj.select_by_index(2)
# time.sleep(2)

#通过value值(文本型)进行选择下拉框中的值
# selobj.select_by_value("50")
# time.sleep(2)
# selobj.select_by_value("20")
# time.sleep(2)
# selobj.select_by_value("10")
# time.sleep(2)

#通过可见文本进行选择下拉框中的值
selobj.select_by_visible_text("每页显示50条")
time.sleep(2)
selobj.select_by_visible_text("每页显示10条")
time.sleep(2)
selobj.select_by_visible_text("每页显示20条")
time.sleep(2)