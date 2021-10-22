'''使用时只需将输入的txt文件目录和输出的xls文件目录修改即可使用'''

import xlwt

InputPath = 'D:/project/Python/PDL_Python/TXTturntoEXCEL/RTSDB3D_2021-10-22 15_03_22_RigidbodiesData-2.txt'

txt1 = open(InputPath)
string1 = txt1.read()     #原文本字符串
string1 = string1.replace(' ', '')      #为了方便转换，将一些空格删除
list1 = string1.split()   #第一层以回车分割

#创建一个workbook对象，相当于创建一个Excel文件
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
#encoding = 'utf-8’说明了文本的编码方式， style_compression=0说明了是否允许改变excel表格样式。

# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
sheet = book.add_sheet('date', cell_overwrite_ok=True)
# 其中的date是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False

# 向表中添加表题
sheet.write(0, 0, 'Test')  # 其中的'0-行, 0-列'指定表中的单元，'X'是向该单元写入的内容
sheet.write(0, 1, 'World')
sheet.write(0, 2, 'Hello')

x = 1
y = 0

for first in list1:
    if first.find('Timestamp') == 0:
        list2 = first.split(':')
        list3 = list2[1].split(',')
        sheet.write(x, y, list3[0])
        sheet.write(x, y + 1, list3[1])
        x += 1
    elif first.find('name') == 0:
        pass
    else:
        pass
        # print(first)
        # list2 = first.split(',')    #第二层以逗号分隔
        # for second in list2:
        #     print(second)
        #     list3 = second.split(':')       #第三层以：号分隔
        #     for third in list3:
        #         print(third)
        #         sheet.write(x, y, list3[1])
        #     y += 1
        #     if y > 2:
        #         y = 0
        # x += 1

book.save(r'D:/project/Python/PDL_Python/TXTturntoEXCEL/RTSDB3D_2021-10-22 15_03_22_RigidbodiesData-2.xls')
