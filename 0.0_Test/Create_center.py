import cv2
import numpy

'''----------------------------------输入参数-------------------------------'''
'''10的倍数'''
picture_width = 80
picture_hight = 60
'''0—1'''
P = 0.5

'''------------------------------------代码---------------------------------'''
img = numpy.zeros([picture_hight, picture_width])

for i in range(picture_hight):
    for j in range(picture_width):
        img[i][j] = 255

black_width = int(picture_width * P)
black_hight = int(picture_hight * P)

# if black_width % 2 == 1:
#     black_width += 1
# if black_hight % 2 == 1:
#     black_hight += 1

for i in range((picture_hight // 2 - black_hight // 2), (picture_hight // 2 - black_hight // 2 + black_hight)):
    for j in range((picture_width // 2 - black_width // 2), (picture_width // 2 - black_width // 2 + black_width)):
        img[i][j] = 0

cv2.imwrite('F:/Project/PDL_Python/0.0_First/test.png', img)