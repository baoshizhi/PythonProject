import unittest
import  HTMLTestRunner
from testunittest.testcase import TestC

#创建测试套件类
class TestS(unittest.TestCase):
    def setUp(self):
        print("---TestS:start---")
    def tearDown(self):
        print("---TestS:end-----")
    def test_suit(self):
        #创建测试套件
        mysuit=unittest.TestSuite()
        #添加测试用例列表
        case_list=["test_normal_login","test_name_cpwd","test_name_cpwd_no"]
        #向测试套件循环添加测试用例列表当中的测试用例
        for case in case_list:
            mysuit.addTest(TestC(case))

        #通过runner执行测试用例
        #执行测试套件(测试用例集) verbosity=2表示为每个测试用例输出测试报告，run的参数是测试套件suit
        #unittest.TextTestRunner(verbosity=2).run(mysuit)

        #定义报告存放路径及报告文件名
        report_path="../Report/scs_login.html"
        #以读写方式打开报告
        fp=open(report_path,"wb")
        #定义测试报告的相关参数
        #stream测试数据写入的文件，title报告标题，description报告描述，verbosity=2表示为每个测试用例输出测试报告
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title="scs登陆测试报告",description="第一轮测试",verbosity=2)
        #执行测试用例
        runner.run(mysuit)
        #关闭报告文件
        fp.close()

if __name__ == '__main__':
    unittest.main()
