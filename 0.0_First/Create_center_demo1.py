import cv2
import numpy

'''----------------------------------输入参数-------------------------------'''
'''10的倍数'''
picture_width = 110
picture_hight = 110
output_path = 'F:/Project/img'

'''------------------------------------代码---------------------------------'''
pixel_list = [200, 150, 100, 50, 0]

img = numpy.zeros([picture_hight, picture_width])

for i in range(picture_hight):
    for j in range(picture_width):
        img[i][j] = 255

for i in range(5):
    for j in range(50, 59):
        for k in range(50, 59):
            img[j][k] = pixel_list[i]
    out_path = output_path + '/img%d' %i + '.png'
    cv2.imwrite(out_path, img)

for i in range(6):
    for j in range(50, 59):
        for k in range(50, 59):
            img[j][k] = pixel_list[i]
    out_path = output_path + '/img%d' %i + '.png'
    cv2.imwrite(out_path, img)