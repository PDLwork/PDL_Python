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

sheet1 = workBook.sheet_by_index(0)

#获取sheet内容
rows = sheet1.row_values(1)     #获取行内容
cols = sheet1.col_values(1)     #获取列内容

print(rows)
print(cols)

print(rows[2])
print(type(rows[2]))

if rows[2] == '':
    print(123)
