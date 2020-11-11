#encoding=utf-8
from selenium import  webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import time
#引入WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
#引入expected_conditions类，并重命名为EC
from selenium.webdriver.support import expected_conditions as EC
#引入By类
from selenium.webdriver.common.by import By


class CommShare:
    # 打开指定的url,并设置隐式等待
    def open_url(self,web_url):
        #打开浏览器并最大化浏览器
        #self.driver=webdriver.Firefox()
        self.driver=webdriver.Chrome()
        '''隐式等待，紧跟在打开的浏览器后面只需声明一次，对整个driver生命周期均有效'''
        self.driver.implicitly_wait(20)

        # #设定显式等待，与until配合使用
        #self.ele_wait= WebDriverWait(self.driver,60,0.5)  # 总共轮循60秒，每0.5秒轮循一次
        self.driver.maximize_window()
        self.driver.get(web_url)

    '退出浏览器'
    def web_quit(self):
        self.driver.quit()

    #八种定位元素方法的封装,返回定位到的元素
    #如果异常捕获到一次之后经sleep后重试如果还是异常则不进行重试定位元素
    def locate_element(self,locate_type,value):
        el=None
        if locate_type == "id":
            # 等待指定元素出现
            #self.ele_wait.until(EC.presence_of_element_located((By.ID,value)))
            el = self.driver.find_element_by_id(value)
        elif locate_type == "name":
            # self.ele_wait.until(EC.presence_of_element_located((By.NAME, value)))
            el = self.driver.find_element_by_name(value)
        elif locate_type == "class":
            # self.ele_wait.until(EC.presence_of_element_located((By.CLASS_NAME, value)))
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == "link":
            # self.ele_wait.until(EC.presence_of_element_located((By.LINK_TEXT, value)))
            el = self.driver.find_element_by_link_text(value)
        elif locate_type == "plink":
            # self.ele_wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, value)))
            el = self.driver.find_element_by_partial_link_text(value)
        elif locate_type == "tag":
            # self.ele_wait.until(EC.presence_of_element_located((By.TAG_NAME, value)))
            el = self.driver.find_element_by_tag_name(value)
        elif locate_type == "xpath":
            # self.ele_wait.until(EC.presence_of_element_located((By.XPATH, value)))
            el = self.driver.find_element_by_xpath(value)
        elif locate_type == "css":
            # self.ele_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
            el = self.driver.find_element_by_css_selector(value)
        return el

    #对定位的目标元素进行点击操作封装
    def click(self,locate_type,value):
        #调用locate_element函数
        el=self.locate_element(locate_type,value)
        #有定位到元素，但因不可见无法点击的情况处理
        self.driver.execute_script("arguments[0].click();",el)
        #ActionChains(self.driver).move_to_element(el).perform()
        #ActionChains(self.driver).click(el).perform()


        #time.sleep(1)
        # try:
        #     el.click()
        # except Exception as err:
        #     print("有报错就强制等待3秒:\n")
        #     print(err)
        #     time.sleep(3)
        #     el.click() #3秒后再次点击

    #清空目标元素的输入框文本,如果用el.clear()只是清空文本，不会清空value值，
    def del_input(self, locate_type, value,js_delreadonly=None):
        if js_delreadonly is not None:
            #去除只读属性
            self.driver.execute_script(js_delreadonly)
        el = self.locate_element(locate_type, value)
        el.send_keys(Keys.CONTROL, 'a')  # 模拟键盘ctrl+a全选
        el.send_keys(Keys.DELETE)  # 清空输入框的可见文本及文本对应的value值
        return el

    #对定位到的目标元素进行文本输入
    def input(self,locate_type,value,text):
        #输入之前先清空文本及value值
        el=self.del_input(locate_type,value)
        #对目标元素进行文本输入
        el.send_keys(text)

    #获取定位到的目标元素的文本内容XXX   <a>XXX</a>
    def get_text(self,locate_type,value):
        el=self.locate_element(locate_type,value)
        return el.text


    #获取定位到的目标元素的标签属性值
    def get_attr(self,locate_type,value,attr_name):
        el=self.locate_element(locate_type,value)
        return el.get_attribute(attr_name)

    #获取下拉框元素(根据传入的类型【下标index/属性值value/文本值text】,默认index方式获取下拉元素)
    '''如果是input标签，就只能点击去操作了，不适用本方法获取元素'''
    def get_select_ele(self,locate_type,value,sel_value,sel_type="index"):
        el=self.locate_element(locate_type,value)
        Sel= Select(el) #根据元素创建一个Select对象
        if sel_type=="index":
            #sel_value=int(sel_value)
            Sel.select_by_index(sel_value)
        elif sel_type=="value":
            Sel.select_by_value(sel_value)
        elif sel_type=="text":
            Sel.select_by_visible_text(sel_value)





#自身调用执行时才执行以下代码
if __name__=='__main__':
    print("123456健康减肥看见")
    #com=CommShare()
    #com.open_url("https://www.baidu.com")
    #com.locate_element("link","新闻").click()
    #com.locate_element("name", "wd").send_keys("我爱你中国")
    #com.input("name","wd","我和我的祖国")
    #com.locate_element("id", "su").click()
    #com.locate_element("class", "bg").click()
    #com.locate_element("xpath", "//*[@id='su']").click()
    #com.locate_element("css", "#su").click()
    #com.click("css","#su")

    # text=com.get_text("name","tj_trxueshu")
    # print("获取到的标签文本:",text)
    # attrname=com.get_attr("name","tj_trxueshu","href")
    # print("标签对应的href属性值：",attrname)