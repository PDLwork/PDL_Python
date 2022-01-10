import cv2
import numpy

'''----------------------------------输入参数-------------------------------'''
#改变图片大小可能会出bug
picture_width = 110
picture_hight = 110
Coarse_output_path = 'D:/project/Python/Coarse_img'

'''------------------------------------代码---------------------------------'''
Coarse_img = numpy.zeros([picture_hight, picture_width])

for i in range(picture_hight):
    for j in range(picture_width):
        Coarse_img[i][j] = 255
cv2.imwrite(Coarse_output_path+ '/img0.png', Coarse_img)

def change_color(Row, Cloumn, color):
    for i in range(Row * 10, Row * 10 + 10):
        for j in range(Cloumn * 10, Cloumn * 10 + 10):
            if color == 'grey':
                Coarse_img[i][j] = 127
            if color == 'black':
                Coarse_img[i][j] = 0

def create_img(gray_list, black_list):
    for i in gray_list:
        change_color(i[0], i[1], 'grey')
    for i in black_list:
        change_color(i[0], i[1], 'black')

black_list = []

for i in range(6):
    gray_list = []
    for j in range(5 - i, 6 + i):
        for k in range(5 - i, 6 + i):
            gray_list.append([j, k])
    create_img(gray_list, black_list)
    cv2.imwrite(Coarse_output_path+ '/img%d' %(i*2+1) + '.png', Coarse_img)

    black_list = gray_list
    create_img(gray_list, black_list)
    cv2.imwrite(Coarse_output_path+ '/img%d' %(i*2+2) + '.png', Coarse_img)