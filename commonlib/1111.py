import re
# text_temp_1="主机地址http://www.baidu.com  地址 "
# text_temp_2 = re.findall("http(.+?)$", text_temp_1)
# print("text_tmp_2:----",text_temp_2)
# text_temp = "http" + text_temp_2[0]
# print("text_temp",text_temp)

# if s_text[0:13]=="<?xml version":
#     print("xml格式")
# elif s_text[0]=="{":
#     print("json格式")

s_text2='<?xml version="1.0" encoding="GBK"? >'
s_text='{"userInfo":{"userType": "0","userId": "1001","userName": "用户名","areaCode": "591"}}'

class GJV:
    def __init__(self):
        pass
    def __del__(self):
        pass

    #返回指定的标签的值或对应的整个文本串
    #如s_text='{"userInfo":{"userType": "0","userId": "1001","userName": "用户名","areaCode": "591"}}'
    #输入标签名userId 返回标签值1001,或者文本串 "userId": "1001"
    def get_json_value(self,s_text,tagname, resp_type):
        if s_text is None:
            print("\n入参源文件大小为空，有可能没有正确取到excel表格数据或者接口请求返回的数据为空请检查接口地址或环境是否有误\n")
        else:
            n1=len(s_text)
            n2=len(tagname)
            text = ""  # 目标节点文本初始化为空字符
            value = ""  # 目标节点的取值初始化为空字符
            locat01=0 #tagname关联的第1个"的位置
            locat02=0 #tagname关联的第2个"的位置
            locat03=0 #tagname关联的第3个"的位置
            locat04=0 #tagname关联的第4个"的位置
            for i in range(n1-1):
                s='"'+tagname
                if s_text[i:i+len(s)] == s:
                    locat01 = i
                    print("locat01:",locat01)
                    for j in range(locat01+1,n1-1):
                        if s_text[j]=='"':
                            locat02=j
                            print("locat02:", locat02)
                            for k in range(locat02+1,n1-1):
                                if s_text[k]=='"':
                                    locat03=k
                                    print("locat03:", locat03)
                                    for m in range(locat03+1,n1-1):
                                        if s_text[m]=='"':
                                            locat04=m
                                            print("locat04:", locat04)
                                            text=s_text[locat01:locat04+1]
                                            value=s_text[locat03+1:locat04]
                                            print("text文本:",text)
                                            print("value值:",value)
                                            break
                                    break
                            break
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

G=GJV()
#G.get_json_value(s_text,"userName","text")
G.get_json_value(s_text,"userId","value")



