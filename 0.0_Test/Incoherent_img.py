import cv2
import numpy
import random

'''----------------------------------输入参数-------------------------------'''
#改变图片大小可能会出bug
picture_width = 110
picture_hight = 110
Incoherent_output_path = 'D:/project/Python/Incoherent_img'

'''------------------------------------代码---------------------------------'''
Incoherent_img = numpy.zeros([picture_hight, picture_width])

for i in range(picture_hight):
    for j in range(picture_width):
        Incoherent_img[i][j] = 255
cv2.imwrite(Incoherent_output_path+ '/img0.png', Incoherent_img)

def change_color(Row, Cloumn, color):
    for i in range(Row * 10, Row * 10 + 10):
        for j in range(Cloumn * 10, Cloumn * 10 + 10):
            if color == 'grey':
                Incoherent_img[i][j] = 127
            if color == 'black':
                Incoherent_img[i][j] = 0

def create_img(gray_list, black_list):
    for i in gray_list:
        change_color(i[0], i[1], 'grey')
    for i in black_list:
        change_color(i[0], i[1], 'black')

temporary_list = []
for i in range(11):
    for j in range(11):
        temporary_list.append([i, j])

black_list = []
gray_list = []

for i in range(6):
    if i == 0:
        temporary_site = random.choice(temporary_list)
        temporary_list.remove(temporary_site)
        gray_list.append(temporary_site)
    else:
        for j in range((i*2+1)**2 - (i*2-1)**2):
            temporary_site = random.choice(temporary_list)
            temporary_list.remove(temporary_site)
            gray_list.append(temporary_site)

    create_img(gray_list, black_list)
    cv2.imwrite(Incoherent_output_path+ '/img%d' %(i*2+1) + '.png', Incoherent_img)

    #black_list = gray_list
    #TMD找了一个多小时，终于找出你了，为什么刚刚就不出错，直接赋值会赋地址？
    black_list = gray_list.copy()
    create_img(gray_list, black_list)
    cv2.imwrite(Incoherent_output_path+ '/img%d' %(i*2+2) + '.png', Incoherent_img)