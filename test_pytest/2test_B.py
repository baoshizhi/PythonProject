
class Test_B():
    bb = "BBBBB"
    print(bb)
    def testfune(self):
        print("fune-self:", self)
    def testfunf(self):
        print("funf-self:",self)
    def testfunc(self):
        print("func-self:", self)

class Test_A():
    def test_fund(self):
        print("---test_fund---")
        pass


def test_funb():
    print("---test_funb--")

def test_funa():
    print("---test_funa--")







# from selenium import webdriver
# # from selenium.webdriver.support.select import Select
# # import time
# web_url01="https://www.baidu.com"
# web_url02="https://www.hao123.com"
# web_url03="https://www.taobao.com"
# import time
# driver1=webdriver.Firefox()
# driver1.get(web_url01)
# print("driver1:",driver1)
#
# driver=webdriver.Firefox()
# driver.get(web_url02)
# print("driver2:",driver)
# driver.quit()
#
# driver=webdriver.Firefox()
# driver.get(web_url03)
# print("driver3:",driver)
# time.sleep(5)
# driver.quit()
#
# print("1111")
# print(driver)
# driver1.quit()
# print("1111")


# driver=webdriver.Firefox()
# driver.delete_all_cookies()
# driver.maximize_window()
# driver.get(web_url)
# #time.sleep(3)
#
# ele=driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/form/div[1]/div/div[1]/input")
# ele.send_keys("baoshizhi")
#
# ele=driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div/div/form/div[2]/div/div/input")
# ele.send_keys("123qweQWE+")
# time.sleep(15)
#
# ele=driver.find_element_by_css_selector("button>span")
# ele.click()
# time.sleep(3)
#
# ele=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/ul/div/label[1]/li/div/span')
# ele.click()
#
# ele=driver.find_element_by_css_selector('label:nth-child(2)>li>span')
# ele.click()
#
# sel_path='div:nth-child(3)>div>div>div>div>input'
# ele=driver.find_element_by_css_selector(sel_path)
# Sel=Select(ele)
# Sel.select_by_index(0)




# def fun01():
#     print("--fun01---")
#     a=1
#     print("a:",a)
#     fun04()
#
# def fun02():
#     fun01()
#     print("--fun02---")
#     b=2
#     print("b:",b)
#     fun03()
#
# def fun03():
#     fun02()
#     print("--fun03---")
#     c=3
#     print("c:",c)
#     fun01()
#
# def fun04():
#     fun01()
#     d=4
#     print("d:", d)
#
#
# fun04()



# class LG01:
#     def __init__(self):
#         print("---LG01--init")
#
#     def __del__(self):
#         print("---LG01--del")
#
#     def fun01(self):
#         print("--fun01---")
#
#
# class LG02(LG01):
#     def __init__(self):
#         #print("--LG02-init--")
#         LG01.__init__(self)
#
#     def __del__(self):
#         #print("---LG02--del")
#         LG01.__del__(self)
#         pass
#
#     def fun02(self):
#         print("--fun02---")
# LG=LG02()
#
#
#









# from selenium import webdriver
#
# #引入WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
# #引入expected_conditions类，并重命名为EC
# from selenium.webdriver.support import expected_conditions as EC
# #引入By类
# from selenium.webdriver.common.by import By
#
#
# import time
# driver=webdriver.Firefox()
#
# driver.maximize_window()
# web_url="http://10.46.180.96:8088/cscweb/index.html#/home"
# driver.get(web_url)
#
# u_path="//*[@id='app']/div/div[2]/div/div/form/div[1]/div/div[1]/input"
# driver.find_element_by_xpath(u_path).send_keys("baoshizhi")
#
# p_path="//*[@id='app']/div/div[2]/div/div/form/div[2]/div/div/input"
# driver.find_element_by_xpath(p_path).send_keys("123qweQWE+")
#
# time.sleep(15)
# lg_path="button>span"
# driver.find_element_by_css_selector(lg_path).click()
#
# path_promanage = '//*[@id="app"]/div/div[2]/div[1]/ul/div/label[1]/li/div/span'
#
# #time.sleep(2)
#
# driver.implicitly_wait(25)
#
# # #设置显式等待
# # print("111111")
# #ele_wait=WebDriverWait(driver,60,0.5)#总共轮循60秒，每0.5秒轮循一次
# # ele_wait.until(EC.presence_of_element_located((By.XPATH,path_promanage)))
# # print("222222")
# print("33333")
# ele=driver.find_element_by_xpath(path_promanage)
# print("44444")
# print(ele)
# ele.click()

