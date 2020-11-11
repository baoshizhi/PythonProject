#encoding=utf-8
import unittest
#创建一个继承于unittest.TestCase类的测试类TC01
class TC01(unittest.TestCase):
    def setUp(self):
        print("start")
    def tearDown(self):
        print("end")

    def test_01(self):
       self.assertEqual("1","1","不相等")
    #判断实际值【2】是否与预期值【1】相等，如果不等，抛出自定义的异常信息
    #assertEqual(预期值,实际值,不相等时的自定义异常信息")
    def test_02(self):
        self.assertEqual("1","2","实际值与预期值不相等")
    def test_03(self):
        print("---test_03----")
if __name__ == '__main__':
    unittest.main()