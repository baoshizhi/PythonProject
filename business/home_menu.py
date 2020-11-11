from business.login_out import *

#创建一个基于登陆类Login的【主页面功能类】，以每一个具体类别测试功能类为单位，登陆/退出一次系统
#用于进入到当前主页面下的各个功能菜单
class HomeMenu(Login_Out):
    def goto_promanage(self): #进入到产品管理功能菜单
        # 点击【产品管理】
        path_promanage = '/html/body/div/div/div[2]/div[1]/ul/div/label[1]/li/div/span'
        self.click('xpath', path_promanage)


    def goto_marketmanage(self):#进入到营销管理功能菜单
        #点击【营销管理】
        path_marketmanage='/html/body/div/div/div[2]/div[1]/ul/div/label[2]/li/div/span'
        self.click("xpath",path_marketmanage)


