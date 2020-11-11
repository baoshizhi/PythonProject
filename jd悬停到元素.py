#encoding=utf-8
from  selenium import  webdriver
import  time
from selenium.webdriver import  ActionChains


driver=webdriver.Firefox()

web_url="https://www.jd.com"
driver.get(web_url)
time.sleep(5)
driver.maximize_window()

#获取一组分类子元素
el_list=driver.find_elements_by_class_name("cate_menu_item")

for el in el_list:
    ActionChains(driver).move_to_element(el).perform()
    time.sleep(3)
driver.quit()