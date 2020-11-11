#encoding=utf-8
from selenium import webdriver
import time
#导入鼠标动作链
from selenium.webdriver import ActionChains

driver=webdriver.Firefox()

web_url="https://www.baidu.com"
driver.get(web_url)

#定位到logo元素
el_logo=driver.find_element_by_css_selector("#lg > map > area")

#鼠标右击,操作元素前需要定位出相应的元素并且传入相应的动作，如果要执行动作则调用perform
ActionChains(driver).context_click(el_logo).perform()