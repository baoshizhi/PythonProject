s_text='<?xml version="1.0" encoding="GBK"?>\
<accept_in>\
 <order_content name="bsz">\
   <order_type>11058002</order_type>\
   <accept_seq>1</accept_seq>\
   <order_req>\
     <home_city>591</home_city>\
     <customer_id a="11">591102059687767</customer_id>\
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
#<response_time  name="bsz">XXXX</response_time>
def get_text_value(s_text, tagname, resp_type):
    if s_text is None:
        print("\n入参源文件大小为空，有可能没有正确取到excel表格数据或者接口请求返回的数据为空请检查接口地址或环境是否有误\n")
    else:
        n1 = len(s_text)  # print("源文本大小:", n1)
        tagnamehead01 = "<" + tagname  # print("tagnamehead01:", tagnamehead02)
        tagnamehead02=">"
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
                    if s_text[i]==">": #获取tagname标签头的闭合字符[>]在整个字符串中的位置
                        head_i02=i
                        break
            elif  s_text[i:i + n4] == tagnametail:
                tail_i = i  # print("tail_i:", tail_i) #获取tagname尾部标签在整个字符串中的位置 </response_time>
                text = s_text[head_i01:tail_i+ n4]  # 截取目标节点文本内容text
                value = s_text[head_i02+1:tail_i]  # 截取目标节点间的value值
                break
        if resp_type == "text":
            if text == "":
                print("\n注意参数%s入参值，没有找到对应值，请输入源字符串中存在的子字符串!\n" % tagname)
            else:
                print("目标节点文本内容:\n", text)
                return text

        elif resp_type == "value":
            if value == "":
                print("\n注意参数%s入参值，没有找到对应值，请输入源字符串中存在的子字符串!\n" % tagname)
            else:
                print("目标节点的取值\n", value)
                return value



get_text_value(s_text,"customer_id", "text")
get_text_value(s_text,"customer_id", "value")
