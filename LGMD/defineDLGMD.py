import cv2
import numpy as np
import math
#高斯核
def gauss(x,y,sigma):
    exponent = (x*x + y*y) / (2 * sigma*sigma)
    amplitude = 1 / (sigma * np.sqrt(2 * np.pi))
    gauss = amplitude * np.exp(-exponent)
    return gauss
def gausskernel(sigma,r):
    R1, C1  = np.meshgrid(range(-15, 16) ,range(-15,16))
    gausskernel=gauss(R1,C1,sigma)
    gausskernel=gausskernel[15-r:16+r,15-r:16+r] #只取16-r：16+r
    return gausskernel
#S=E-aI
def DOG(a,Sigma_E,Sigma_I,r):
    R1 = np.full(shape=(31,31), fill_value=0)
    C1 = np.full(shape=(31, 31), fill_value=0)
    R2 = np.full(shape=(31, 31), fill_value=0)
    C2 = np.full(shape=(31, 31), fill_value=0)
    DOG=gauss(R1,C1,Sigma_E)-a*gauss(R2,C2,Sigma_I)
    DOG=DOG[15-r:16+r,15-r:16+r] #只取16-r：16+r
    return gausskernel
#**********定义卷积函数***********
def conv(image, kernel, mode='same'):
    if mode == 'fill':  #选择是否进行边缘填充
        h = kernel.shape[0] // 2   #卷积核的列除以2取整
        w = kernel.shape[1] // 2   #卷积核的行除以2取整
        #在原始图像边缘进行填充，常数填充，填数值0，假设原始图像600*600，卷积核大小5*5，则填充后图像大小604*604
        image = np.pad(image, ((h, h), (w, w), (0, 0)), 'constant')  

    #进行卷积运算
    # conv_b = _convolve(image[:, :, 0], kernel)
    # conv_g = _convolve(image[:, :, 1], kernel)
    # conv_r = _convolve(image[:, :, 2], kernel)
    # res = np.dstack([conv_b, conv_g, conv_r])
    res = _convolve(image, kernel)
    return res

def _convolve(image, kernel):
    h_kernel, w_kernel = kernel.shape  #获取卷积核的长宽，也就是行数和列数
    h_image, w_image = image.shape   #获取欲处理图片的长宽

    #计算卷积核中心点开始运动的点，因为图片边缘不能为空
    res_h = h_image - h_kernel + 1
    res_w = w_image - w_kernel + 1

    #生成一个0矩阵，用于保存处理后的图片
    res = np.zeros((res_h, res_w), np.uint8)

    for i in range(res_h):   #行
        for j in range(res_w):   #列
            #image处传入的是一个与卷积核一样大小矩阵，这个矩阵取自于欲处理图片的一部分
            #这个矩阵与卷核进行运算，用i与j来进行卷积核滑动
            res[i, j] = normal(image[i:i + h_kernel, j:j + w_kernel], kernel)

    return res
def normal(image, kernel):
    #np.multiply()函数：数组和矩阵对应位置相乘，输出与相乘数组/矩阵的大小一致（点对点相乘）
    
    res = np.multiply(image, kernel).sum() #点对点相乘后进行累加
    if res > 255:
        return 255
    elif res<0:
        return 0
    else:
        return res
#时间常数tau
def Calc_tau(r,alfa,beta,lamda):
    tau = np.zeros(shape=(2*r+1,2*r+1))
    for x in range(-r,r+1):
        for y in range(-r,r+1):
            tau[x][y]= alfa + 1/(beta+ math.exp(-((x*lamda)*(x*lamda)+(y*lamda)*(y*lamda))))
    Calc_tau = np.where(tau<1,0,tau)
    return Calc_tau
#定义窗口名称
winName='The Filtered Image'
#定义滑动条回调函数，此处pass用作占位语句保持程序结构的完整性
def nothing(x):
    pass
#***********图像********************
Diff_1=cv2.imread('F:\define LGMD\PHOTO/Diff_1.bmp')
Diff_2=cv2.imread('F:\define LGMD\PHOTO/Diff_2.bmp')
Diff_3=cv2.imread('F:\define LGMD\PHOTO/Diff_3.bmp')
Diff_4=cv2.imread('F:\define LGMD\PHOTO/Diff_4.bmp')
Frame_diff1=abs(Diff_2-Diff_1)
Frame_diff2=abs(Diff_3-Diff_2)
Frame_diff3=abs(Diff_4-Diff_3)
Max_delay = 2

