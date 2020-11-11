#encoding=utf-8
from selenium import  webdriver
import  time

driver=webdriver.Firefox()
web_url="https://www.baidu.com"
driver.get(web_url)
time.sleep(3)
driver.maximize_window()

el_set=driver.find_element_by_link_text("设置")
el_set.click()

#进入搜索设置并点击
el_search=driver.find_element_by_css_selector(".setpref")
el_search.click()

#定位保存设置按钮
el_save=driver.find_element_by_css_selector(".prefpanelgo")
el_save.click()
time.sleep(3)
#进入警告框中并且点击确定接受
# driver.switch_to.alert.accept()

#进入警告框中并直接关闭警告框
driver.switch_to.alert.dismiss()
