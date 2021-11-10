import xlwt
from xlwt.BIFFRecords import ExternnameRecord

def create_excel(ExcelName):
    global book
    global sheet
    book = xlwt.Workbook(encoding = 'utf-8',style_compression = 0)     #创建excel
    sheet = book.add_sheet(ExcelName, cell_overwrite_ok = True)
    return sheet

def save():
    book.save('D:/project/Python/PDL_Python/OptimizeExcel/code/123.xls')
    #