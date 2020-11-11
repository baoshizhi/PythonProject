from business.market_manage import *
import allure
import pytest


#创建一个【营销案管理】测试类Test_MarketCaseManage
@allure.feature('营销案管理')  # html测试报告一级展示标签
class Test_MarketCaseManage:
    # 实例化一个营销案管理测试类
    MCM=MarketCaseManage()

    #@allure注释必须紧挨着放在测试函数之前
    @allure.title('创建营销案')  # html测试报告二级展示标签
    @allure.description('创建一个营销案')
    def testcremarketcase(self):
        self.MCM.goto_marketmanage()#点击营销管理菜单项(放在第1个测试函数内执行)
        self.MCM.click_marketcase() #点击营销案管理菜单项(放在第1个测试函数内执行)
        marketcasename="营销案bsz070"
        casename=self.MCM.cre_marketcase(marketcasename)

        #断言
        assert casename==marketcasename,"创建营销案失败"


