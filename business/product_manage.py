from business.home_menu import HomeMenu
from selenium.webdriver import ActionChains
from commonlib import globalvar #导入跨文件全局变量.py文件
import time



#创建一个【产品管理--内容型产品配置类】ConProConf，
class ConProConf(HomeMenu):
    def __init__(self):
        self.driver=globalvar.get_value('g_driver') #导入driver会话ID全局变量
    def __del__(self):
        pass
    #点击内容型产品配置菜单
    def click_conproconf(self):
        path_conproconf = "/html/body/div[1]/div/div[2]/div[1]/ul/div/label[1]/li/ul/div/label[2]/li/span"
        self.click("xpath", path_conproconf)
    #关闭内容型产品配置菜单
    def close_conproconf(self):
        path_conproconf='//*[@id="tab-/product/demand"]/span'
        self.click("xpath",path_conproconf)


    #模拟键盘鼠标点击某个元素触发其他弹出框消失
    def mouse_click(self):
        path_lable = "#app>div>div.main-page.clearfix>div.small-main-router.fl>div.config-wrap>form:nth-child(1)>div>h3"
        ele = self.locate_element("css", path_lable)
        ActionChains(self.driver).click(ele).perform()

    #根据ID查询产品
    def query_by_id(self,proid,exp_path,locate_type):
        #在产品id输入框输入内容
        path_input='div:nth-child(1)>div>div>div>input'
        self.input('css',path_input,proid)

        time.sleep(1)
        #点击查询按钮
        path_query = 'div:nth-child(1)>div>div>button>span'
        self.click('css',path_query)

        #点击查询完之后，清空原有输入框文本及value值
        self.del_input('css',path_input)

        #获取并返回查询后的预期文本
        #获取查询结果页面中的产品ID元素路径
        text=self.get_text(locate_type,exp_path)
        time.sleep(1)
        return text

    # 根据产品名称查询产品
    def query_by_proname(self,proname,exp_path,locate_type):
        # 在产品名称输入框输入内容
        path_input = 'div>div:nth-child(2)>div>div>div>input'
        self.input('css', path_input, proname)
        time.sleep(1)
        # 点击查询按钮
        path_query = 'div:nth-child(1)>div>div>button>span'
        self.click('css', path_query)

        # 点击查询完之后，清空原有输入框文本及value值
        self.del_input('css', path_input)

        # 获取并返回查询后的预期文本
        # 获取查询结果页面中的产品ID元素路径
        # exp_path='tbody>tr>td.el-table_1_column_1.is-center>div>div'
        text = self.get_text(locate_type,exp_path)
        time.sleep(1)
        return text


    #根据产品类型查询产品,传入参数：产品类型元素点击操作js方法
    def query_by_protype(self,js_text):
        #先输入一个不存在的产品ID进行查询，清空原先默认的查询结果页面
        # 预期文本元素路径
        exp_path = 'div.el-table__body-wrapper.is-scrolling-left>div>span'
        self.query_by_id("10086",exp_path,"css")

        #点击产品类型输入框
        path_sel='div:nth-child(3)>div>div>div>div>input'
        self.click('css',path_sel)


        #有些input类型的下拉框点击下拉框元素时无效,可以用js方法进行点击，先找到目标元素的类名,有可能多个，通过下标值取得准确类名
        #利用[js]方法嵌入点击
        #选择点击要查询的产品类型
        self.driver.execute_script(js_text)

        time.sleep(1)
        #点击查询按钮
        path_query='div:nth-child(1)>div>div>button>span'
        self.click('css', path_query)

        #清除原先输入的内容
        #去除只读属性js_delreadonly
        js_delreadonly="document.querySelector('div:nth-child(3)>div>div>div>div>input').removeAttribute('readonly');"
        self.del_input("css",path_sel,js_delreadonly)

        #获取并返回预期查询结果文本
        #查询结果预期文本的元素路径
        exp_path = '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[3]/div/span'
        return self.get_text("xpath",exp_path)

    #根据产品状态查询产品
    def query_by_prostatus(self,js_text):
        # 先输入一个不存在的产品ID进行查询，清空原先默认的查询结果页面
        # 预期文本元素路径
        exp_path = 'div.el-table__body-wrapper.is-scrolling-left>div>span'
        self.query_by_id("10086",exp_path, "css")

        #点击产品状态输入框
        path_sel = 'div:nth-child(4)>div>div>div>div>input'
        self.click('css', path_sel)

        # 选择点击要查询的产品类型
        self.driver.execute_script(js_text)

        time.sleep(1)
        # 点击查询按钮
        path_query = 'div:nth-child(1)>div>div>button>span'
        self.click('css', path_query)

        #清除原先输入的内容
        #去除只读属性js_delreadonly
        js_delreadonly = "document.querySelector('div:nth-child(4)>div>div>div>div>input').removeAttribute('readonly');"
        self.del_input("css",path_sel,js_delreadonly)

        # 获取并返回预期查询结果文本【查询返回页面的第一行数据当中的产品状态字段值】
        # 查询结果预期文本的元素路径
        exp_path='//table/tbody/tr[1]/td[4]/div/span'
        time.sleep(1)
        return self.get_text("xpath", exp_path)

    #创建单次点播产品
    def cre_pro_dcdb(self,proname_text):
        #点击【创建】按钮进入到创建页面
        cre_path="div.publicMgr-wrap>div.result-wrap>div.clearfix>div>div>button>span"
        self.click("css",cre_path)

        #产品名称
        proname_path="form:nth-child(1)>div>div>div:nth-child(1)>div>div>div>input"
        self.input("css",proname_path,proname_text)

        #产品类型
        protype_path = "form:nth-child(1)>div>div>div:nth-child(2)>div>div>div>div>div.el-input.el-input--suffix>input"
        self.click("css",protype_path)
        #选择单次点播产品
        protype_js="document.querySelector('div:nth-child(5)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span:nth-child(1)').click();"
        self.driver.execute_script(protype_js)
        self.mouse_click()

        #产品价格
        propri_path ="form:nth-child(1)>div>div>div:nth-child(3)>div>div>div>input"
        propri_text="1.05"
        self.input("css",propri_path,propri_text)

        #生效时间(日期框当input框处理)
        proetime_path="form:nth-child(1)>div>div>div:nth-child(4)>div>div>div.el-date-editor.el-input.el-input--prefix.el-input--suffix.el-date-editor--time>input"
        proetime_text="2020-04-08"
        self.input("css",proetime_path,proetime_text)
        #模拟鼠标点击其他任何一个地方来关闭日期框
        self.mouse_click()

        #失效时间
        prontime_path ="form:nth-child(1)>div>div>div:nth-child(5)>div>div>div>input"
        prontime_text="2025-03-25"
        self.input("css",prontime_path,prontime_text)
        # 模拟鼠标点击其他任何一个地方来关闭日期框
        self.mouse_click()

        #适用地区列表
        area_path ="form:nth-child(1)>div>div>div:nth-child(6)>div>div>div:nth-child(1)>div>div.el-input.el-input--suffix>input"
        self.click("css",area_path)
        #js方式选择下拉框
        area_js="document.querySelector('body>div:nth-child(8)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span').click();"
        self.driver.execute_script(area_js)
        # 模拟鼠标点击其他任何一个地方来关闭日期框
        self.mouse_click()

        #业务平台
        bplatform_path ="form:nth-child(1)>div>div>div:nth-child(7)>div>div>div>div>div>input"
        self.click("css",bplatform_path)
        bplatform_js="document.querySelector('body>div:nth-child(9)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span').click();"
        self.driver.execute_script(bplatform_js)

        #推荐序号
        num_path="form:nth-child(1)>div>div>div:nth-child(8)>div>div>div>input"
        self.input("css",num_path,"8")

        #产品描述
        prodescrip_path="form:nth-child(1)>div>div>div:nth-child(9)>div>div>div>textarea"
        descrip_text="...产品描述..."+proname_text
        self.input("css",prodescrip_path,descrip_text)


        #适用渠道列表
        channel_path="form:nth-child(2)>div>div>div:nth-child(1)>div>div>div:nth-child(1)>div>div.el-input.el-input--suffix>input"
        self.click("css",channel_path)
        channelOTT_js="document.querySelector('body>div:nth-child(10)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span').click();"
        channelDPin_js = "document.querySelector('body>div:nth-child(10)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(2)>span').click();"
        self.driver.execute_script(channelOTT_js)
        self.driver.execute_script(channelDPin_js)
        #点击其他地方，收缩弹出框
        self.mouse_click()

        #支付方式
        paymode_path="form:nth-child(2)>div>div>div:nth-child(5)>div>div>div>div>div.el-input.el-input--suffix>input"
        self.click("css",paymode_path)
        telchargepay_js="document.querySelector('body>div:nth-child(11)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span').click();"
        disanfangpay_js = "document.querySelector('body>div:nth-child(11)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(2)>span').click();"
        self.driver.execute_script(telchargepay_js)
        self.driver.execute_script(disanfangpay_js)
        # 点击其他地方，收缩弹出框
        self.mouse_click()

        #提交,提交后有页面跳转时，需要等待个几秒钟让页面进行加载
        submit_path="div.small-main-router.fl>div.config-wrap>div>button:nth-child(2)"
        self.click("css",submit_path)
        time.sleep(1)

        #查询刚刚创建的产品
        exp_path="//div[3]/table/tbody/tr[1]/td[2]/div/div"
        exp_text=self.query_by_proname(proname_text,exp_path,"xpath")
        time.sleep(1)
        return exp_text

