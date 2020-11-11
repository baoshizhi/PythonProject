from business import login_out
import  unittest

#创建继承于unittest.TestCase类的测试类

class TestC(unittest.TestCase):
    def setUp(self):
        print("---start---")
    def tearDown(self):
        print("---end-----")

    #验证正常登陆
    def test_normal_login(self):
        #实例化login.py文件中的一个登陆类Login
        logi= login_out.Login()
        #调用类中登陆函数login函数进行正确登陆网站
        logi.login("bsz01","root1234")
        #获取登陆后的断言结果存放于变量data
        data=logi.get_text("xpath","//*[@id= 'navbar-container']/div[2]/ul/li[1]/a")
        print("相关函数test_normal_login登陆后的用户名:",data)

        #断言是否成功登陆,预期值在前，实际值在后
        self.assertEqual("1李连杰",data)

    #验证账号正确，密码错误的登陆情况
    def test_name_cpwd(self):
        # 实例化login.py文件中的一个登陆类Login
        logi = login_out.Login()
        # 调用类中登陆函数login函数进行登陆
        logi.login("bsz01", "root123")
        # 获取断言结果存放于变量data
        data = logi.get_text("xpath", "//*[@id='login-error']/span")
        print("相关函数test_name_cpwd报错提示:", data)
        # 断言是否按预期正常报错,预期值在前，实际值在后
        self.assertEqual("用户名或密码错误",data)
        # 验证账号正确，密码错误的登陆情况

    # 验证账号正确，密码错误的登陆情况(人为设置预期值为异常)
    def test_name_cpwd_no(self):
        # 实例化login.py文件中的一个登陆类Login
        logi = login_out.Login()
        # 调用类中登陆函数login函数进行登陆
        logi.login("bsz01", "root123")
        # 获取断言结果存放于变量data
        data = logi.get_text("xpath", "//*[@id='login-error']/span")
        print("相关函数test_name_cpwd_no报错提示:", data)
        # 断言是否按预期正常报错,预期值在前，实际值在后
        self.assertEqual("用户名或密码错误1", data)

if __name__ == '__main__':
    unittest.main()




