import xlwt
import xlrd

'''-----------------------------------------------------------------------------------'''
# InputPath = 'D:/project/Python/PDL_Python/TXTturntoEXCEL/box'
# TxtName = 'RTSDB3D_2021-10-22 16_33_26_RigidbodiesData-3.txt'
OutputPath = 'E:/Project/Python/PDL_Python/OptimizeExcel/test'
ExcelName = 'test.xls'
'''-----------------------------------------------------------------------------------'''

book = xlwt.Workbook(encoding = 'utf-8',style_compression = 0)
sheet = book.add_sheet(ExcelName, cell_overwrite_ok = True)

sheet.write(3, 2, 'Y')

book.save(OutputPath + '/' + ExcelName)

# 打开文件
workBook = xlrd.open_workbook('E:/Project/Python/PDL_Python/OptimizeExcel/test/test1.xls')
allSheetNames = workBook.sheet_names()

sheet1 = workBook.sheet_by_index(0)         #根据索引获取表格， 一个excel文件里面会有多个表格，在excel下方可以看见

#获取表格的行数和列数
row_number = sheet1.nrows
col_number = sheet1.ncols

#获取单元格内容(三种方式)
#   print(sheet1_content1.cell(1, 0).value)
#   print(sheet1_content1.cell_value(2, 2))
#   print(sheet1_content1.row(2)[2].value)

#获取sheet中一行或一列内容
# rows = sheet1.row_values(9)     #获取行内容
# cols = sheet1.col_values(4)     #获取列内容

for i in range(0, col_number):
    cols = sheet1.col_values(i)
    for j in range(0, row_number):
        value = sheet1.cell_value(j, i)
        if value != '':
            if 0 < value < 10:
                sheet.write(j, 0, value)

book.save(OutputPath + '/' + ExcelName)