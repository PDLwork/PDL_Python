import cv2
import numpy as np
import math
from array_test import array_print_excel
'''

Max_delay = 2;
LGMD_OutputS = zeros(length(sigma_E),FrameEnd_Num-Max_delay-1);
FFI = zeros(length(sigma_E),FrameEnd_Num-Max_delay-1);
Threshold_Pnt = zeros(length(sigma_E),1);
kernalG = ones(4,4);
a = 1.2
Thresh_G_0 = 0.5;

sigma_E = 1.5
sigma_I = 5
r = 6;
alfa = -0.1
beta = 0.5
lamda = 0.7

'''

#高斯核
def gauss(R,C,sigma):
    gauss_array=np.zeros((31,31))
    for i in range(31):
        for j in range(31):
            #R1[i][j]=(i-15)      
            #C1[i][j]=(i-15)
            exponent = (R[i][j]**2 + C[i][j]**2) / (2 * sigma**2)
            amplitude = 1 / (sigma * np.sqrt(2 * np.pi))
            gauss_array[i][j] = amplitude * np.exp(-exponent)
    return gauss_array

def gausskernel(sigma,r):
    R1=np.zeros((31,31))
    C1=np.zeros((31,31))
    for i in range(31):
        for j in range(31):
            R1[i][j]=(i-15)      
            C1[i][j]=(j-15)
    gausskernel_array=gauss(R1,C1,sigma)
    gausskernel_array=gausskernel_array[15-r:16+r,15-r:16+r] #只取16-r：16+r
    return gausskernel_array

#时间常数tau
def Calc_tau(r,alfa,beta,lamda):
    tau = np.zeros((2*r+1,2*r+1))
    x=[i for i in range(-r,r+1)]
    y=[i for i in range(-r,r+1)]
    for i in range(0,2*r+1):
        for j in range(0,2*r+1):
            tau[i][j]= alfa + 1/(beta+ math.exp(-((x[i]*lamda*x[i]*lamda)+(y[j]*lamda*y[j]*lamda))))
            if tau[i][j]<1 :
                tau[i][j]=0
    Calc_tau = tau
    return Calc_tau
#卷积函数
def conv(data,k,r):
    #n,m=data.shape 为什么这个函数不可以使用？
    img_new=[] 
    #填充
    data = np.pad(data, ((r, r), (r, r)), 'constant', constant_values=0) 
    n = len(data)
    m = len(data[0])
    for i in range(n-2*r):
        line=[]
        for j in range(m-2*r):
            a=data[i:i+2*r+1,j:j+2*r+1]
            res=np.multiply(a,k)
#if res > 255:
    #res=255
#elif res<0:
    #res=0
#else:
    #res=res
            line.append(np.sum(res))
        img_new.append(line)
    return np.array(img_new)
#取值
Sigma_E = 1.5
Sigma_I = 5
r = 6
alfa = -0.1
beta = 0.5
lamda = 0.7
a = 1.2
Thresh_G_0 = 0.5
FilePath = 'F:/00_Code/picture/vtpgray/diff'
    #计算D-LGMD**
tau = Calc_tau(r,alfa,beta,lamda)

#S=E-aI
Tempkernel =gausskernel(Sigma_E,r)-a*gausskernel(Sigma_I,r)
kernel_E = gausskernel(Sigma_E,r)
array_print_excel(kernel_E)
    #kernel_E(tau < 1) = Tempkernel(tau < 1)# kernel_E(ht>1) = 0;kernel_E(kernel_E<0) = 0;
for i in range(2*r+1):
    for j in range(2*r+1):
        if tau[i][j]<1:
            kernel_E[i][j]=Tempkernel[i][j]
        if (tau[i][j]>1) or (kernel_E[i][j]<0):
            kernel_E[i][j]=0
#Showkerne_E=np.round(kernel_E * 100)
#Showkerne_E=Showkerne_E.astype(int)

    #kernel_I = a *  gausskernel(Sigma_I, r)
    #kernel_I=np.where(tau < 1,0,kernel_I) 
kernel_I =a*gausskernel(Sigma_I, r)
kernel_I_delay1=np.zeros((len(kernel_I),len(kernel_I[0])))
for i in range(2*r+1):
    for j in range(2*r+1):
        if tau[i][j]<1:
            kernel_I[i][j]=0
        kernel_I_delay1[i][j] = kernel_I[i][j]