#新建窗口
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)


cv2.imshow('Original IMG',Diff_1)
cv2.waitKey(2000)

#新建7个滑动条，表示颜色时空卷几核的各项参数
cv2.createTrackbar('Sigma_E',winName,20,300,nothing)
cv2.createTrackbar('sigma_I',winName,50,500,nothing)
cv2.createTrackbar('a',winName,0,255,nothing)
cv2.createTrackbar('r',winName,1,9,nothing)
cv2.createTrackbar('alfa',winName,255,255,nothing)
cv2.createTrackbar('beta',winName,255,255,nothing)
cv2.createTrackbar('lamda',winName,255,255,nothing)

while(1):
    #函数cv2.getTrackbarPos()范围当前滑块对应的值
    Sigma_E = cv2.getTrackbarPos('Sigma_E',winName)*0.01
    Sigma_I = cv2.getTrackbarPos('sigma_I',winName)
    a = cv2.getTrackbarPos('a',winName)
    r = cv2.getTrackbarPos('r',winName)
    alfa = cv2.getTrackbarPos('alfa',winName)
    beta = cv2.getTrackbarPos('beta',winName)
    lamda = cv2.getTrackbarPos('lamda',winName)
    #根据参数计算E、I卷积核**
    tau = Calc_tau(r,alfa,beta,lamda)
    # Tempkernel = DOGAnalysis(a, sigma_I/sigma_E , sigma_E, r)
    # kernel_E = GaussAnalysis(sigma_E,r)
    # kernel_E(tau<1) = Tempkernel(tau<1)

    #计算D-LGMD**
    Tempkernel = DOG(a,Sigma_E,Sigma_I,r)
    kernel_E = gausskernel(Sigma_E,r)
    #kernel_E(tau < 1) = Tempkernel(tau < 1)#把tau里小于1的坐标找出来
    Tempkernel = DOG(a,Sigma_E,Sigma_I,r)
    kernel_E = gausskernel(Sigma_E,r)
    #kernel_E(tau < 1) = Tempkernel(tau < 1)#把tau里小于1的坐标找出来
    temporary=np.where(tau<1,0,Tempkernel)
    kernel_E=np.where(tau<1,temporary,kernel_E)
    kernel_E=np.where(tau>1,0,kernel_E)
    kernel_E=np.where(kernel_E < 0,0,kernel_E)
    ttemp=kernel_E * 100
    Showkerne_E = np.round(ttemp)

    kernel_I = a *  gausskernel(Sigma_I, r)
    kernel_I=np.where(tau < 1,0,kernel_I) 
    kernel_I_delay1 = kernel_I

    kernel_I_delay1=np.where(tau < 1 ,0,kernel_I_delay1)
    kernel_I_delay1=np.where(tau > 1.8999 ,0,kernel_I_delay1)
    Showkernel_I_delay1 = np.round(kernel_I_delay1 * 100)

    kernel_I_delay2 = kernel_I
    kernel_I_delay2=np.where(tau < 1.8999,0,kernel_I_delay2)
    Showkernel_I_delay2 = np.round(kernel_I_delay2 * 100)

    FFI=np.sum(np.sum(Frame_diff1))
    Thresh_G=np.min(((FFI/20000)*0.5),0.3)

    Layer_E = conv(Frame_diff3,kernel_E,'same')
    Layer_I_delay1 = conv(Frame_diff2,kernel_I_delay1,'same')
    Layer_I_delay2 = conv(Frame_diff1,kernel_I_delay2,'same')
    Layer_I = Layer_I_delay1 + Layer_I_delay2   #delay0 has been involved to kernal E.
    Layer_S = cv2.absdiff(Layer_E,Layer_I)

    Layer_G_Cef=conv(Layer_S,np.ones([4,4],'same'))
    Layer_G=Layer_S*Layer_G_Cef
    Layer_G=np.where(Layer_G < Thresh_G, 0)
    Layer_G=np.where(Layer_G > 1,1)
    LGMD_OutputS = sum(sum(Layer_S))
    LGMD_OutputG = sum(sum(Layer_G))


    def normalization(data):
        _range = np.max(data) - np.min(data)
        return (data - np.min(data)) / _range

    Normalized_OutS= normalization(LGMD_OutputS)
    Normalized_OutG= normalization(LGMD_OutputG)
    #展示D-LGMD滤波后效果



    cv2.imshow(winName,Diff_3)
    if cv2.waitKey(100)==ord('q'):

        break
cv2.destroyAllWindows()