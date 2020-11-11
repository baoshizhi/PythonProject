#encoding=utf-8
import unittest
from commonlib.request import PortOperation

class Test_Port(unittest.TestCase):
    def setUp(self):
        print("---start---")
    def tearDown(self):
        print("---stop----")
    def test_para_get(self):
        #实例化接口测试Interface_Port类
        interfaceport=PortOperation()

        #自定义接口测试类的各个入参参数，resp_data_type为接口返回的数据类型，分json和text两种类型
        resp_data_type="json"
        url="http://192.168.65.111:7000/api/v1/sysconf"
        para=None
        #调用类中port_para_get函数发起get请求，将获取的数据存入数组变量resp_data
        resp_data=interfaceport.port_para_get(resp_data_type,url,para)
        #打印返回的接口数据
        print("返回的get请求接口数据：\n",resp_data)
        # 获取返回json串中某个字段的值,resp_data[子一级][子二级][子三级]
        bs3 = resp_data["bs3url"]
        print("bs3_url:", resp_data["bs3url"])
        self.assertEqual("http://192.168.66.204:8080",bs3)


    def test_para_post(self):
        # 实例化接口测试Interface_Port类
        interfaceport=PortOperation()
        resp_data_type="json"
        url="http://192.168.65.111:7000/api/v1/user/me"
        para={"name":"bsz01","password":"U2FsdGVkX1/Gpe80bPelG5aUw5gAKkfTYaHHvrHaIro="}
        resp_data=interfaceport.port_para_post(resp_data_type,url,para)
        print("返回的post请求接口数据\n",resp_data)
        # 打印返回的json数据串中指定的字段值
        resp_fname = resp_data["fname"]
        print("返回的姓名:\n",resp_fname)
        self.assertEqual("1李连杰22",resp_fname)

if __name__ == '__main__':
    unittest.main()

