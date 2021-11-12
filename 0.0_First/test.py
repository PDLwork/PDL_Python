import cv2
import numpy

def callback():
    pass

img = numpy.zeros((600, 600))

cv2.namedWindow('Test')
cv2.createTrackbar('R', 'Test', 10, 255, callback)
cv2.createTrackbar('B', 'Test', 10, 255, callback)
i = 0

while True:
    r = cv2.getTrackbarPos('R', 'Test')
    g = cv2.getTrackbarPos('B', 'Test')
    print(r, g)
    cv2.imshow('Test', img)
    i += 1
    if i > 10:
        break

cv2.destroyAllWindows()