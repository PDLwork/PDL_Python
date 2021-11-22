import xlwt
import numpy

def array_print_excel(Array):
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = book.add_sheet('123', cell_overwrite_ok=True)

    n, m = Array.shape
    for i in range(n):
        for j in range(m):
            sheet.write(i, j, float(Array[i][j]))
            book.save('Test.xls')

if __name__ == '__main__':
    kernel1 = numpy.array\
    ([
        [1,0,-1,2],
        [1,0,-1,2],
        [1,0,-1,2],
    ])
    array_print_excel(kernel1)