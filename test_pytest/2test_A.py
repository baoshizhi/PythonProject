import pytest
def test_fun05():
    print("---test_fun05--")

def test_fun01():
    print("---test_fun01--")

class Test_C:
    bb = "B1234"
    print("bb:",bb)


class Test_A:
    aa = "A1234"
    print("aa:",aa)



# from commonlib import globalvar #导入跨文件全局变量.py文件
# from commonlib.a1 import aa1
# class aa2:
#     def __init__(self):
#         name = globalvar.get_value("name")
#         print(name)
#
# aa=aa2()

# import xlrd
# import chardet
# import re
# book_excel = xlrd.open_workbook("D:\PythonProject\data_excel\五中心.xls")
# # 定位excel表中的某个sheet字表
# sheet_excel= book_excel.sheet_by_index(1)
# expect_text_tmp=sheet_excel.cell_value(2,11)
# expect_text=re.sub("\s", "", expect_text_tmp)
#
# format_stype1=chardet.detect(expect_text.encode())
# print("预期文本编码格式:",format_stype1)
# print("expect_text:\n\n",expect_text)
#
# actual_text_tmp=sheet_excel.cell_value(2,14)
# actual_text=re.sub("\s", "", actual_text_tmp)
# format_stype2=chardet.detect(actual_text.encode())
# print("接口返回的文本编码格式:",format_stype2)
# print("actual_text:\n\n",actual_text)
# if expect_text==actual_text:
#     print("相等")
# else:
#     print("不相等")
#
# format()


# #print("text_temp_1:---",text_temp_1)
# #匹配http开头直到文本结束的文本(list变量类型)，本身不包含http字符，通过(变量名[下标值])取值
# text_temp_2= re.findall("http(.+?)$",text_temp_1)
# #print("text_tmp_2:----",text_temp_2)
# #往缺少http字符开头的字符串补添加http字符
# text_temp="http"+text_temp_2[0]  #list变量类型 通过下标值取值【数字】取值