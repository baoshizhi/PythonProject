#encoding="utf-8"
#import xml.etree.ElementTree as ET
from lxml import etree  #用lxml解析避免被解析xml文本中因混合编码类型引起的错误

#解析文件,将一个文件或者字符串解析为树结构 element tree。
xml_tree=etree.parse("D:\PythonProject\data_excel\五中心.xml")

#获得xml文本的根节点对象
xml_root=xml_tree.getroot()
print("根节点对象:",xml_root)
print("根节点名称:",xml_root.tag)

#输出xml文本的内容
#text=etree.tostring(xml_root)
#print("xml文本内容：\n",text)

#找到第一个accept_id标签
xml_tag=xml_root.find("accept_id")

print("tag:",xml_tag)
print("类型：",type(xml_tag))
print("值为:", xml_tag.text)

# #遍历所有的account_id标签,并打印标签的值
# for ele in xml_root.findall("account_id"):
#     print("account_id值:",ele.text)