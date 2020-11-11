#encoding=utf-8
from selenium import webdriver
from time import sleep
web_url="http://www.renren.com/"
driver=webdriver.Firefox()
driver.get(web_url)
sleep(5)
driver.maximize_window()
#定位到账号输入框
el_account=driver.find_element_by_name("email")
el_account.send_keys("112233")
#定位到密码输入框
el_pwd=driver.find_element_by_xpath("//*[@id=\"password\"]")
el_pwd.send_keys("777777")
#定位到登陆按钮
el_login=driver.find_element_by_id("login")
el_login.click()
driver.close()
