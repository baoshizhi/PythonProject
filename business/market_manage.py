from business.home_menu import HomeMenu
from selenium.webdriver import ActionChains
from commonlib import globalvar #导入跨文件全局变量.py文件
import  win32api,win32con

import time

#创建一个营销案管理类
class MarketCaseManage(HomeMenu):
    def __init__(self):
        self.driver=globalvar.get_value('g_driver')  # 导入driver会话ID全局变量
    def __del__(self):
        pass
    #模拟键盘鼠标点击某个元素触发其他弹出框消失
    def mouse_click(self,path_lable=None):
        if path_lable is  None:
            path_lable = "div.small-main-router.fl>div.config-wrap>form:nth-child(1)>div>h3"
        ele = self.locate_element("css", path_lable)
        ActionChains(self.driver).click(ele).perform()

    #点击营销案管理菜单项
    def click_marketcase(self):
        #点击营销案管理
        path_marketcase = "/html/body/div/div/div[2]/div[1]/ul/div/label[2]/li/ul/div/label[1]/li/span"
        self.click("xpath", path_marketcase)

    #创建营销案
    def cre_marketcase(self,marketcasename):
        #点击新建按钮
        path_create='.button-group>button:nth-child(1)'
        self.click("css",path_create)

        #营销案名称
        path_marketcasename='form:nth-child(1)>div>div>div:nth-child(1)>div>div>div.el-input>input'
        self.input("css",path_marketcasename,marketcasename)

        #营销案类型
        path_marketcasetype='form:nth-child(1)>div>div>div:nth-child(2)>div>div>div>div>div>input'
        self.click("css",path_marketcasetype)
        time.sleep(1)
        #选择下拉框营销案js
        js_marketcasesel="document.querySelector('div.el-select-dropdown:nth-child(5)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span:nth-child(1)').click();"
        self.driver.execute_script(js_marketcasesel)

        #适用地区列表
        path_area='form:nth-child(1) > div > div > div:nth-child(3) > div > div > div > div > div.el-input.el-input--suffix > input'
        self.click("css",path_area)
        #选择下拉框地区js
        js_area="document.querySelector('div.el-select-dropdown:nth-child(6)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1) >span:nth-child(1)').click();"
        self.driver.execute_script(js_area)
        #模拟鼠标点击去除弹出框
        self.mouse_click()


        #适用渠道列表
        path_channel= 'form:nth-child(1)>div>div>div:nth-child(4)>div>div>div>div>div.el-input.el-input--suffix>input'
        self.click("css", path_channel)
        #选择下拉框渠道js
        js_channel="document.querySelector('div.el-select-dropdown:nth-child(7)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span:nth-child(1)').click();"
        self.driver.execute_script(js_channel)
        # 模拟鼠标点击去除弹出框
        self.mouse_click()


        #生效时间
        path_etime="form:nth-child(1)>div>div>div:nth-child(5)>div>div>div>input"
        etime="2020-04-08"
        self.input("css",path_etime,etime)
        #模拟鼠标点击去除弹出框
        self.mouse_click()

        #失效时间
        path_ntime="form:nth-child(1)>div>div>div:nth-child(6)>div>div>div>input"
        ntime = "2025-03-25"
        self.input("css", path_ntime,ntime)
        #模拟鼠标点击去除弹出框
        self.mouse_click()

        #业务平台
        path_bplatform ="div.fl:nth-child(7)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>input:nth-child(1)"
        self.click("css", path_bplatform)
        # 选择业务平台下拉框js
        js_bplatform='document.querySelector("div.el-select-dropdown:nth-child(10)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span:nth-child(1)").click();'
        self.driver.execute_script(js_bplatform)


        #捆绑时长
        path_bindtime="form:nth-child(1)>div>div>div:nth-child(9)>div>div>div>input"
        self.input("css",path_bindtime,"3")

        #捆绑单位
        path_bindunit_input="div.fl:nth-child(10)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>input:nth-child(1)"
        self.click("css",path_bindunit_input)
        #选择捆绑单位下拉框js
        js_bindunit='document.querySelector("body>div:nth-child(11)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(2)>span").click();'
        self.driver.execute_script(js_bindunit)

        #排序数值
        path_ordernum="form:nth-child(1)>div>div>div:nth-child(11)>div>div>div.el-input>input"
        self.input("css",path_ordernum,"5")

        # 将页面滚动条拖到底部,scrollTop设置足够大的值
        # -1代表向下移动一个单位
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-1000)
        time.sleep(3)

        #优惠类型
        path_discounttype="form.el-form:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>input:nth-child(1)"
        self.click("css",path_discounttype)
        #优惠类型下拉框js
        js_distype_xiala="document.querySelector('div:nth-child(12)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span').click();"
        self.driver.execute_script(js_distype_xiala)

        #活动价格
        path_activityprice="form.el-form:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>input:nth-child(1)"
        text_activityprice="1.09"
        self.input("css",path_activityprice,text_activityprice)

        #是否连续性优惠
        path_lxyh="form:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div:nth-child(4)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>div:nth-child(1)>input"
        self.click("css",path_lxyh)
        #连续性优惠下拉框js
        js_lxyh_xiala="document.querySelector('div:nth-child(13)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(2)>span').click();"
        self.driver.execute_script(js_lxyh_xiala)
        #持续月数
        path_continue_month="form:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div:nth-child(5)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>input"
        text_continue_month="6"
        self.input("css",path_continue_month,text_continue_month)

        #设置可受理时间
        path_handletime="form.el-form:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div:nth-child(6)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>button:nth-child(2)"
        self.click("css",path_handletime)

        # 周期类型
        path_periodtype = ".shelve-form>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>input:nth-child(1)"
        self.click("css", path_periodtype)
        # 选择周期类型下拉框js(每周)
        js_periodtype = "document.querySelector('div.el-select-dropdown:nth-child(16)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(2)>span:nth-child(1)').click();"
        self.driver.execute_script(js_periodtype)
        # 点击星期输入框
        # path_week_input="div.el-form-item:nth-child(2)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>div:nth-child(2)>input:nth-child(1)"
        # self.click("css",path_week_input)
        js_week_input = "document.querySelector('div.el-form-item:nth-child(2)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>div:nth-child(2)>input:nth-child(1)').click();"
        self.driver.execute_script(js_week_input)

        # 选择星期下拉框选项js(全选)
        js_week_xiala = "document.querySelector('div.el-select-dropdown:nth-child(17)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span:nth-child(1)').click();"
        self.driver.execute_script(js_week_xiala)
        # 模拟鼠标点击其他元素隐藏下拉框
        css_path = ".el-dialog__title"
        self.mouse_click(css_path)
        #点击确定按钮
        path_confirm = '.el-dialog__footer > div:nth-child(1) > button:nth-child(1)'
        self.click("css", path_confirm)

        #产品列表
        path_selpro = "form.el-form:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div:nth-child(7)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>button:nth-child(2)"
        self.click("css", path_selpro)
        #勾选前面2个产品
        path1_pro = "/html/body/div[16]/div/div[2]/div[2]/div/div/div[1]/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span"
        path2_pro = "tr.el-table__row:nth-child(2)>td:nth-child(1)>div:nth-child(1)>label:nth-child(1)>span:nth-child(1)>span:nth-child(1)"
        self.click("xpath", path1_pro)
        self.click("css", path2_pro)
        #勾选完选择确定按钮
        time.sleep(0.5)
        path_confirm="body > div.el-dialog__wrapper.select-dialog>div>div.el-dialog__footer>div>button.el-button.search.el-button--primary>span"
        self.click("css",path_confirm)

        time.sleep(0.5)
        # 提交
        path_submit = "#app>div>div.main-page.clearfix>div.small-main-router.fl>div.config-wrap>div>button:nth-child(2)"
        self.click("css", path_submit)

        #获取创建后的营销案名称
        path_querymarketcasename='//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/div'
        marketcasename= self.get_text("xpath",path_querymarketcasename)
        return marketcasename











