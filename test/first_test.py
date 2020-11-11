#encoding=utf-8
from selenium import webdriver
import time

import sys
sys.path.append("../commonlib")
from commonlib import  commonfun

import unittest

class TC01(unittest.TestCase):
    def setUp(self):
        print("101-hello")
    def test_101(self):
        print("---101---")
    def test_102(self):
        print("---102---")
    def test_103(self):
        print("---103---")
    def tearDown(self):
        print("101-bye")

class TC02(unittest.TestCase):
    def setUp(self):
        print("201--hello")
    def test_201(self):
        print("---201---")
    def test_202(self):
        print("---202---")
    def test_203(self):
        print("---203---")
    def tearDown(self):
        print("201--bye")
print("----2222-----")
print("name:",__name__)
print("\n")

if __name__ == '__main__':
    print("---1111111----")
    unittest.main()
    # # unittest.main()运行时自动寻找TestCase子类，并运行
    # # 在TestCase子类中只执行以test开头的方法
    # # setUp()用于初始化一些参数，在测试用例执行前自动被调用，tearDown()用于在测试用例执行后自动被调用。
    #
    # #1.创建测试套件(测试用例集)
    # suit=unittest.TestSuite()
    # #2.定义一个需要加载测试的目标测试用例列表
    # case_list01=["test_101","test_102"]
    # case_list02=["test_201","test_202"]
    # #3.向测试套件(测试用例集)循环添加待测试的测试用例testcase， 类名(类中test_开头的方法)
    # for case in case_list01:
    #     suit.addTest(TC01(case))
    # for case in case_list02:
    #     suit.addTest(TC02(case))
    # #suit.addTest(test_9002)
    # #4.执行测试套件(测试用例集) verbosity=2表示为每个测试用例输出测试报告，run的参数是测试套件suit
    # unittest.TextTestRunner(verbosity=2).run(suit)
    print(__name__)





