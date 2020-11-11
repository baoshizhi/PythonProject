#encoding=utf-8
from commonlib.get_textvalue import *
from commonlib.request import *
import time
from commonlib.read_xml import *

'''相关xml配置文件见business目录，main函数整体说明见文末'''
if __name__ == '__main__':
    '''
    该变量表示所有sheet表下的所有行不需要校验的标签名集合为空表示全文本对比
    (不剔除任何标签名关联的字符串)
    '''
    tagname_line_list = ["accept_id", "response_time", "request_time"]

    excel_path=get_xml_value("excel_path") #从xml配置文件中获取excel表路径
    # 实例化一个读取excel表格内容的类
    readexcel = ReadWriteExcel()
    '''
    1)打开excel表并返回表中的sheet数目或者load_workbook对象(0-返回sheet数目  1--返回excle中的load_workbook对象)
    2)每调用一次readexcel.open_excel函数生成的load_workbook对象均不相同，
    3)后面打开sheet表操作函数readexcel.open_sheet(i)和保存excel表操作函数book_excel.save(excel_path)
     依赖的是后执行的【代码行2】生成的load_workbook对象
    '''
    sheet_total = readexcel.open_excel(excel_path,0) #代码行1
    book_excel= readexcel.open_excel(excel_path,1)#代码行2

    sheet_start=int(get_xml_value("sheet_start"))
    sheet_stop=int(get_xml_value("sheet_stop"))
    sheet_stop_tag=get_xml_value("sheet_stop_tag")#控制sheet_stop字段

    row_start = int(get_xml_value("row_start"))
    row_stop = int(get_xml_value("row_stop"))
    row_stop_tag=get_xml_value("row_stop_tag") #控制row_stop字段


    request_host_col=int(get_xml_value("request_host_col"))#主机地址所在列序号
    request_type_col=int(get_xml_value("request_type_col"))#excel表中request请求接口类型(post/get)所在的列序号(列计数从1开始)
    request_text_col=int(get_xml_value("request_text_col"))#excel表中request请求体数据所在的列序号(列计数从1开始)
    expect_text_col=int(get_xml_value("expect_text_col")) #excel表中request请求后返回的数据预期值所在的列序号(列计数从1开始)
    test_status = get_xml_value("test_status")
    test_status_col = int(get_xml_value("test_status_col"))  # 插入表格中的执行状态列序号
    test_result_col = int(get_xml_value("test_result_col"))  # 插入表格中的结果描述列序号
    resp_data_col = int(get_xml_value("resp_data_col"))  # 返回的结果报文插入表格中的目标列序号

    # 实例化一个接口测试请求操作类PortOperation
    PortTest = PortOperation()
    # 实例化一个文本检查点的基类
    GTV = GetTextValue()

    if sheet_stop_tag=="on":  #如果满足[on]条件，手动控制执行sheet表的个数
        sheet_total=sheet_stop
    for i in range(sheet_start,sheet_total+1): #遍历每一个sheet子表
        # 打开第i个sheet子表,并返回总行数
        lines_total=readexcel.open_sheet(i)
        if row_stop_tag=="on":
            lines_total=row_stop
        for row_i in range(row_start,lines_total+1):  #循环提取当前sheet子表的每一行数据并向服务器发起请求
            print("----提取第%d个sheet表第%s行数据向服务器发起请求----"%(i,row_i))
            # 从excel表格中获取接口测试的相关请求体信息
            host=readexcel.get_request_data(request_host_col,request_type_col,request_text_col,expect_text_col,row_i,get_xml_value("type",0))

            send_type=readexcel.get_request_data(request_host_col,request_type_col,request_text_col,expect_text_col,row_i,get_xml_value("type",1))
            send_data_source=readexcel.get_request_data(request_host_col,request_type_col,request_text_col,expect_text_col,row_i,get_xml_value("type",2))
            exp_data = readexcel.get_request_data(request_host_col, request_type_col, request_text_col, expect_text_col,
                                                  row_i, get_xml_value("type",3))
            if host is None or send_type is None or send_data_source is None or exp_data is None :
                print("----未获取到第%d个sheet表第%s行的主机/请求类型/请求体数据/预期检查点数据，请检查表格数据----"%(i, row_i))
                actual_data_source="未获取到表格中正确的相关数据[主机/请求类型/请求体数据/预期检查点数据]"
                readexcel.write_excel(i, row_i, resp_data_col, actual_data_source)
                continue #中断本次循环，进入下一行测试
            print("request主机地址：\n", host)
            print("request请求体数据:\n",send_data_source)
            #print("预期检查点数据exp_data:\n",exp_data)
            exp_check_data = GTV.get_del_tagnames(exp_data, tagname_line_list)
            print("预期待校验文本exp_check_data\n", exp_check_data)
            #print(send_data)

            #调用类中的请求函数向服务器发起测试请求, 并保存返回数据
            #接口请求后返回的初始数据actual_data_source,返回类型为[text],也可为[json]
            actual_data_source=PortTest.get_response(host,send_data_source,send_type)
            print("request请求后返回的数据actual_data_source:\n",actual_data_source)
            # 接口请求后返回的经去除空白字符后的数据actual_data
            actual_data=PortTest.get_del_blank(actual_data_source)
            #print("actual_data:\n",actual_data)

            #接口返回的数据中提取需要检验对比的检查点文本
            # 每一行不需要校验的标签名均相同，找不到某个标签则不删除该标签关联的字符串
            actual_check_data=GTV.get_actual_check(exp_data,actual_data,tagname_line_list)
            print("接口返回的待校验标签对应的字符串actual_check_data:",actual_check_data)

            # 将返回的初始数据actual_data_source写回excel表格(参数说明:sheet表序号(从1开始计数)|单元格行号|列号，数据文本
            readexcel.write_excel(i, row_i,resp_data_col, actual_data_source)  # 写入返回报文
            readexcel.write_excel(i,row_i,test_status_col,test_status) #写入执行状态[是否执行]
            #将返回的检查点文本与预期的的检查点文本进行比较，以判断接口测试请求是否通过
            if actual_check_data==exp_check_data:
                print("\n该接口请求测试通过\n")
                readexcel.write_excel(i, row_i, test_result_col,get_xml_value("result",0)) #写入【通过】
            else:
                readexcel.write_excel(i, row_i, test_result_col,get_xml_value("result",1)) #写入【不通过】
                print("\n该接口请求测试不通过\n")
        #当完成一次sheet表的测试，统一做一次保存excel表操作（如果边写入边保存执行效率很低）
        book_excel.save(excel_path)
        time.sleep(3)