for i in range(2*r+1):
    for j in range(2*r+1):
        if (tau[i][j]<1) or (tau[i][j]>1.8999):
            kernel_I_delay1[i][j]=0       
#Showkernel_I_delay1 = np.round(kernel_I_delay1 * 100)
#Showkernel_I_delay1=Showkernel_I_delay1.astype(int)
kernel_I_delay2 = kernel_I
    #kernel_I_delay2=np.where(tau < 1.8999,0,kernel_I_delay2)
for i in range(2*r+1):
    for j in range(2*r+1):
        if tau[i][j]<1.8999:
            kernel_I_delay2[i][j]=0
#Showkernel_I_delay2 = np.round(kernel_I_delay2 * 100)
#Showkernel_I_delay2=Showkernel_I_delay2.astype(int)

def main():
    #读取图片
    for x in range(950,954-3) :
        FileName = FilePath+str(x)+'.jpg'
        img0=cv2.imread(str(FileName), cv2.IMREAD_GRAYSCALE)
        img0=img0/255
        FileName = FilePath+str(x+1)+'.jpg'
        img1=cv2.imread(str(FileName), cv2.IMREAD_GRAYSCALE)
        img1=img1/255
        FileName = FilePath+str(x+2)+'.jpg'
        img2=cv2.imread(str(FileName), cv2.IMREAD_GRAYSCALE)
        img2=img2/255
        FileName = FilePath+str(x+3)+'.jpg'
        img3=cv2.imread(str(FileName), cv2.IMREAD_GRAYSCALE)
        img3=img3/255

        img_diff10=np.subtract(img0,img1)
        img_diff20=np.subtract(img1,img2)
        img_diff30=np.subtract(img2,img3)


        img_diff1=np.abs(img_diff10)
        img_diff2=np.abs(img_diff20)
        img_diff3=np.abs(img_diff30)        
#FFI
        FFI=np.sum(img_diff1)
        Thresh_G=min(((FFI/200000)*0.5),0.3)

#卷积前对卷积核float转化为int
   # kernel_E=kernel_E.astype(int)
   # kernel_I_delay1=kernel_I_delay1.astype(int)
   # kernel_I_delay2=kernel_I_delay2.astype(int)
#开始卷积
        Layer_E = conv(img_diff3,kernel_E,r)
        Layer_I_delay1 = conv(img_diff2,kernel_I_delay1,r)
        Layer_I_delay2 = conv(img_diff1,kernel_I_delay2,r)
        Layer_I = np.add(Layer_I_delay1 , Layer_I_delay2) #delay0 has been involved to kernal E.

        Layer_S = np.subtract(Layer_E,Layer_I)
        n = len(Layer_S)
        m = len(Layer_S[0])
        for i in range(n):
            for j in range(m):
                if Layer_S[i][j]<0:
                    Layer_S[i][j]=0

    #Layer_S=Layer_S.where(Layer_S<0,0,Layer_S)
        #Layer_S=Layer_S.astype(int)
#增强输出G，图像最后处理
        plus=np.ones([5,5], dtype = int)
        Layer_G_Cef=conv(Layer_S,plus,2)
        Layer_G=np.multiply(Layer_S,Layer_G_Cef)
    #Layer_G=np.where(Layer_G < Thresh_G, 0)
    #Layer_G=np.where(Layer_G > 1,1)
        for i in range(2*r+1):
            for j in range(2*r+1):
                if Layer_G[i][j]< Thresh_G:
                    Layer_G[i][j]=0
                if Layer_G[i][j]>1:
                    Layer_G[i][j]=1#化为0和1不好使
        # LGMD_OutputS[x] = sum(Layer_S)
        # LGMD_OutputG[x] = sum(Layer_G)  
#输出s和g层图像
        smax=np.ptp(Layer_S)
        gmax=np.ptp(Layer_G)
        Layer_S=Layer_S*(255/smax)
        Layer_G=Layer_G*(255/gmax)
        # print(Layer_S)
        # print()
        # print(Layer_G)
        cv2.imwrite('s.png',Layer_S)
        imgs=cv2.imread('s.png')
        cv2.namedWindow('s',cv2.WINDOW_AUTOSIZE)
        cv2.imshow('s',imgs)

        cv2.imwrite('g.png',Layer_G)
        imgg=cv2.imread('g.png')
        cv2.namedWindow('g',cv2.WINDOW_AUTOSIZE)
        cv2.imshow('g',imgg)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    #print(Calc_tau(r,alfa,beta,lamda))
