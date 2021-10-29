import xlwt
import csv

'''使用时修改以下参数'''
'''-----------------------------------------------------------------------------------'''
InputPath = 'D:/project/Python/PDL_Python/OptimizeExcel/testdata'
CsvName = '1v 70sulv-012346.csv'

# OutputPath = 'E:/Project/Python/PDL_Python/OptimizeExcel/test'
# ExcelName = 'test.xls'
OutputPath = 'D:/project/Python/PDL_Python/OptimizeExcel/testdata'
ExcelName = 'new1 .xls'

X_max1 = -245
X_min1 = -390

X_max2 = -545
X_min2 = -580
'''-----------------------------------------------------------------------------------'''

book = xlwt.Workbook(encoding = 'utf-8',style_compression = 0)     #创建excel
sheet = book.add_sheet(ExcelName, cell_overwrite_ok = True)

csvFile = open(InputPath + '/' + CsvName)     #读取文件
list1 = list(csv.reader(csvFile))   #将csv文件提取成列表形式

row_number = len(list1)         #读取行数
col_number = (len(list1[1]))    #读取列数

for i in range(5, row_number):
    for j in range(2, col_number, 3):
        if list1[i][j] != '':
            if X_min1 < float(list1[i][j]) < X_max1:
                sheet.write(i, 0, float(list1[i][j]))
                sheet.write(i, 1, float(list1[i][j + 1]))
                sheet.write(i, 2, float(list1[i][j + 2]))
            if X_min2 < float(list1[i][j]) < X_max2:
                sheet.write(i, 3, float(list1[i][j]))
                sheet.write(i, 4, float(list1[i][j + 1]))
                sheet.write(i, 5, float(list1[i][j + 2]))

book.save(OutputPath + '/' + ExcelName)