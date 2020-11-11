text='<?xml version="1.0" encoding="GBK"?>\
<accept_in>\
 <order_content>\
   <order_type>11058002</order_type>\
   <accept_seq>1</accept_seq>\
   <order_req>\
     <home_city>591</home_city>\
     <customer_id name="bsz">591102059687767</customer_id>\
     <account_id>591200121573218</account_id>\
     <user_id>591600007053220</user_id>\
     <query_and>1</query_and>\
     <status>0</status>\
   </order_req>\
 </order_content>\
 <process_code>IA_QueryGroupAccountingRelationInfo</process_code>\
 <accept_id>200822724458</accept_id>\
 <sysfunc_id>91005043</sysfunc_id>\
 <accept_info>\
   <accept_city>590</accept_city>\
   <accept_province>5910</accept_province>\
   <identify_type>B</identify_type>\
   <request_seq>329696</request_seq>\
   <accept_org_id>0000000</accept_org_id>\
   <accept_org_name>外系统机构</accept_org_name>\
 </accept_info>\
 <operator_id>9998653</operator_id>\
 <operator_city>590</operator_city>\
 <request_source>304007</request_source>\
 <request_time>20191011101937</request_time>\
 <operator_info>\
   <operator_county>0</operator_county>\
   <operator_level>1</operator_level>\
   <operator_name>9998653</operator_name>\
   <operator_home_area/>\
   <operator_home_area_name/>\
 </operator_info>\
 <order_num>1</order_num>\
</accept_in>'
#返回文本中所输入的特定标签对应的值构成一个检查点字符串对比文本
#s_text='<accept_city>590</accept_city><accept_province>5910</accept_province><identify_type>B</identify_type>'
#若输入的参数为，accept_city，accept_province，则返回的字符串值为【5905910】
class GetFieldValue:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def get_text_value(self,s_text, tagname, resp_type):
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
            if resp_type == "text":
                if text == "":
                    print("\n注意参数%s入参值，在字符串中没有找到对应值，请输入正确的标签值!\n" % tagname)
                else:
                    #print("目标节点文本内容:\n", text)
                    return text

            elif resp_type == "value":
                if value == "":
                    print("\n注意参数%s入参值，在字符串中没有找到对应值，请输入正确的标签值!\n" % tagname)
                else:
                    #print("目标节点的取值\n", value)
                    return value
    def get_check_fieldvalue(self,s_text, fieldname1=None, fieldname2=None, fieldname3=None, fieldname4=None,
                   fieldname5=None):
        if s_text is None:
            print("\n入参源文件大小为空，有可能没有正确取到excel表格数据或者接口请求返回的数据为空请检查接口地址或环境是否有误\n")
            return
        else:
            self.resp_type="value"  # resp_type="value"为返回的类型为目标节点的值
            self.text = s_text
            fieldvalue="" #将获得的值存储在fieldvalue中
            if fieldname1 is not None:
                # 调用类中函数get_text_value获取指定的fieldname1标签对应的值并存放在变量fieldname1_value中
                fieldname1_value = self.get_text_value(self.text, fieldname1, self.resp_type)  # 若没找到，返回为None
                if fieldname1_value is None:
                    fieldname1_value=""
                fieldvalue=fieldname1_value
            if fieldname2 is not None:
                # 调用类中函数get_text_value获取指定的fieldname2标签对应的值并存放在变量fieldname2_value中
                fieldname2_value = self.get_text_value(self.text, fieldname2, self.resp_type)  # 若没找到，返回为None
                if fieldname2_value is None:
                    fieldname2_value= ""
                fieldvalue=fieldname1_value+fieldname2_value
            if fieldname3 is not None:
                # 调用类中函数get_text_value获取指定的fieldname3标签对应的值并存放在变量fieldname3_value中
                fieldname3_value = self.get_text_value(self.text, fieldname3, self.resp_type)  # 若没找到，返回为None
                if fieldname3_value is None:
                    fieldname3_value= ""
                fieldvalue=fieldname1_value+fieldname2_value+fieldname3_value

            if fieldname4 is not None:
                # 调用类中函数get_text_value获取指定的fieldname4标签对应的值并存放在变量fieldname4_value中
                fieldname4_value = self.get_text_value(self.text, fieldname4, self.resp_type)  # 若没找到，返回为None
                if fieldname4_value is None:
                    fieldname4_value= ""
                fieldvalue=fieldname1_value+fieldname2_value+fieldname3_value+fieldname4_value

            if fieldname5 is not None:
                # 调用类中函数get_text_value获取指定的fieldname5标签对应的值并存放在变量fieldname5_value中
                fieldname5_value = self.get_text_value(self.text, fieldname5, self.resp_type)  # 若没找到，返回为None
                if fieldname5_value is None:
                    fieldname5_value= ""
                fieldvalue=fieldname1_value+fieldname2_value+fieldname3_value+fieldname4_value+fieldname5_value
            print("返回指定检查点对应的值字符串:\n",fieldvalue)
            return fieldvalue
GCF=GetFieldValue()
GCF.get_check_fieldvalue(text,"customer_id","process_code","accept_org_name","operator_name","operator_info")
