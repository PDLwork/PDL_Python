import xlwt

'''使用时只需对以下内容修改即可使用'''
'''-----------------------------------------------------------------------------------'''
ThrowObject = 0     #丢向无人机的物品，1为fly（手里剑）、0为box（纸箱）
InputPath = 'E:/project/Python/PDL_Python/TXTturntoEXCEL/box'
TxtName = 'RTSDB3D_2021-10-22 16_33_26_RigidbodiesData-3.txt'
OutputPath = 'E:/project/Python/PDL_Python/TXTturntoEXCEL/box'
ExcelName = 'RTSDB3D_2021-10-22 16_33_26_RigidbodiesData-3.xls'
'''-----------------------------------------------------------------------------------'''

'''----------------------设计表格样式----------------------'''
#创建一个workbook对象，相当于创建一个Excel文件
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
#encoding = 'utf-8’说明了文本的编码方式， style_compression=0说明了是否允许改变excel表格样式。

# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
sheet = book.add_sheet('123', cell_overwrite_ok=True)
# 其中的ExcelName是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False

#设置对其方式(居中)
Alignment1 = xlwt.Alignment() # Create Alignment
Alignment1.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
Alignment1.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED

#设置字体样式（标题）
Font1 = xlwt.Font()
Font1.name = 'Times New Roman'
Font1.bold = True # 黑体
Font1.italic = True # 斜体字
#Font1.underline = True # 下划线

#设置边框样式
Borders1 = xlwt.Borders()
Borders1.left = xlwt.Borders.THIN     # DASHED虚线 NO_LINE没有 THIN实线
Borders1.right = xlwt.Borders.THIN
Borders1.top = xlwt.Borders.THIN
Borders1.bottom = xlwt.Borders.THIN
Borders1.left_colour = 0x40
Borders1.right_colour = 0x40
Borders1.top_colour = 0x40
Borders1.bottom_colour = 0x40

#创建类并设置字体风格
Style = xlwt.XFStyle()
Style.font = Font1
Style.alignment = Alignment1
Style.borders = Borders1

# 向表中添加表题
#sheet.write(0, 0, 'X', Style) # 其中的'0-行, 0-列'指定表中的单元，'X'是向该单元写入的内容, style为写入格式
#sheet.write_merge(x1, x2, y1, y2, 'X', Style)# 其从X1行合并到X2行，从Y1列合并到Y2列，'X'是向该单元写入的内容, style为写入格式
sheet.write_merge(0, 3, 0, 0, 'tv_sec', Style)
sheet.write_merge(0, 3, 1, 1, 'tv_usec', Style)
sheet.write_merge(0, 0, 2, 15, 'Name', Style)
sheet.write_merge(1, 1, 2, 8, 'drone', Style)
if ThrowObject == 1:
    sheet.write_merge(1, 1, 9, 15, 'fly', Style)
if ThrowObject == 0:
    sheet.write_merge(1, 1, 9, 15, 'box', Style)
sheet.write_merge(2, 2, 2, 4, 'Position', Style)
sheet.write_merge(2, 2, 5, 8, 'Quaternion', Style)
sheet.write_merge(2, 2, 9, 11, 'Position', Style)
sheet.write_merge(2, 2, 12, 15, 'Quaternion', Style)
sheet.write(3, 2, 'X', Style)
sheet.write(3, 3, 'Y', Style)
sheet.write(3, 4, 'Z', Style)
sheet.write(3, 5, 'X', Style)
sheet.write(3, 6, 'Y', Style)
sheet.write(3, 7, 'Z', Style)
sheet.write(3, 8, 'W', Style)
sheet.write(3, 9, 'X', Style)
sheet.write(3, 10, 'Y', Style)
sheet.write(3, 11, 'Z', Style)
sheet.write(3, 12, 'X', Style)
sheet.write(3, 13, 'Y', Style)
sheet.write(3, 14, 'Z', Style)
sheet.write(3, 15, 'W', Style)

#设置表格列宽  格式为一个0字符的1/256作为单位
sheet.col(0).width = 256 * 12
sheet.col(1).width = 256 * 8
for i in range(2, 16):
    sheet.col(i).width = 256 * 12

'''----------------------开始提取文本内容----------------------'''
'''----------------------采用分割字符串的方法----------------------'''
txt1 = open(InputPath + '/' + TxtName)  #读取文本目录
string1 = txt1.read()     #原文本字符串
string1 = string1.replace(' ', '')      #为了方便转换，将一些空格删除
list1 = string1.split()   #第一层以回车分割

#设置表格内容填写初始位置
x = 4

for first in list1:
    if first.find('Timestamp') == 0:    #判断不同的内容选择不同的分割方式并填入
        list2 = first.split(':')
        list3 = list2[1].split(',')
        sheet.write(x, 0, list3[0])
        sheet.write(x, 1, list3[1])
    elif first.find('name') == 0:
        if first.find('drone') == 5:
            list2 = first.split('-->')
            list3 = list2[1].split(':')
            list4 = list3[1].split(',')

            for i in range(0, 3):
                sheet.write(x, 2 + i, list4[i])

            list3 = list2[2].split(':')
            list4 = list3[1].split(',')

            for i in range(0, 4):
                sheet.write(x, 5 + i, list4[i])
            
        if ThrowObject == 0:
            if first.find('box') == 5:
                list2 = first.split('-->')
                list3 = list2[1].split(':')
                list4 = list3[1].split(',')

                for i in range(0, 3):
                    sheet.write(x, 9 + i, list4[i])
                
                list2 = first.split('-->')
                list3 = list2[2].split(':')
                list4 = list3[1].split(',')

                for i in range(0, 4):
                    sheet.write(x, 12 + i, list4[i])
                
                x += 1
            
        if ThrowObject == 1:
            if first.find('fly') == 5:
                list2 = first.split('-->')
                list3 = list2[1].split(':')
                list4 = list3[1].split(',')

                for i in range(0, 3):
                    sheet.write(x, 9 + i, list4[i])
                
                list2 = first.split('-->')
                list3 = list2[2].split(':')
                list4 = list3[1].split(',')

                for i in range(0, 4):
                    sheet.write(x, 12 + i, list4[i])
                
                x += 1

    else:
        pass

book.save(OutputPath + '/' + ExcelName)
