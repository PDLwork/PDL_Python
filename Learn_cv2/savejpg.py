import cv2

img1 = cv2.imread('E:/Project/Python/PDL_Python/Learn_cv2/test.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('E:/Project/Python/PDL_Python/Learn_cv2/test.png')

img3 = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
img3 = cv2.cvtColor(img3,cv2.COLOR_GRAY2RGB)

cv2.imshow('test', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()