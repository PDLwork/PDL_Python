'''用CV2的方式'''
import os
from itertools import cycle
import cv2

Picture_Path = 'D:/project/Python/PDL_Python/Video_Turnto_Picture/123'

# 列出frames文件夹下的所有图片
filenames = os.listdir(Picture_Path)
file_number = len(filenames)

# 通过itertools.cycle生成一个无限循环的迭代器，每次迭代都输出下一张图像对象
img_iter = cycle([cv2.imread(os.sep.join([Picture_Path, 'hi%d.jpg' %x])) for x in range(file_number)])

key = 0
while key & 0xFF != ord('p'):
    cv2.imshow('Animation', next(img_iter))
    key = cv2.waitKey(42)

'''matplotlib.pyplot'''
# import matplotlib.pyplot
# import cv2
# import os
# import time
# from itertools import cycle

# Picture_Path = 'D:/project/Python/PDL_Python/Video_Turnto_Picture/123'

# filenames = os.listdir(Picture_Path)

# img_iter = cycle([cv2.imread(os.sep.join([Picture_Path, x]), cv2.IMREAD_GRAYSCALE) for x in filenames])

# fig = matplotlib.pyplot.figure(1)
# matplotlib.pyplot.axis('off')       #关闭坐标轴

# while True:
#     matplotlib.pyplot.imshow(next(img_iter), cmap='gray')
#     matplotlib.pyplot.draw()
#     matplotlib.pyplot.pause(0.5)