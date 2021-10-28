import xlwt
import xlrd

'''-----------------------------------------------------------------------------------'''
# InputPath = 'D:/project/Python/PDL_Python/TXTturntoEXCEL/box'
# TxtName = 'RTSDB3D_2021-10-22 16_33_26_RigidbodiesData-3.txt'
OutputPath = 'E:/Project/Python/PDL_Python/OptimizeExcel/test'
ExcelName = 'test.xls'
'''-----------------------------------------------------------------------------------'''

book = xlwt.Workbook(encoding = 'utf-8',style_compression = 0)
sheet = book.add_sheet('ExcelName', cell_overwrite_ok = True)

sheet.write(3, 2, 'Y')

book.save(OutputPath + '/' + ExcelName)