# import os
from typing import Awaitable, Text
import xlwt

# a = os.getcwd()     #获取当前目录
# print (a)       #打印当前目录
# os.chdir('E:/Project/Python/PDL_Python/TxttoExcel')     #定位到新的目录，请根据你自己文件的位置做相应的修改
# a = os.getcwd()     #获取定位之后的目录
# print(a)        #打印定位之后的目录

txt1 = open('E:/Project/Python/PDL_Python/TxttoExcel/test.txt')
a = txt1.read()
print(a)
list1 = a.split()
print(list1[0])

#创建一个workbook对象，相当于创建一个Excel文件
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
#encoding = 'utf-8’说明了文本的编码方式， style_compression=0说明了是否允许改变excel表格样式。

# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
sheet = book.add_sheet('date', cell_overwrite_ok=True)
# 其中的date是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False

# 向表中添加表题
sheet.write(0, 0, 'X')  # 其中的'0-行, 0-列'指定表中的单元，'X'是向该单元写入的内容
sheet.write(0, 1, 'Y')
sheet.write(0, 2, 'Z')

book.save(r'E:/Project/Python/PDL_Python/TxttoExcel/test.xls')