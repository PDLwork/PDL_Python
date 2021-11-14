import tkinter
import math
import cv2
import numpy
import matplotlib.pyplot
from array_test import array_print_excel

'''-------------------------初始参数设计-------------------------'''
sigma_E = 1.5
sigma_I = 5
r = 6
a = 1.2
alfa = -0.1
beta = 0.5
lamda = 0.7
FilePath = 'D:/project/LGMDVideo/Picture/hi'

'''-------------------------D-LGMD函数部分-------------------------'''
#gauss_kernel
def gausskernel(sigma, r):
    Array1 = numpy.zeros((31, 31))
    Array2 = numpy.zeros((31, 31))
    gauss_array = numpy.zeros((31, 31))

    for i in range(31):
        for j in range(31):
            Array1[i][j]=(i - 15)
            Array2[i][j]=(j - 15)
            exponent = -(Array1[i][j] ** 2 + Array2[i][j] ** 2) / (2 * sigma ** 2)
            amplitude = 1 / (sigma * numpy.sqrt(2 * numpy.pi))
            gauss_array[i][j] = amplitude * numpy.exp(exponent)

    gausskernel_array = gauss_array[15-r:16+r, 15-r:16+r] #只取16-r：16+r

    return gausskernel_array

#Time时间常数---tau(可改进)
def Calc_tau(r,alfa,beta,lamda):
    tau_array = numpy.zeros((2*r+1,2*r+1))
    x=[i for i in range(-r,r+1)]
    y=[i for i in range(-r,r+1)]
    for i in range(0,2*r+1):
        for j in range(0,2*r+1):
            tau_array[i][j]= alfa + 1/(beta+ math.exp(-((x[i]*lamda*x[i]*lamda)+(y[j]*lamda*y[j]*lamda))))
            if tau_array[i][j] < 1 :
                tau_array[i][j]=0
    return tau_array

#卷积函数
def Convolution_same(data,k,r):
    img_new=[] 
    #填充
    data = numpy.pad(data, ((r, r), (r, r)), 'constant', constant_values=0) 
    n = len(data)
    m = len(data[0])
    for i in range(n-2*r):
        line=[]
        for j in range(m-2*r):
            a=data[i:i+2*r+1,j:j+2*r+1]
            res=numpy.multiply(a,k)
#if res > 255:
    #res=255
#elif res<0:
    #res=0
#else:
    #res=res
            line.append(numpy.sum(res))
        img_new.append(line)
    return numpy.array(img_new)

#D-LGMD主程序
def main():
    #根据参数生成卷积核s
    tau = Calc_tau(r, alfa, beta, lamda)
    kernel_E = gausskernel(sigma_E, r)
    kernel_I = a*gausskernel(sigma_I, r)
    Tempkernel = kernel_E - kernel_I        #E-I

    #对kernel_E处理
    for i in range(2*r+1):
        for j in range(2*r+1):
            if tau[i][j]<1:
                kernel_E[i][j]=Tempkernel[i][j]
            if (tau[i][j]>1) or (kernel_E[i][j]<0):
                kernel_E[i][j]=0

    #对kernel_I处理，并生成kernel_I_delay1和kernel_I_delay2
    kernel_I_delay1 = numpy.zeros((len(kernel_I),len(kernel_I[0])))
    for i in range(2*r+1):
        for j in range(2*r+1):
            if tau[i][j]<1:
                kernel_I[i][j]=0
            kernel_I_delay1[i][j] = kernel_I[i][j]
    for i in range(2*r+1):
        for j in range(2*r+1):
            if (tau[i][j]<1) or (tau[i][j]>1.8999):
                kernel_I_delay1[i][j]=0
    kernel_I_delay2 = kernel_I
    for i in range(2*r+1):
        for j in range(2*r+1):
            if tau[i][j]<1.8999:
                kernel_I_delay2[i][j]=0

    #读取图片并处理
    for x in range(950,954-3):
        #获取四张图片并将其归一化
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

        #图片做差
        img_diff10=numpy.subtract(img0,img1)
        img_diff20=numpy.subtract(img1,img2)
        img_diff30=numpy.subtract(img2,img3)

        #取绝对值
        img_diff1=numpy.abs(img_diff10)
        img_diff2=numpy.abs(img_diff20)
        img_diff3=numpy.abs(img_diff30)   

        #FFI
        FFI = numpy.sum(img_diff1)
        Thresh_G = min(((FFI/200000)*0.5),0.3)

        #卷积
        Layer_E = Convolution_same(img_diff3,kernel_E,r)
        Layer_I_delay1 = Convolution_same(img_diff2,kernel_I_delay1,r)
        Layer_I_delay2 = Convolution_same(img_diff1,kernel_I_delay2,r)
        Layer_I = numpy.add(Layer_I_delay1 , Layer_I_delay2) #delay0 has been involved to kernal E.

        #得到S层输出并处理
        Layer_S = numpy.subtract(Layer_E,Layer_I)
        n = len(Layer_S)
        m = len(Layer_S[0])
        for i in range(n):
            for j in range(m):
                if Layer_S[i][j]<0:
                    Layer_S[i][j]=0
        
        #对S层增强得到G层并处理
        plus=numpy.ones([5,5], dtype = int)
        Layer_G_Cef=Convolution_same(Layer_S,plus,2)
        Layer_G=numpy.multiply(Layer_S,Layer_G_Cef)
        for i in range(2*r+1):
            for j in range(2*r+1):
                if Layer_G[i][j]< Thresh_G:
                    Layer_G[i][j]=0
                if Layer_G[i][j]>1:
                    Layer_G[i][j]=1

        #处理矩阵符合灰度图定义
        smax = numpy.ptp(Layer_S)       #求出矩阵中最大值将其设置为255
        gmax = numpy.ptp(Layer_G)
        Layer_S = Layer_S*(255/smax)
        Layer_G = Layer_G*(255/gmax)

        #打印原图、S层和G层
        matplotlib.pyplot.subplot(211)
        matplotlib.pyplot.title('Original image')
        matplotlib.pyplot.axis('off')
        matplotlib.pyplot.imshow(cv2.imread(str(FilePath+str(x+3)+'.jpg'), cv2.IMREAD_GRAYSCALE), cmap='gray')

        matplotlib.pyplot.subplot(223)
        matplotlib.pyplot.title('Output S')
        matplotlib.pyplot.axis('off')
        matplotlib.pyplot.imshow(Layer_S, cmap='gray')

        matplotlib.pyplot.subplot(224)
        matplotlib.pyplot.title('Output G')
        matplotlib.pyplot.axis('off')
        matplotlib.pyplot.imshow(Layer_G, cmap='gray')

        matplotlib.pyplot.show()

        #将S层和G层保存
        # cv2.imwrite('s.png',Layer_S)
        # cv2.imwrite('g.png',Layer_G)

