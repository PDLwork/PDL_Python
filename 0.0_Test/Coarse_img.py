import cv2
import numpy

img = cv2.imread('D:/BaiduNetdiskDownload/ball.png', cv2.IMREAD_UNCHANGED)
print(img.shape)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()