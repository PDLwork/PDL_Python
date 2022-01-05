import cv2
import numpy
import random

'''----------------------------------输入参数-------------------------------'''
picture_width = 50
picture_hight = 50
P = 0.5

'''------------------------------------代码---------------------------------'''
img = numpy.zeros([picture_width, picture_hight])

white_list = []
for i in range(picture_hight):
    for j in range(picture_width):
        white_list.append([i, j])

for i in range(int(picture_width * picture_hight * P)):
    coordinate_change = random.choice(white_list)
    white_list.remove(coordinate_change)

for i in white_list:
    img[i[0]][i[1]] = 255

cv2.imwrite('F:/Project/PDL_Python/0.0_First/test.png', img)