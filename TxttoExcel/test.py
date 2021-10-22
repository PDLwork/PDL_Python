import xlwt

txt1 = open('E:/Project/Python/PDL_Python/TxttoExcel/test.txt')
string1 = txt1.read()     #原字符串
print(string1)
print()

list1 = string1.split()   #第一层以回车分割
print(list1)
len1 = len(list1)
print(list1[0])
print()

list2 = list1[0].split(',')     #第二层以逗号分割
print(list2)
len2 = len(list2)
print(list2[0])
print()

list3 = list2[0].split(':')     #第三层以冒号分割
print(list3)
print()

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
    print(first)
    list2 = first.split(',')
    for second in list2:
        print(second)
        list3 = second.split(':')
        for third in list3:
            print(third)
            sheet.write(x, y, list3[1])
        y += 1
        if y > 2:
            y = 0
    x += 1

book.save(r'E:/Project/Python/PDL_Python/TxttoExcel/test.xls')