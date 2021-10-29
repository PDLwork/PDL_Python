import xlwt
import csv

'''使用时修改以下参数'''
'''-----------------------------------------------------------------------------------'''
InputPath = 'D:/project/Python/PDL_Python/OptimizeExcel/testdata'
CsvName = '1v 70sulv-012346.csv'

# OutputPath = 'E:/Project/Python/PDL_Python/OptimizeExcel/test'
# ExcelName = 'test.xls'
OutputPath = 'D:/project/Python/PDL_Python/OptimizeExcel/testdata'
ExcelName = 'new1.xls'

X_max1 = -245
X_min1 = -390

X_max2 = -545
X_min2 = -580
'''-----------------------------------------------------------------------------------'''

'''——————————————————创建Excel并设计格式——————————————————'''
book = xlwt.Workbook(encoding = 'utf-8',style_compression = 0)     #创建excel
sheet = book.add_sheet(ExcelName, cell_overwrite_ok = True)

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

#设计表格
sheet.write_merge(2, 2, 2, 7, 'Position', Style)
sheet.write_merge(3, 3, 2, 4, 'Wing1', Style)
sheet.write_merge(3, 3, 5, 7, 'Wing2', Style)
sheet.write_merge(2, 4, 1, 1, 'Frame', Style)
sheet.write(4, 2, 'X', Style)
sheet.write(4, 3, 'Y', Style)
sheet.write(4, 4, 'Z', Style)
sheet.write(4, 5, 'X', Style)
sheet.write(4, 6, 'Y', Style)
sheet.write(4, 7, 'Z', Style)

'''——————————————————读取csv内容并填入Excel——————————————————'''
csvFile = open(InputPath + '/' + CsvName)     #读取文件
list1 = list(csv.reader(csvFile))   #将csv文件提取成列表形式

row_number = len(list1)         #读取行数
col_number = len(list1[1])      #读取列数

for i in range(5, row_number):
    sheet.write(i, 1, i - 4)
    for j in range(2, col_number, 3):
        if list1[i][j] != '':
            if X_min1 < float(list1[i][j]) < X_max1:
                sheet.write(i, 2, float(list1[i][j]))
                sheet.write(i, 3, float(list1[i][j + 1]))
                sheet.write(i, 4, float(list1[i][j + 2]))
            if X_min2 < float(list1[i][j]) < X_max2:
                sheet.write(i, 5, float(list1[i][j]))
                sheet.write(i, 6, float(list1[i][j + 1]))
                sheet.write(i, 7, float(list1[i][j + 2]))

book.save(OutputPath + '/' + ExcelName)