#创建一个【产品管理--内容包配置】类，
class ConBagConf(HomeMenu):
    def __init__(self):
        self.driver=globalvar.get_value('g_driver') #导入driver会话ID全局变量
        #同个产品管理下只需要点击一次【产品管理】，故本次内容包配置类不需要初始化点击【产品管理】
        #self.goto_promanage() #进入产品管理
    def __del__(self):
        pass

    # 点击内容包配置菜单项
    def click_conbagconf(self):
        path_conbagconf='/html/body/div[1]/div/div[2]/div[1]/ul/div/label[1]/li/ul/div/label[3]/li/span'
        self.click("xpath",path_conbagconf)

    # 模拟键盘鼠标点击某个元素触发其他弹出框消失
    def mouse_click(self):
        path_lable = "div.el-form-item:nth-child(2)>label:nth-child(1)"
        ele = self.locate_element("css", path_lable)
        ActionChains(self.driver).click(ele).perform()

    def cre_con_bag(self,conbagname):
        #点击新建按钮
        path_create='body>div:nth-child(1)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div:nth-child(1)>button'
        self.click("css",path_create)

        #内容包名称
        path_conbagname="form>div:nth-child(1)>div:nth-child(1)>div:nth-child(2)>div:nth-child(2)>div:nth-child(1)>input"
        self.input("css",path_conbagname,conbagname)

        #业务平台
        path_bplatform="div.el-form-item:nth-child(3)>div:nth-child(2)>div:nth-child(1)>div:nth-child(1)>input:nth-child(1)"
        self.click("css",path_bplatform)
        time.sleep(1)
        #选择业务平台下拉框js
        js_bplatform="document.querySelector('div.el-select-dropdown:nth-child(5)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span:nth-child(1)').click();"
        self.driver.execute_script(js_bplatform)

        #CP
        path_CP="div.el-input:nth-child(2)>input:nth-child(1)"
        self.click("css",path_CP)
        #选择CP下拉框js
        js_CP="document.querySelector('div.el-select-dropdown:nth-child(6)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span:nth-child(1)').click();"
        self.driver.execute_script(js_CP)
        self.mouse_click()

        #描述
        path_descripthion="div.el-textarea.el-input--small.el-input--suffix>textarea"
        text_descripthion="...描述..."+conbagname
        self.input("css",path_descripthion,text_descripthion)

        #选择产品
        path_selpro="div:nth-child(7)>div>div>button>span"
        self.click("css",path_selpro)
        #勾选前面2个产品
        path1_pro="//div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span"
        path2_pro="//div/div[3]/table/tbody/tr[2]/td[1]/div/label/span/span"
        self.click("xpath",path1_pro)
        self.click("xpath",path2_pro)
        #勾选完点击确定按钮
        path_confirm="div>button.el-button.search.el-button--primary.el-button--small>span"
        self.click("css",path_confirm)

        #提交
        path_submit="div.clearfix.button-group>button:nth-child(2)>span"
        self.click("css",path_submit)

        #获取创建后的内容包名称
        path_querybagname='//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/div'
        bag_name=self.get_text("xpath",path_querybagname)
        time.sleep(1)
        return bag_name






















