import cv2
import numpy
import random

'''----------------------------------输入参数-------------------------------'''
#改变图片大小可能会出bug
picture_width = 110
picture_hight = 110
Incoherent_output_path = 'D:/project/Python/PDL_Python/quan/Incoherent_img'

'''------------------------------------代码---------------------------------'''
Incoherent_img = numpy.zeros([picture_hight, picture_width])
color_list = [225, 200, 175, 150, 125, 100, 75, 50, 25, 0]

for i in range(picture_hight):
    for j in range(picture_width):
        Incoherent_img[i][j] = 255
cv2.imwrite(Incoherent_output_path+ '/img0.png', Incoherent_img)

def change_color(Row, Cloumn, color_number):
    for i in range(Row * 10, Row * 10 + 10):
        for j in range(Cloumn * 10, Cloumn * 10 + 10):
            Incoherent_img[i][j] = color_list[color_number]

def create_img(pixel_list):
    color_number = 0
    for i in pixel_list:
        for j in i:
            change_color(j[0], j[1], color_number)
        color_number += 1 

pixel_list = [[], [], [], [], [], [], [], [], [], []]

temporary_list = []
for i in range(11):
    for j in range(11):
        temporary_list.append([i, j])

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

    for j in range(10):
        if j == 0:
            pixel_list[j] = gray_list.copy()
            create_img(pixel_list)
            cv2.imwrite(Incoherent_output_path+ '/img%d' %(i*10+j+1) + '.png', Incoherent_img)
        else:
            pixel_list[j] = pixel_list[j - 1].copy()
            create_img(pixel_list)
            cv2.imwrite(Incoherent_output_path+ '/img%d' %(i*10+j+1) + '.png', Incoherent_img)