'''
  1)excel文档只支持xlsx格式，如果执行程序时遇到错误1等稀奇古怪的非语法逻辑错误
    建议清除表格当中所有子表的一切格式重新再试一下
    错误1：Max value is {0}'.format(self.max)) ValueError: Max value is 14
    错误2：zipfile.BadZipFile: File is not a zip file:(表格被破坏了，换一个表格)
    强制停止运行，有可能导致excel表格被损坏打不开，导致错误2发生，所以建议先把初始数据表备一份
  2)对excel表进行接口测试时如果加载异常缓慢,则可以通过新建一个excel文件
    把每个sheet表内容复制过来，再执行测试会大大加快执行速度！
    如果运行时超时退出，可在request.py文件中的request_error函数增加超时时间time_out的值
  3)注意excel表格当中预期检查点单元格的数据
    i)如果以<?xml...>开头代表的xml格式数据或者以{ 开头的json格式数据则表示返回的接口数据与该单元格预期数据
      做全文本对比，但可根据输入的关于不需要对比标签list变量tagnames_list值去除不需要对比的节点，

      该变量为空则进行完全对比，如果每一行需要剔除的标签名不同，可直接在tagnames_list添加上所有不同的标签名
      如数据行1不需要对比的节点是accept_id，name
        数据行2不需要对比的节点是request_time
        数据行3不需要对比的节点是response_time
        则设置节点list变量tagname_line_list=["accept_id","name",response_time","request_time"]
        若不需要剔除任何节点标签，则设置tagname_line_list=[]进行全文本对比               
    ii)如果以类似格式<resp_code>10000017</resp_code>开头
       或者以"mktCaseId": "100030","auditStatus": "10"开头，则只对比这些节点的数据
  4)重点关注三个配置
    i)是否循环执行所有的sheet表，相关配置变量为【sheet_start/sheet_stop/sheet_stop_tag】
    ii)是否循环执行当前表下的所有行配置，相关配置变量为【row_start/row_stop/row_stop_tag】
    iii)所有行待剔除校验的标签名都设置为一样
        即把所有行接口涉及到的不需要校验的标签全都加载到【tagname_line_list】         
  5）针对预期检查点文本为【全文本】类型时但某些标签字段不需要对比校验时，相关配置变量见4)-iii
  6）只支持excel表格下所有的sheet表的相关配置共用一套统一的配置，不支持独立配置不同的sheet表
  7）需要配置的参数如下：
     excel_path:带表名的excel表绝对路径
     sheet_start:开始接口测试的sheet子表序号(子表计数从1开始)
     sheet_stop:手动配置的停止测试的sheet子表序号
                 如sheet_stop==3时表示第3个sheet表运行结束后就不再运行其他sheet表下的接口测试，
                   （注：sheet_stop_tag=="on"时本设置才生效)
     sheet_stop_tag:是否开启按手动配置运行结束的sheet子表序号标志(一般设为"off",测试全部sheet表)
                    "off"表示读取excel表格下的所有子sheet表并进行测试
                    "on"表示手动指定停止测试的sheet子表序号
     row_start: 当前sheet子表进行接口测试的目标数据起始行序号(行计数从1开始)
     row_stop:  当前sheet子表中手动配置的停止测试的数据行所在序号
                如row_stop=10表示第10行运行完后停止运行该sheet表其他数据行
                  （注：row_stop_tag=="on"时该设置才生效）
     row_stop_tag:是否开启手动指定停止运行结束的行序号标志，（一般设为"off",测试全部数据行）
                  "off"表示执行到当前sheet表格下的最后一行数据，
                  "on"表示开启手动指定停止运行的行数
     tagname_line_list：所有sheet表下的所有行不需要校验的标签名集合
                        tagname_line_list=[]为空表示全文本对比(不剔除任何标签名关联的字符串)
                        tagname_line_list=["accept_id","response_time","request_time"]
                        表示从对比的全文本数据中剔除accept_id，response_time，request_time相关联的文本串
                        剔除后再对比剩下的文本

     request_host_col=7 #主机地址所在列序号(列计数从1开始)
     request_type_col=8 #excel表中request请求接口类型(post/get)所在的列序号(列计数从1开始)
     request_text_col=9 #excel表中request请求体数据所在的列序号(列计数从1开始)
     expect_text_col=10 #excel表中request请求后返回的数据预期值所在的列序号(列计数从1开始)
     resp_type = ["host", "send_type", "send_data", "exp_data"] #list变量
     # 函数指定的待返回数据类型分为
       (主机host/请求类型send_type /请求体数据send_data/预期数据exp_data/请求体数据类型body_type)    
     # list变量类型通过下标取值 resp_type[0-3]

     test_status = "已执行"
     test_status_col = 11  #表格中的执行状态列序号
     test_result = ["通过", "未通过"] #测试结果说明，分为【通过]与【未通过】
     test_result_col = 12  #结果描述列序号
     resp_data_col = 13  #返回的结果报文列序号
  '''