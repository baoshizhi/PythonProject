import os
import glob   #用于读取路径下的文件名或者文件夹名
import shutil #用于压缩文件
import smtplib
import socket
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication #用于加载附件

'''删除指定文件夹下的所有内容'''
def del_folder(path):
    '''读取path路径下所有的文件名,list变量'''
    FileNames=glob.glob(path+r'\*')

    '''循环删除文件夹及文件'''
    for filename in FileNames:
        try:
            '''如果是文件则直接删除，是文件夹则进入异常分支'''
            os.remove(filename)
        except:
            try:
                '''如果是空文件夹，直接删除，文件夹不为空，则进入异常分支'''
                os.rmdir(filename)
            except:
                '''先删除文件'''
                del_folder(filename)
                '''再删除文件夹'''
                os.rmdir(filename)

'''调用本机系统的allure.bat程序将allure初始格式报告转换成html格式的报告'''
def allure_to_html(allure_path,command_params,htmlreport_path):
     '''改变工作目录,定位到系统程序allure所在bin目录'''
     #allure_path = r"d:\性能测试相关\allure-2.13.0\bin"
     os.system(allure_path)


     '''
       allure generate [path_from] -o [path_to] --clean
       [path_from]:D:\PythonProject\Report\allure_report  初始报告路径
       [path_to]：D:\PythonProject\Report\html-Report     目标html格式报告路径
       --clean 表示删除原有[path_to]html文件夹下的html报告后再生成新的html报告
     '''
     # allure generate D:\PythonProject\Report\allure_report -o D:\PythonProject\Report\html-Report --clean"
     '''调用allure generate进行转换得到html格式的报告并存入文件夹'''
     os.system(command_params)

     '''将生成的报告文件夹打包成zip格式，供后续邮件作为附件发送'''
     source_dir = htmlreport_path #待打包的源html格式的报告路径
     path_zipname = htmlreport_path  # 经打包后带路径的zip文件名
     shutil.make_archive(path_zipname, "zip", source_dir) # 把测试报告打包成ZIP格式


'''邮件发送'''
def send_email(smtp_server,smtp_port,username,password,recv,mailtitle,mailcontent,report_path,att_name):
    '''邮件服务器地址,smtp,不要写成stmp'''
    host_server = smtp_server
    host_port = smtp_port

    '''邮件发送账号及密码，需登陆邮箱开启POP3/SMTP服务'''
    sender=username
    pwd = password

    '''邮件接收地址'''
    receiver=recv

    '''邮件主题'''
    mail_title=mailtitle

    '''邮件正文内容'''
    mail_content=mailcontent

    '''
    创建一个带测试报告附件的实例,使用MIMEMultipart来标示这个邮件是多个部分组成的，
    然后attach各个部分。如果是附件，则add_header加入附件的声明   
    '''
    message=MIMEMultipart()
    message['From']=sender #邮件发送者
    #message['To']=receiver #只支持单个邮件收件者，参数为字符串类型
    message['To']=','.join(receiver) #支持多个邮件接收者，参数为list变量类型

    message['Subject']=mail_title #邮件标题

    #加载邮件正文plain纯文本,html
    message.attach(MIMEText(mail_content,"plain",'utf-8'))

    '''构造附件,构造后的filename附件名称的后缀名必须与源文件相同'''
    # 读取文件
    att_report=MIMEApplication(open(report_path,'rb').read())
    #添加附件头部声明
    att_report.add_header('Content-Disposition','attachment',filename=att_name)
    #加载邮件附件
    message.attach(att_report)

    try:
        smtp=smtplib.SMTP(host_server,host_port)#连接到指定的stmp服务器
        smtp.set_debuglevel(1)#参数值为1表示开启调试模式，参数值为0关闭调试模式
        smtp.ehlo(host_server) #向stmp服务器确认身份
        smtp.login(sender,pwd) #登陆smtp服务器
        smtp.sendmail(sender,receiver,message.as_string()) #发送邮件
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('发送邮件失败')
    except socket.gaierror:
        print("连接邮件服务器错误，发送邮件失败，请检查网络")