import numpy

def gausskernel(r, sigma):
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

E = gausskernel(6, 1.5)
print(E)

'''
能源动力 谢泉生 16:30:44
def gauss(R,C,sigma):
    gauss_array=np.zeros((31,31))
    for i in range(31):
        for j in range(31):
            #R1[i][j]=(i-15)      
            #C1[i][j]=(i-15)
            exponent = (R[i][j]*R[i][j] + C[i][j]*C[i][j]) / (2 * sigma*sigma)
            amplitude = 1 / (sigma * np.sqrt(2 * np.pi))
            gauss_array[i][j] = amplitude * np.exp(-exponent)
    return gauss_array

def gausskernel(sigma,r):
    R1=C1=np.zeros((31,31))
    for i in range(31):
        for j in range(31):
            R1[i][j]=(i-15)      
            C1[i][j]=(i-15)
    gausskernel_array=gauss(R1,C1,sigma)
    gausskernel_array=gausskernel_array[15-r:16+r,15-r:16+r] #只取16-r：16+r
    return gausskernel_array
'''