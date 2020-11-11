from commonlib import globalvar #导入跨文件全局变量.py文件

class aa1:
    def fun1(self):
        globalvar._init()
        globalvar.set_value("name","baoshizhi")


a=aa1()
a.fun1()
print("1234")
# import re
#
# tagname_list=[[] for x in range(5)]
# tagname_list.append("232")
# print(tagname_list)

# tagname_list_tmp1=["123","675"]
# tagname_list_tmp2=[]
# tagname_list_tmp3=["777"]
# tagname_list=[]
# tag=[]
# print("--111--:",len(tagname_list))
#
# tagname_list.append(tagname_list_tmp1)
# tagname_list.append(tagname_list_tmp2)
# tagname_list.append(tagname_list_tmp3)
#
# for i in range(4,6):
#     tagname_list.append(tag)
#
# print("--222--:",len(tagname_list))
# print(tagname_list[3])


# s_text='"userType":"0","userId":1001"userName":"用户名""areaCode":"591"'
# tagname="areaCode"
#
# k=0
# j=0
# for i in range(len(s_text)):
#     if s_text[i]==":":
#         j=i-1 #:号往回第一个【"】的位置坐标
#         k=j
#         while True:
#             k= k-1
#             if(s_text[k])=='"': #:号往回第二个【"】的位置坐标
#                 break
#         print(s_text[k+1:j])
#
#
# def get_json_alltagnames(self,s_text):
#     if s_text is None:
#         print("\n入参源文件大小为空，请检查excel表格中检查点的字段\n")
#         return
#     else:
#         k = 0
#         j = 0
#         self.tagname_list=[]
#         for i in range(len(s_text)):
#             if s_text[i] == ":":
#                 j = i - 1  #:号往回第一个【"】的位置坐标
#                 k = j
#                 while True:
#                     k = k - 1
#                     if (s_text[k]) == '"':  #:号往回第二个【"】的位置坐标
#                         break
#                 tagname =s_text[k+1:j]  # 找到标签值
#                 self.tagname_list.append(tagname)  # 将找到标签值存储在list变量中
#         return self.tagname_list
#









# 返回json请求格式的数据当中指定的标签的值或对应的整个文本串
# 如s_text='{"userInfo":{"userType":"0","userId":1001,"userName":"用户名","areaCode":"591"}}'
#输入标签名userId 返回文本串 "userId": 1001
#输入标签名areaCode返回文本串 "areaCode": "591"
# def get_json_value(s_text, tagname):
#     if s_text is None:
#         print("\n入参源文件大小为空，有可能没有正确取到excel表格数据或者接口请求返回的数据为空请检查接口地址或环境是否有误\n")
#     else:
#         text = ""  # 目标节点文本初始化为空字符
#         for i in range(0,len(s_text)):
#             if s_text[i:i+len(tagname)]==tagname:
#                 j=i-1 #tagname标签前半部分的"所在的位置
#                 for i in range(j,len(s_text)):
#                     if s_text[i]=="," or s_text[i]=="}":
#                         k=i #tagname标签对应值的后一位字符所在的位置
#                         text=s_text[j:k]
#                         break
#                 break
#         print("标签对应的字符串为:\n",text)
#         if text == "":
#             print("\n未找到%s标签，请检查表格中预期校验单元格的标签，也可能接口返回为空或返回数据未包含该标签,!\n" % tagname)
#         else:
#             # print("目标节点文本内容:\n", text)
#             return text

#get_json_value(s_text,tagname)























#s_text="<resp_code>  10000017</resp_code><resp_result>1</resp_result><accept_id>300004650046</accept_id><customer_id>591102059455206</customer_id>"
#s_text="<nr>17</nr><sp>1</sp>"
#text=re.sub("\s","",s_text) #去除空白字符后的源文本
#print(len(s_text))





#
# k=0
# i=0
# j=0
# tagname_list=[]
# for i in range(0,len(text)):
#     if s_text[i:i+2]=="</":
#          j=i  #找到第一个“</”的位置
#          for i in range(j,len(s_text)):
#              if s_text[i]==">": #往后面找到紧挨着的“>”的位置
#                 k=i
#                 break
#          tagname=s_text[j+2:k]  #找到标签值
#          tagname_list.append(tagname) #将找到标签值存储在list变量中
#
# for i in range(0,len(tagname_list)):
#     print(tagname_list[i])
#
#
# str=[]
# print(len(str))
# print(str[0])
# #



