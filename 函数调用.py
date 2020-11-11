#encoding=utf-8

#导入系统路径，并加载所引用.py文件模块所在目录的相对路径或绝对路径
import sys
#sys.path.append("D:/PythonProject/commonlib")  #绝对路径
sys.path.append("./commonlib") #相对路径

#从commonlib目录下导入commonfun.py文件
from commonlib import commonfun

#调用.py文件中(commonfun.py)的某个具体函数CommShare
com=commonfun.CommShare()
com.open_url("https://www.baidu.com")
#com.locate_element("link","新闻").click()
#com.locate_element("name", "wd").send_keys("我爱你中国")
#com.input("name","wd","我和我的祖国")
#com.locate_element("id", "su").click()
#com.locate_element("class", "bg").click()
#com.locate_element("xpath", "//*[@id='su']").click()
#com.locate_element("css", "#su").click()
#com.click("css","#su")
text=com.get_text("name","tj_trxueshu")
print("获取到的标签文本:",text)
attrname=com.get_attr("name","tj_trxueshu","href")
print("标签对应的href属性值：",attrname)





