#encoding="utf-8"
import pytest
from business.login_out import Login_Out
import time
from test_pytest.pytestfun import *
from commonlib import globalvar #导入跨文件全局变量.py文件

'''报告目录如果没有程序会自动创建，不需要事先创建好目录'''
if __name__ == '__main__':
    '''第三方报告转换程序allure所在bin目录'''
    allure_path = "d:\\性能测试相关\\allure-2.13.0\\bin"

    '''执行pytest命令后生成的初始allure格式的测试报告存储路径'''
    allurereport_path="E:\\data_excel\\report\\allure_report"
    allurereport_path2="--alluredir=E:\\data_excel\\report\\allure_report"

    '''经第三方allure工具转换后生成的html格式的测试报告存储路径'''
    htmlreport_path="E:\\data_excel\\report\\html-report"

    '''测试报告邮件接收相关配置'''
    smtp_server = "smtp.139.com"  # 邮件发送服务器
    smtp_port = 25  # 邮件端口号，一般为25，不同服务器不同端口号
    username = "18850139950@139.com"  # 邮件发送账号需登陆邮箱开启POP3/SMTP服务
    password = "Bsz_051205"  # 邮件发送者登陆密码
    recv = ["601259294@qq.com", "18850139950@139.com"]  # 多个接收者邮箱
    mailtitle = "内容计费平台测试自动化测试报告，详情见附件"  # 邮件主题
    mailcontent = "这是python自动化测试完成后系统自动发起的测试报告邮件，" \
                  "请下载附件解压后用火狐浏览器打开index.html,可在左下方菜单点击界面语言【zh】切换为中文" \
                  "并点击【功能】选项卡查看测试报告，" \
                  "详情见附件，若有问题请联系鲍仕枝！"  # 邮件正文
    report_path = "E:\\data_excel\\report\\html-report.zip"  # 邮件附件本地路径
    att_name = "内容计费平台测试.zip"  # 附件后缀名必须与源文件后缀名相同


    '''
    执行pytest测试前，先删除原先生成的allure初始格式报告，以便生成新的,
    防止转换为目标html格式时把旧的初始格式报告也一起转换了
    '''
    del_folder(allurereport_path)

    '''
    调用pytest.main函数执行当前.py文件所在目录及子目录下所有符合条件的test文件夹/文件/类/函数
    "--html=../report/report.html"])  
    --alluredir生成支持allure能够解析的初始测试报告
    --html直接生成html格式报告
    --reruns 1 失败时再执行1次
    -s -v,表示详细输出
    r,代表不需要转义特殊字符
    '''
    r_num="0"#运行失败时重复执行的次数，注意需输入字符串类型
    html_report="--html=E:\\data_excel\\report\\report.html" #执行pytest命令生成的简易html格式报告文件名

    #构造pytest.main入参list变量类型参数params
    params = []
    params.append("--reruns")
    params.append(r_num)
    params.append("-s")
    params.append("-v")
    params.append(allurereport_path2)
    params.append(html_report)

    '''执行pytest主函数之前先登录平台，获取driver会话ID，并设置跨文件全局变量供pytest模式下各test函数调用'''
    LG=Login_Out() #初始化登录类，在pytest执行前做好设置driver全局变量工作
    LG.login("baoshizhi","123qweQWE-")
    globalvar._init()
    globalvar.set_value('g_driver', LG.driver)

    '''执行pytest测试生成allure报告及简易html格式报告'''
    pytest.main(params)
    #pytest.main(["--reruns","0","-s","-v",r"--alluredir=../report/allure_report",r"--html=../report/report.html"])
    #LG.web_quit() #全部测试完毕后关闭浏览器

    #拼接命令参数command_params用于执行allure generate命令转换生成html格式的报告
    command_params = "allure generate " + allurereport_path + " -o " + htmlreport_path + " --clean"
    #allure generate D:\PythonProject\Report\allure_report -o D:\PythonProject\Report\html-Report --clean
    '''调用allure_to_html函数将报告转换为html格式的精美报告,并打包成zip格式'''
    allure_to_html(allure_path,command_params,htmlreport_path)


    time.sleep(5) #报告打包成zip格式5秒后发送邮件
    '''
    调用邮件发送函数进行发送测试报告邮件,当前配置的发送服务器为139邮箱
    '''
    #调用邮件发送函数
    #send_email(smtp_server,smtp_port,username,password,recv,mailtitle,mailcontent,report_path,att_name)
