#encoding=utf-8
import xlrd
import xlwt
import os
from xlutils.copy import copy
excel_path="D:\PythonProject\data_excel\五中心测试.xls"
sheet_index=2
row_i=5
col_j=15
text='<?xml version="1.0" encoding="GBK"?>\
<accept_in>\
 <order_content>\
   <order_type>11058002</order_type>\
   <accept_seq>1</accept_seq>\
   <order_req>\
     <home_city>591</home_city>\
     <customer_id>591102059687767</customer_id>\
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

book_excel=xlrd.open_workbook(excel_path, formatting_info=True)
old_excel=book_excel
# 将操作文件对象拷贝，变成可写的workbook对象
new_excel=copy(old_excel)
# 获得第一个sheet的对象
sheet_index=sheet_index-1
new_sheet= new_excel.get_sheet(sheet_index)

# 预定一个字体相关的格式对象style
style=xlwt.XFStyle()
# 字体参数相关配置
font=xlwt.Font()
font.name="Microsoft YaHei UI"
font.bold=False  # 是否加粗，True为加粗
font.height=250  # 如果是200对应的是10号字体
style.font=font
# 边框
borders=xlwt.Borders()
borders.top=xlwt.Borders.THIN
borders.bottom=xlwt.Borders.THIN
borders.left=xlwt.Borders.THIN
borders.right=xlwt.Borders.THIN
style.borders=borders
# 写入数据
new_sheet.write(row_i-1,col_j-1,text,style)
#另存为excel文件，并将文件命名如果与原来文件重名则修改原文件
#os.remove(excel_path)
new_excel.save(excel_path)
