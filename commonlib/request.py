#encoding=utf-8
import requests
import  re
import urllib
import urllib.error
import socket
import time
import json
from commonlib.readwrite_excel import ReadWriteExcel
class PortOperation:
    def __init__(self):
        print("----init----")
    def __del__(self):
        print("----del-----")

    '''
    1)捕获请求异常有正确返回后，再进行后续操作
    2)url:请求链接地址   request_data:请求体数据
    '''
    def request_error(self,url,request_data):
        response_data=""
        error_code=""
        error_text=""
        #url[0:5] 值取到0-4
        if url[0:5]=="http:" or url[0:6]=="https:":
            #socket.setdefaulttimeout(3)
            try:
                # urllib.request.urlopen("https://www.cnblogs.com/mcq1999/p/python_Crawler_1.html")
                # request_data入参必须为utf-8类型的数据，超时时间设为5，超过5秒后未返回则报错(设少了有可能还会报错)
                urllib.request.urlopen(url,request_data,timeout=5)
                #无论中英文，urlopen中的请求体数据只支持utf-8字节流数据
                response_data="OK"
            except socket.timeout: #接收数据时传输虽然超时，但实际任可接收到数据到完毕，response_data值依然可设为"OK"
                response_data="OK"
                time.sleep(2)
            except urllib.error.URLError as e:  #捕捉错误时有可能只有出错原因，没有出错代码
                if hasattr(e, "code"):
                    error_code=str(e.code)  #转换成字符型
                    #print(e.code)
                if hasattr(e, "reason"):
                    error_text=str(e.reason) #转换成字符型
                    #print(e.reason)
                if error_code!="":
                    response_data ="错误代码:"+error_code+"  错误原因:"+error_text
                else:
                    response_data = "错误原因:" + error_text
            except urllib.error.HTTPError as er:
                if hasattr(er, "code"):
                    error_code=str(er.code)
                    #print(er.code)
                if hasattr(er, "reason"):
                    error_text=str(er.reason)
                    #print(er.reason)
                if error_code!="":
                    response_data ="错误代码:"+error_code+"  错误原因:"+error_text
                else:
                    response_data = "错误原因:" + error_text
        else:
            response_data = "没有获取到正确的请求url地址，请核对url地址在表格当中的行号列号入参"
            #print("没有获取到正确的请求url地址，请核对url地址在表格当中的行号列号入参")
        #print("response_data:",response_data)
        return response_data


    #返回http请求数据
    #url为请求链接地址，para为请求体数据，request_type为请求类型 post或者get,接口返回初始数据
    def get_response(self,url, para,request_type):
        head=""
        if para[0:5]=="<?xml":#设置xml请求头，
            head={'Content-Type': 'application/xml;charset=UTF-8'}
        elif para[0] == "{":#设置json请求头，
            head = {'Content-Type': 'application/json;charset=UTF-8'}

        #调用request_error函数，捕捉request请求异常，符合条件发起post或者get请求
        para_utf8=para.encode("utf-8") #防止调用系统函数urllib.request.urlopen请求体数据中出现非utf-8格式的中文时发生报错
        self.responsedata = self.request_error(url, para_utf8)
        if self.responsedata == "OK":
            json_data = None
            text_data = None
            if request_type=="post"or request_type=="POST" or request_type=="Post":
                # 发起post请求
                self.res_data=requests.post(url,data=para_utf8,headers=head) #数据必须为utf-8类型时，请求体出现中文时才不会报错
            elif request_type=="get"or request_type=="GET"or request_type=="Get" :
                #发起get请求
                self.res_data = requests.get(url,params=para,headers=head)#请求体数据中若出现utf-8类型的中文会报错，不支持utf-8中文
            else:
                self.res_data="不支持post/get以外的其他http请求方式"
                return self.res_data
            # 获取完整的返回包的text数据(json与xml格式的均属于text数据)
            print("response_status_code:",self.res_data.status_code)
            if self.res_data.status_code!=404:#正常的状态码为200  如果是404下面语句会报错
                responsedata= self.res_data.text
            else:
                responsedata="python内置requests函数返回的状态码为:"+str(self.res_data.status_code)+",请用postman工具重试一下"
            #print("请求返回的初始数据:responsedata:\n",responsedata)
            return responsedata
        else:
            return self.responsedata

    #去除空白字符
    def get_del_blank(self,s_text):
        if s_text==None or s_text=="":
            print("待去除空白字符的入参文本为空，请确认")
            return
        else:
            text=re.sub("\s","",s_text)
            return text
