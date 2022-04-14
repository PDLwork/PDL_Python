import numpy
import math

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
            line.append(numpy.sum(res))
        img_new.append(line)
    return numpy.array(img_new)

def create_kernel(sigma_E, sigma_I, r, a, alfa, beta, lamda):
    #根据参数生成卷积核
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
    
    return kernel_E, kernel_I_delay1, kernel_I_delay2