'''-------------------------调试窗口部分-------------------------'''
def GUI_design():
    Window_Tool = tkinter.Tk()      #创建调参的窗口
    Window_Tool.title('Window_Tool')    #设置窗口名字
    Window_Tool.geometry('300x650+0+50')    #设置窗口大小和放置位置

    #设置sigma_E滑动条并放置（参数设置参考使用手册）
    Scale_sigma_E = tkinter.Scale(Window_Tool,\
                        from_=1,\
                        to=5,\
                        resolution=0.1,\
                        length=300,\
                        label='sigma_E',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_sigma_E.set(sigma_E)
    Scale_sigma_E.pack()

    #设置sigma_I滑动条并放置
    Scale_sigma_I = tkinter.Scale(Window_Tool,\
                        from_=1.0,\
                        to=5.0,\
                        resolution=0.1,\
                        length=300,\
                        label='sigma_I',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_sigma_I.set(sigma_I)
    Scale_sigma_I.pack()

    #设置r滑动条并放置
    Scale_r = tkinter.Scale(Window_Tool,\
                        from_=1,\
                        to=7,\
                        resolution=1,\
                        length=300,\
                        label='r',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_r.set(r)
    Scale_r.pack()

    #设置a滑动条并放置
    Scale_a = tkinter.Scale(Window_Tool,\
                        from_=1.0,\
                        to=3.0,\
                        resolution=0.1,\
                        length=300,\
                        label='a',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_a.set(a)
    Scale_a.pack()

    #设置alfa滑动条并放置
    Scale_alfa = tkinter.Scale(Window_Tool,\
                        from_=-1.0,\
                        to=2.0,\
                        resolution=0.1,\
                        length=300,\
                        label='alfa',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_alfa.set(alfa)
    Scale_alfa.pack()

    #设置beta滑动条并放置
    Scale_beta = tkinter.Scale(Window_Tool,\
                        from_=-1.0,\
                        to=2.0,\
                        resolution=0.1,\
                        length=300,\
                        label='beta',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_beta.set(beta)
    Scale_beta.pack()

    #设置lamda滑动条并放置
    Scale_lamda = tkinter.Scale(Window_Tool,\
                        from_=-1.0,\
                        to=2.0,\
                        resolution=0.1,\
                        length=300,\
                        label='lamda',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_lamda.set(lamda)
    Scale_lamda.pack()

    #点击按钮激活函数
    #用于调试判断gui有没有问题，执行到最后调用LGMD_main函数
    #获取滑动条数值并全局共享
    def hit_Button_Run():
        global sigma_E
        global sigma_I
        global r
        global a
        global alfa
        global beta
        global lamda
        sigma_E = Scale_sigma_E.get()
        sigma_I = Scale_sigma_I.get()
        r = Scale_r.get()
        a = Scale_a.get()
        alfa = Scale_alfa.get()
        beta = Scale_beta.get()
        lamda = Scale_lamda.get()
        main()

    #设计按钮并放置
    Button_Run = tkinter.Button(Window_Tool,\
                            text='run',\
                            font=('Arial', 12),\
                            width=10,\
                            height=1,\
                            command=hit_Button_Run)
    Button_Run.pack()

    #窗口循环显示
    Window_Tool.mainloop()

if __name__ == '__main__':
    GUI_design()