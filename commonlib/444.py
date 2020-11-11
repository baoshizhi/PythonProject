import xlwt
import xlrd
from xlutils.copy import copy

excel_path="D:\PythonProject\data_excel\五中心.xls"
row_i=3
col_j=13
text="你好我的中国"
def write_excel(excel_path,row_i,col_j,text):
    # 打开想要更改的excel文件
    old_excel=xlrd.open_workbook(excel_path,formatting_info=True)
    # 将操作文件对象拷贝，变成可写的workbook对象
    new_excel=copy(old_excel)
    # 获得第一个sheet的对象
    new_sheet=new_excel.get_sheet(0)

    #预定一个字体相关的格式对象style
    style=xlwt.XFStyle()
    #字体参数相关配置
    font=xlwt.Font()
    font.name="Microsoft YaHei UI"
    font.bold = False #是否加粗，True为加粗
    font.height = 250 #  如果是200对应的是10号字体
    style.font = font
    #边框
    borders=xlwt.Borders()
    borders.top=xlwt.Borders.THIN
    borders.bottom=xlwt.Borders.THIN
    borders.left=xlwt.Borders.THIN
    borders.right=xlwt.Borders.THIN
    style.borders=borders
    #写入数据
    new_sheet.write(row_i-1, col_j-1,text,style)
    #另存为excel文件，并将文件命名如果与原来文件重名则修改原文件
    new_excel.save(excel_path)

write_excel(excel_path,row_i,col_j,text)


# import urllib.request
# import urllib.error
# import time
# #url="http://10.45.138.39:8380/bac-ia-account-microservice/account-relation/queryGroupAccountingRelationInfo"
# url="https://www.cnblogs.com/mcq1999/p/python_Crawler_1.html"
# class PortOperation:
#     def __init__(self):
#         print("----init----")
#     def __del__(self):
#         print("----del-----")
#     #捕获请求异常有正确返回后，再进行后续操作
#     def request_error(self,url):
#         request_status=""
#         for i in range(3):
#             try:
#                 #urllib.request.urlopen("https://www.cnblogs.com/mcq1999/p/python_Crawler_1.html")
#                 urllib.request.urlopen(url)
#                 request_status="OK"
#                 time.sleep(3)
#             except urllib.error.URLError as e:
#                 if hasattr(e, "code"):
#                     print(e.code)
#                 if hasattr(e, "reason"):
#                     print(e.reason)
#                 request_status="NO"
#         return request_status
#
#     def port_get(self,url):
#         if self.request_error(url)=="OK":
#             #发起get请求
#             print("发起get请求")
#
# PO=PortOperation()
# PO.port_get(url)
