import cv2
import numpy

def callback(x):
    pass

img = numpy.zeros((1, 1))

cv2.namedWindow('Test', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Test', 600, 400)

cv2.createTrackbar('R', 'Test', 10, 255, callback)
cv2.createTrackbar('B', 'Test', 10, 255, callback)
cv2.createTrackbar('g', 'Test', 10, 255, callback)
cv2.createTrackbar('a', 'Test', 10, 255, callback)
cv2.createTrackbar('v', 'Test', 10, 255, callback)
cv2.createTrackbar('x', 'Test', 10, 255, callback)

i = 0

# while True:
#     r = cv2.getTrackbarPos('R', 'Test')
#     g = cv2.getTrackbarPos('B', 'Test')
#     print(r, g)
#     cv2.imshow('Test', img)
#     i += 1
#     if i > 10000:
#         break
cv2.imshow('Test', img)
cv2.waitKey()
cv2.destroyAllWindows()