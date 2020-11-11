import xml.dom.minidom
def get_xml_value(tag_name,order=0):
    '''读取xml配置文件'''
    xml_open = xml.dom.minidom.parse("webinterfacetest.xml")
    '''获取xml文档对象'''
    xml_root = xml_open.documentElement
    '''获取指定标签'''
    itemlist=xml_root.getElementsByTagName(tag_name) #根据标签名获取所有符合条件的标签存入list变量,通过下标取值

    '''获取标签的值，默认获取符合条件的第一个标签的值'''
    item_value=itemlist[order].firstChild.data
    #print("标签值为：",item_value)
    #print(type(item_value))
    return item_value

    # '''获取某一标签内某个属性的的属性值'''
    # itemlist = xml_root.getElementsByTagName('excel_path')  # 根据标签名获取所有符合条件的标签存入list变量
    # item = itemlist[0]
    # item_value = item.getAttribute("pwd")  # 获取excel_config标签的user属性值
    # print("属性值为:", item_value)

if __name__ == '__main__':
    a=int(get_xml_value("sheet_start"))
    print("类型:",type(a))