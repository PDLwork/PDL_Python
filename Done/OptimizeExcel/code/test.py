from xlwt.BIFFRecords import SharedStringTable
import CreateExcel

if '__name__' == '__main__':
    CreateExcel.create_excel('456')
    global sheet
    sheet.write(1, 1, '?')
    book.save('D:/project/Python/PDL_Python/OptimizeExcel/code/123.xls')