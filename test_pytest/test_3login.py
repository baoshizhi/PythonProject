from business.login_out import Login_Out
import allure
import pytest
'''
引用allure模块主要是为了使用pytest命令生成支持第三方工具allure能够解析的报告
并打开该报告时能够定制化输出注释内容，方便查看报告具体情况
@allure.feature():标注主要功能模块
@allure.story():标注feature功能模块下的分支功能
@allure.title():标注story下测试用例名称
@allure.step():标注测试用例的重要步骤
@allure.description(): 标注测试用例的描述
@allure.severity():标注测试用例的重要级别
(1)Blocker级别——中断缺陷
    客户端程序无响应，无法执行下一步操作。
(2)Critical级别――临界缺陷，包括：
    功能点缺失，客户端爆页。
(3)Normal级别――普通缺陷，包括：
    1)数值计算错误
    2)JavaScript错误。
(4)Minor级别———次要缺陷，包括：
    1)界面错误与UI需求不符。
    2)打印内容、格式错误
    3)程序不健壮，操作未给出明确提示。
(5)Trivial级别——轻微缺陷，包括：
    1)辅助说明描述不清楚
    2)显示格式不规范，数字，日期等格式。
    3)长时间操作未给用户进度提示
    4)提示窗口文字未采用行业术语
    5)可输入区域和只读区域没有明显的区分标志
    6)必输项无提示，或者提示不规范。

'''
'一级标签'
@allure.feature('登陆验证')
#创建一个测试类Test_login
class Test_login:
    #实例化一个登陆类Login
    LG=Login_Out()

    '''验证正常登陆教育计费平台首页'''
    #@allure.story('第1个二级标签')
    @allure.title('正常登陆教育计费平台首页')
    #@allure.step('调用登陆函数登陆')
    @allure.description('正常登陆:测试用例描述')
    @allure.severity(allure.severity_level.NORMAL)
    #@allure.attach('错误截图')
    #@pytest.mark.run(order=1) #在所有的测试用例中设定第1个执行登录函数
    def test_login_user_pwd(self):
        '''调用登陆类中的登陆函数进行登陆首页'''
        self.LG.login("baoshizhi2","123qweQWE+")

        '''获取登陆后页面右上角显示的账号'''
        account=self.LG.get_text("css","div.nl-header.clearfix>ul>li:nth-child(5)>span")
        print("登陆成功后的用户名为:",account)
        '''断言'''
        assert account=="baoshizhi2","未登陆成功"

        '''退出浏览器'''
        self.LG.web_quit()


    '''测试完成强制关闭浏览器'''
    # @allure.story('第1个二级标签')
    @allure.title('测试完成强制关闭浏览器')
    @allure.description('测试完成强制关闭浏览器')
    @allure.severity(allure.severity_level.NORMAL)
    #@allure.attach('错误截图')
    @pytest.mark.last  #在所有的测试用例中设定最后1个执行该测试用例进行退出浏览器器
    def test_logout(self):
        '''退出浏览器'''
        self.LG.web_quit()


    '''验证正确用户名--错误密码登陆'''
    # @allure.story('第2个二级标签')
    @allure.title('错误密码登陆教育计费平台首页')
    @allure.description('错误密码登陆描述')
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_user_cpwd(self):
        self.LG.login("baoshizhi", "1232ADE")
        '''获取报错提示'''
        text=self.LG.get_text("css", "div.el-message-box__message>p")
        print('报错提示:', text)
        '''断言'''
        assert "用户密码输入错误" in text, "没能看到预期错误提示"
        '''退出浏览器'''
        self.LG.web_quit()

    '''验证空用户名'''
    #@allure.story('第3个二级标签')
    @allure.title('空用户名登陆教育计费平台首页')
    @allure.description('不输入用户名直接点击登陆按钮')
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_user_no(self):
        self.LG.login("","JJDK")
        '''获取用户名为空提示'''
        text=self.LG.get_text("css","div:nth-child(1)>div>div.el-form-item__error")

        print("用户名为空提示：",text)

        '''断言'''
        assert text=="请输入用户名称","用户名为空提示与预期不一致"

        '''退出浏览器'''
        self.LG.web_quit()


    '''验证空密码'''
    #@allure.story('第4个二级标签')
    @allure.title('空密码登陆教育计费平台首页')
    @allure.description('不输入密码直接点击登陆按钮')
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_pwd_no(self):
        self.LG.login("jkkkd","")
        '''获取密码为空提示'''
        text=self.LG.get_text("css","div:nth-child(2)>div>div.el-form-item__error")
        print("密码为空提示:",text)

        '''断言'''
        assert text=="请输入用户密码","密码为空提示与预期不一样"
        '''退出浏览器'''
        self.LG.web_quit()













