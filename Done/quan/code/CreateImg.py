import cv2
import numpy
import random

'''----------------------------------输入参数-------------------------------'''
'''10的倍数'''
picture_width = 80
picture_hight = 60
'''0—1'''
P = 0.2

'''------------------------------------代码---------------------------------'''
img = numpy.zeros([picture_hight, picture_width])

def change_color(Row, Cloumn):
    for i in range(Row * 10, Row * 10 + 10):
        for j in range(Cloumn * 10, Cloumn * 10 + 10):
            img[i][j] = 255 

white_list = []

for i in range(int(picture_hight / 10)):
    for j in range(int(picture_width / 10)):
        white_list.append([i, j])

for i in range(int((picture_width/10) * (picture_hight/10) * P)):
    coordinate_change = random.choice(white_list)
    white_list.remove(coordinate_change)

for i in white_list:
    change_color(i[0], i[1])

cv2.imwrite('F:/Project/PDL_Python/0.0_First/test.png', img)