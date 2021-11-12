import cv2
import numpy as np

cv2.namedWindow('hhhdt')
img = np.zeros((600,600,3),np.uint8)

def nothing(x):
    pass
cv2.createTrackbar('Sigma_E','hhhdt',1,20,nothing)
cv2.createTrackbar('sigma_I','hhhdt',5,100,nothing)
cv2.createTrackbar('a','hhhdt',0,10,nothing)
cv2.createTrackbar('r','hhhdt',1,9,nothing)
cv2.createTrackbar('alfa','hhhdt',1,10,nothing)
cv2.createTrackbar('beta','hhhdt',1,10,nothing)
cv2.createTrackbar('lamda','hhhdt',1,10,nothing)
#创建一个0和1的转换按钮
#switch = '0 : OFF \n 1 : ON'
cv2.createTrackbar('switch','hhhdt',0,1,nothing) 
flag=True
while(1):
    cv2.imshow('hhhdt',img)
    if  cv2.waitKey(1) == ord('q'):
        break
        pass
    
    Sigma_E = cv2.getTrackbarPos('Sigma_E','hhhdt')
    Sigma_I = cv2.getTrackbarPos('sigma_I','hhhdt')
    a = cv2.getTrackbarPos('a','hhhdt')
    r = cv2.getTrackbarPos('r','hhhdt')
    alfa = cv2.getTrackbarPos('alfa','hhhdt')
    beta = cv2.getTrackbarPos('beta','hhhdt')
    lamda = cv2.getTrackbarPos('lamda','hhhdt')
    switch = cv2.getTrackbarPos('switch','hhhdt')
    if flag :
        if switch==1:
            print(a+r)
            flag=False
