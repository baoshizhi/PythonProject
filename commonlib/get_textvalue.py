#encoding=utf-8
import re
'''
   def get_xml_value(self,s_text, tagname)
   1)返回XML格式的数据当中指定的标签对应的整个文本串
   2)s_text="12345<accept_id name="bsz">201312096911</accept_id><request_time>20171222111519</request_time>456"
   3)如输入参数为tagname="accept_id", 返回<accept_id name="bsz">201312096911</accept_id>

  def get_json_value(self,s_text, tagname):
   1)返回json请求格式的数据当中指定的标签的值或对应的整个文本串
   2)如s_text='{"userInfo":{"userType":"0","userId":1001,"userName":"用户名","areaCode":"591"}}'
   3)输入标签名userId 返回文本串 "userId": 1001
   4)输入标签名areaCode返回文本串 "areaCode": "591"
    
    
    def get_xml_alltagnames(self,s_text):
    1)获取excel表格检查点单元格内的所有标签名并存储在list变量tagname_list中
    2)s_text="<resp_code>  10000017</resp_code><resp_result>1</resp_result><accept_id>300004650046</accept_id><customer_id>591102059455206</customer_id>"
    3)返回标签名称列表
      tagname_list=["resp_code","resp_result","accept_id","customer_id"]
    
    def get_json_alltagnames(self,s_text):
           1)获取excel表格检查点单元格内的所有标签名并存储在list变量tagname_list中
           2)s_text='"userType":"0","userId":1001,"userName":"用户名","areaCode":"591"'
           3)返回标签名称列表
             tagname_list=["userType","userId","userName","areaCode"]
             
    def del_tagnames(self, s_text, tagname_list=None)
        1)根据不同文本类型(XML/json）去除不需要对比的节点之间的内容
        2)tagname_list为list变量，默认为空，为空时，文本不做任何处理直接返回
        3)如tagname_list=["userid","username","sex"]
           为xml格式：则去除<userid>XXXXXXXX</userid>
                            <username>XXXXXXXX</username>
                            <sex>XXXXXXXXXXXXX</sex>
           为json格式：则去除"userid":XXXXX
                             "username":"XXXXX"
                             "sex":"M"
 
    def get_check_text(self,expect_text,response_text): 从接口返回的数据中提取待校验的文本串
    1)如果excel表格预期文本的数据是部分待校验的标签，则根据此标签从接口返回的数据中提取出需要校验的字符串文本，
      如excel表格中的预期XML校验文本为
       expect_check_text="<accept_city>591</accept_city><accept_org_id>314</accept_org_id>"
       则从接口返回的数据中提取与以上相同格式的文本为：
       actual_check_text="<accept_city>592</accept_city><accept_org_id>315</accept_org_id>"   
    2)如果excel表格预期文本的数据是完整的XML或者json文本，则调用去除指定标签字符串函数再返回数据
      del_tagname_list为list变量，为空表示文本不做去除指定标签关联字符串处理，不为空去除指定关联字符串
       如tagname_list=["userid","username","sex"]
           为xml格式：则在接口返回的数据中去除<userid>XXXXXXXX</userid>
                            <username>XXXXXXXX</username>
                            <sex>XXXXXXXXXXXXX</sex>
           为json格式：则在接口返回的数据中去除"userid":XXXXX
                             "username":"XXXXX"
                             "sex":"M"                              
    3)完整的XML文本：以<?xml version="1.0" encoding="GBK"?>开头
      完整的json文本：以{开头    
'''
class GetTextValue:
    def __init__(self):
        pass
    def __del__(self):
        pass

    '''返回XML格式的数据当中指定的标签对应的整个文本串'''
    def get_xml_value(self,s_text,tagname):
        if s_text is None:
            print("\n入参源文件大小为空，有可能没有正确取到excel表格数据或者接口请求返回的数据为空请检查接口地址或环境是否有误\n")
        else:
            n1 = len(s_text)  # print("源文本大小:", n1)
            tagnamehead01 = "<" + tagname  # print("tagnamehead01:", tagnamehead02)
            tagnamehead02 = ">"
            tagnametail = "</" + tagname + ">"  # print("tagnametail:", tagnametail)
            n2 = len(tagnamehead01)  # print("tagnamehead大小:", n2)
            n3 = len(tagnamehead02)  # print("tagnametail大小:", n3)
            n4 = len(tagnametail)  # print("tagnametail大小:", n3)
            text = ""  # 目标节点文本初始化为空字符
            value = ""  # 目标节点的取值初始化为空字符
            head_i01 = 0  # 目标tagnamehead字符标签头【<response_time】第一次出现的位置初始化为0
            head_i02 = 0  # 紧跟目标tagnamehead字符串之后的第一次出现闭合字符">"的位置初始化为0
            tail_i = 0  # 目标tagnametail字符串第一次出现的位置初始化为0
            for i in range(n1 - 1):
                if s_text[i:i + n2] == tagnamehead01:
                    # 第一次出现tagname字符串标签头【<response_time】部分的位置
                    head_i01 = i
                    while True:
                        i = i + 1
                        if s_text[i] == ">":  # 获取tagname标签头的闭合字符[>]在整个字符串中的位置
                            head_i02 = i
                            break
                elif s_text[i:i + n4] == tagnametail:
                    tail_i = i  # print("tail_i:", tail_i) #获取tagname尾部标签在整个字符串中的位置 </response_time>
                    text = s_text[head_i01:tail_i + n4]  # 截取目标节点文本内容text
                    value = s_text[head_i02 + 1:tail_i]  # 截取目标节点间的value值
                    break
            if text == "":
                print("\n未找到%s标签，请检查表格中预期校验单元格的标签，也可能接口返回为空或返回数据未包含该标签,!\n"%tagname)
                return
            else:
                #print("目标节点文本内容:\n", text)
                return text


    '''返回json请求格式的数据当中指定的标签的值或对应的整个文本串'''
    def get_json_value(self,s_text, tagname):
        if s_text is None:
            print("\n入参源文件大小为空，有可能没有正确取到excel表格数据或者接口请求返回的数据为空请检查接口地址或环境是否有误\n")
        else:
            text = ""  # 目标节点文本初始化为空字符
            for i in range(0, len(s_text)):
                if s_text[i:i + len(tagname)] == tagname:
                    j = i - 1  # tagname标签前半部分的"所在的位置
                    for i in range(j, len(s_text)):
                        if s_text[i] == "," or s_text[i] == "}":
                            k = i  # tagname标签对应值的后一位字符所在的位置
                            text = s_text[j:k]
                            break
                    break
            print("标签对应的字符串为:\n", text)
            if text == "":
                print("\n未找到%s标签，请检查表格中预期校验单元格的标签，也可能接口返回为空或返回数据未包含该标签,!\n" % tagname)
            else:
                # print("目标节点文本内容:\n", text)
                return text


    '''获取excel表格检查点单元格内的【xml类型】所有标签名并存储在list变量tagname_list中'''
    def get_xml_alltagnames(self,s_text):
        if s_text is None:
            print("\n入参源文件大小为空，请检查excel表格中检查点的字段\n")
            return
        else:
            k = 0
            i = 0
            j = 0
            self.tagname_list = []
            text=re.sub("\s","",s_text)  #去除空白字符
            for i in range(0, len(text)):
                if s_text[i:i + 2] == "</":
                    j = i  # 找到第一个“</”的位置
                    for i in range(j, len(s_text)):
                        if s_text[i] == ">":  # 往后面找到紧挨着的“>”的位置
                            k = i
                            break
                    tagname = s_text[j + 2:k]  # 找到标签值
                    self.tagname_list.append(tagname)  # 将找到标签值存储在list变量中
            return self.tagname_list


    '''获取excel表格检查点单元格内的【json类型】所有标签名并存储在list变量tagname_list中'''
    def get_json_alltagnames(self,s_text):
        if s_text is None:
            print("\n入参源文件大小为空，请检查excel表格中检查点的字段\n")
            return
        else:
            k = 0
            j = 0
            self.tagname_list = []
            for i in range(len(s_text)):
                if s_text[i] == ":":
                    j = i - 1  #:号往回第一个【"】的位置坐标
                    k = j
                    while True:
                        k = k - 1
                        if (s_text[k]) == '"':  #:号往回第二个【"】的位置坐标
                            break
                    tagname = s_text[k + 1:j]  # 找到标签值
                    self.tagname_list.append(tagname)  # 将找到标签值存储在list变量中
            return self.tagname_list

    '''根据不同文本类型(XML/json）去除不需要对比的节点之间的内容'''
    def get_del_tagnames(self, s_text, tagname_list=None):
        t_num = 0  # 待去除的目标节点标签名的数量初始化为0
        text = ""  # 去除指定的标签名对应字符串后的文本初始化为空
        response_text = s_text
        if tagname_list is not None:
            t_num = len(tagname_list)  # 待去除的目标节点标签名的个数
        if s_text is None:
            print("\n入参源文件大小为空，有可能没有正确取到excel表格数据或者接口请求返回的数据为空请检查接口地址或环境是否有误\n")
            return
        else:
            if t_num == 0:
                return response_text  # 没有输入待去除的标签名，不做任何处理，直接返回源文本
            else:
                for i in range(t_num):
                    # 返回标签相关联的字符串
                    if s_text[0:5] == "<?xml":  # 查找xml文本中指定标签的关联字符串
                        tagname_text = self.get_xml_value(s_text, tagname_list[i])
                    elif s_text[0] == "{":  # 查找json文本中指定标签的关联字符串
                        tagname_text = self.get_json_value(s_text, tagname_list[i])
                    else:
                        tagname_text=""

                    if tagname_text is None or tagname_text=="":
                        print("没有找到%s标签对应的字符串，请核查" % tagname_list[i])
                    else:
                        text = re.sub(tagname_text, "", s_text)  # 将s_text文本中tagname_text关联的字符串替换为空即去除
                        s_text = text  # 将替换后的字符串赋值给s_text变量作为下一次替换的源文本，重复去除目标文本串
                        response_text = text  # 将替换后的字符串赋值给response_text用来作为函数的返回值
                return response_text


    '''从接口返回的数据中提取待校验的文本串'''
    def get_actual_check(self,expect_text,response_text,del_tagname_list=None):
        tagname_list=[] #从excel表格中预期检查点文本中提取的待校验的标签名构成的一个list变量，值初始化为空
        actual_check_list=[] #指定的标签名在接口返回的文本中对应的字符串的一个list变量，值初始化为空
        actual_check_text="" #接口返回的经处理过的最终校验文本初始化为空
        if expect_text is None:
            print("\n函数get_check_text入参源文件大小为空，请检查excel表格中检查点的字段\n")
            return
        elif response_text is None:
            print("\n接口返回的数据为空，请检查请求相关数据\n")
            return
        else:
            if expect_text[0:5] == "<?xml" or expect_text[0] == "{": #接口返回的xml格式/json格式的完整数据与预期全文本做完全对比校验
                if del_tagname_list is not  None: #
                    actual_check_text=self.get_del_tagnames(response_text,del_tagname_list)
                else:
                    actual_check_text = self.get_del_tagnames(response_text)
            else:
                if expect_text[0] == "<" and expect_text[0:5]!="<?xml":
                    tagname_list=self.get_xml_alltagnames(expect_text)  #返回excel表格当中预期检查点内容所有的待校验的标签名列表
                elif expect_text[0]=='"':
                    tagname_list=self.get_json_alltagnames(expect_text)
                if tagname_list==None:
                    print("未获取到excel表格中检查点的标签名列表")
                    return

                #从接口返回的完整数据中提取所有待检查标签的值构成一个文本，与预期关键检查点值进行校验对比
                #逐个将标签文本字符串追加到list变量actual_check_list，用于后面步骤提取出最终的校验文本actual_check_text
                for i in range(0,len(tagname_list)):
                    if expect_text[0] == "<" and expect_text[0:5] != "<?xml":
                        # post请求体的数据格式是xml格式调用get_xml_value函数获取指定关联的单个目标标签文本字符串
                        tagname_text = self.get_xml_value(response_text, tagname_list[i])
                        print("接口返回的数据中单个待校验标签对应的文本串为：\n", tagname_text)
                    elif expect_text[0]=='"':
                        # post请求体的数据格式是json格式调用get_json_value函数获取指定关联的单个目标标签文本字符串
                        tagname_text = self.get_json_value(response_text, tagname_list[i])
                        print("接口返回的数据中单个待校验标签对应的文本串为：\n", tagname_text)
                    if tagname_text is not None:
                        actual_check_list.append(tagname_text)
                if actual_check_list==[]:
                    actual_check_text = "从接口返回的数据中,未找到与excel表格中的预期检查点标签相匹配的的文本!"
                    print(actual_check_text)
                else:
                    # 从actual_check_list中逐个提取待校验标签对应字符串添加到最终待校验文本actual_check_text
                    for i in range(0,len(actual_check_list)):
                        actual_check_text=actual_check_text+actual_check_list[i]
            #print("接口返回的数据中全部待校验标签对应的文本串为:\n",actual_check_text)
            return actual_check_text












