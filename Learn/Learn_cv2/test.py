import numpy as np
import cv2
# import matplotlib.pyplot as plt

# # 图6-1中的矩阵
# img = np.array([
#     [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
#     [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
#     [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
# ], dtype=np.uint8)

# # 用matplotlib存储
# plt.imsave('img_pyplot.jpg', img)

img0 = cv2.imread('E:/934_rgb.jpg', cv2.IMREAD_GRAYSCALE)
img1 = cv2.imread('E:/935_rgb.jpg', cv2.IMREAD_GRAYSCALE)

img = img0 - img1

# 用OpenCV存储
cv2.imwrite('img_cv2.jpg', img)
