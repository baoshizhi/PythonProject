from business.product_manage import *
import allure
import pytest

#创建一个【内容型产品配置】测试类Test_ConProConf
@allure.feature('内容型产品配置')  #html测试报告一级展示标签
class Test_ConProConf:
    #实例化一个内容型产品配置类
    CPC=ConProConf()

    #@allure注释必须紧挨着放在测试函数之前
    @allure.story('产品查询')  # html测试报告二级展示标签
    @allure.title('按正常ID查询产品')
    @allure.description('输入产品ID:1585793476174正常查询')
    def testqueryby_id_normal(self):
        self.CPC.goto_promanage()  # 调用父类方法进入到【产品管理】功能菜单(放在第一个测试函数内)
        self.CPC.click_conproconf()  # 点击内容型产品配置菜单(放在第一个测试函数内)

        #输入产品ID点击查询
        pro_id="1585793476174"
        # 预期文本元素路径
        exp_path='//div[3]/table/tbody/tr/td[1]/div/div'
        #获取查询结果页面中的产品ID信息文本
        exp_text=self.CPC.query_by_id(pro_id,exp_path,"xpath")
        #断言
        assert exp_text==pro_id,"没查到指定的产品ID"
        # #关闭内容型产品配置菜单
        # self.CPC.close_conproconf()


    @allure.story('产品查询')
    @allure.title('根据不足位数的ID号查询产品')
    @allure.description('输入不足位数的产品ID号:1600001进行查询')
    def testqueryby_id_nonid(self):
        # 输入产品ID点击查询
        pro_id = "1600001"

        # 预期文本元素路径
        exp_path = 'div.el-table__body-wrapper.is-scrolling-left>div>span'

        # 获取查询结果页面中的产品ID信息文本
        exp_text = self.CPC.query_by_id(pro_id,exp_path,"css")
        # 断言
        assert exp_text=="暂无数据","产品不存在时界面提示与预期不一致"

    @allure.story('产品查询')
    @allure.title('根据错误的ID号查询产品')
    @allure.description('输入错误的产品ID号:1600011597进行查询')
    def testqueryby_id_noid(self):
        # 输入产品ID点击查询
        pro_id = "1600011597"

        # 预期文本元素路径
        exp_path = 'div.el-table__body-wrapper.is-scrolling-left>div>span'

        # 获取查询结果页面中的产品ID信息文本
        exp_text = self.CPC.query_by_id(pro_id,exp_path,"css")
        # 断言
        assert exp_text == "暂无数据", "产品不存在时界面提示与预期不一致"

    @allure.story('产品查询')
    @allure.title('按条件【单次点播】进行查询')
    @allure.description('查询条件选择【单次点播】进行查询')
    def testqueryby_protype_dcdb(self):
        #有些input类型的下拉框点击下拉框元素时无效,可以用js方法进行点击，先找到目标元素的类名,有可能多个，通过下标值取得准确类名
        #利用[js]方法嵌入点击【单次点播】
        protype_js="document.querySelector('body>div:nth-child(5)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span').click();"

        #调用按产品类型查询函数query_by_protype进行查询，获取预期返回结果
        exp_text=self.CPC.query_by_protype(protype_js)

        #断言
        assert exp_text=="单次点播","无单次点播产品或者单次点播查询条件没有生效"


    @allure.story('产品查询')
    @allure.title('按条件【连续性包月】进行查询')
    @allure.description('查询条件选择【连续性包月】进行查询')
    def testqueryby_protype_lxby(self):
        # 有些input类型的下拉框点击下拉框元素时无效,可以用js方法进行点击，先找到目标元素的类名,有可能多个，通过下标值取得准确类名
        # 利用[js]方法嵌入点击【连续性包月】
        protype_js = "document.querySelector('body>div:nth-child(5)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(2)>span').click();"

        # 调用按产品类型查询函数query_by_protype进行查询，获取预期返回结果
        exp_text = self.CPC.query_by_protype(protype_js)

        # 断言
        assert exp_text == "连续性包月", "无连续性包月产品或者连续性包月查询条件没有生效"


    @allure.story('产品查询')
    @allure.title('按条件【按时长订购】进行查询')
    @allure.description('查询条件选择【按时长订购】进行查询')
    def testqueryby_protype_ascdg(self):
        # 有些input类型的下拉框点击下拉框元素时无效,可以用js方法进行点击，先找到目标元素的类名,有可能多个，通过下标值取得准确类名
        # 利用[js]方法嵌入点击【按时长订购】
        protype_js = "document.querySelector('div:nth-child(5)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(3)>span').click();"

        #调用按产品类型查询函数query_by_protype进行查询，获取预期返回结果
        exp_text = self.CPC.query_by_protype(protype_js)

        #断言
        assert exp_text == "按时长订购", "无按时长订购产品或者按时长订购查询条件没有生效"


    @allure.story('产品查询')
    @allure.title('按条件【周末包】进行查询')
    @allure.description('查询条件选择【周末包】进行查询')
    def testqueryby_protype_zmb(self):
        #有些input类型的下拉框点击下拉框元素时无效,可以用js方法进行点击，先找到目标元素的类名,有可能多个，通过下标值取得准确类名
        #利用[js]方法嵌入点击【周末包】
        protype_js = "document.querySelector('body>div:nth-child(5)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(4)>span').click();"

        #调用按产品类型查询函数query_by_protype进行查询，获取预期返回结果
        exp_text = self.CPC.query_by_protype(protype_js)

        #断言
        assert exp_text == "周末包", "无周末包产品或者按周末包查询条件没有生效"

    @allure.story('产品查询')
    @allure.title('按条件【产品状态】进行查询')
    @allure.description('查询条件选择【正常】进行查询')
    def testqueryby_prostatus_normal(self):
        #点击产品状态相关的js文本
        prostus_js = "document.querySelector('body>div:nth-child(6)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(1)>span').click();"
        #获取预期返回结果(查询页面中第一行数据【产品状态】字段的值)
        exp_text=self.CPC.query_by_prostatus(prostus_js)


        #断言
        assert exp_text=="正常","无正常状态的产品或者查询条件没有生效"


    @allure.story('产品查询')
    @allure.title('按条件【产品状态】进行查询')
    @allure.description('查询条件选择【暂停】进行查询')
    def testqueryby_prostatus_pause(self):
        #点击产品状态相关的js文本
        prostus_js = "document.querySelector('body>div:nth-child(6)>div:nth-child(1)>div:nth-child(1)>ul:nth-child(1)>li:nth-child(2)>span').click();"
        #获取预期返回结果(查询页面中第一行数据【产品状态】字段的值)
        exp_text=self.CPC.query_by_prostatus(prostus_js)

        #断言
        assert exp_text=="暂停","无暂停状态的产品或者查询条件没有生效"


    @allure.story('创建内容型产品')
    @allure.title('创建单次点播产品')
    @allure.description('创建单次点播产品')
    def testcrepro_dcdb(self):
        #单次点播产品名称
        proname_text="单次点播产品bsz102"
        exp_text=self.CPC.cre_pro_dcdb(proname_text)
        #断言
        assert exp_text==proname_text,"创建失败"


#创建一个【内容型产品配置】测试类Test_ConProConf
@allure.feature('内容包配置')  #html测试报告一级展示标签
class Test_ConBagConf():
    #实例化一个内容包配置类
    CBC=ConBagConf()

    @allure.title('创建内容包')
    @allure.description('创建一个内容包')
    def testcreconbag(self):
        self.CBC.click_conbagconf() #点击内容包配置菜单项
        conbagname="内容包bsz068"
        bagname=self.CBC.cre_con_bag(conbagname)

        #断言
        assert bagname==conbagname,"创建内容包失败"





