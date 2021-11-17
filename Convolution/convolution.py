import cv2
import numpy
import matplotlib.pyplot
import time
from numba import jit

# start = time.time()
# end = time.time()
# print(str(end - start))

#定义Valid卷积函数
def convolution_Valid(input, kernel):
    #读取卷积核和被输入矩阵的长宽
    input_row, input_column = input.shape
    kernel_row, kernel_column = kernel.shape

    #创建列表用于存储卷积后的矩阵
    array_new = []

    for i in range(input_row - kernel_row + 1):
        array_new_row = []      #创建列表用于存放矩阵每行的内容
        for j in range(input_column - kernel_column + 1):
            array1 = input[i : i + kernel_row, j : j + kernel_column]       #提取出当前卷积的小矩阵
            array_new_row.append(numpy.sum(array1 * kernel))
        array_new.append(array_new_row)

    return numpy.array(array_new)       #返回卷积后的矩阵

#定义Same卷积函数
def Convolution_Same(input, kernel):
    #读取卷积核和被输入矩阵的长宽
    input_row, input_column = input.shape
    kernel_row, kernel_column = kernel.shape

    #周围填充0
    input = numpy.pad(input, ((kernel_row // 2, kernel_column // 2), (kernel_row // 2, kernel_row // 2)), 'constant', constant_values=0)

    #创建列表用于存储卷积后的矩阵
    array_new = []

    for i in range(input_row):
        array_new_row = []      #创建列表用于存放矩阵每行的内容
        for j in range(input_column):
            array1 = input[i:i + kernel_row, j:j + kernel_column]
            array_new_row.append(numpy.sum(array1 * kernel))
        array_new.append(array_new_row)

    return numpy.array(array_new)

#主函数
def main():
    pass

#测试函数
def test():
    image1 = cv2.imread('D:/Project/python/PDL_Python/Convolution/test3.png', cv2.IMREAD_GRAYSCALE)

    #定义卷积核
    #在numpy.array后加“\”为了换行美观，不加会出错
    #垂直检测
    kernel1 = numpy.array\
    ([
        [1,0,-1],
        [1,0,-1],
        [1,0,-1],
    ])

    #水平检测
    kernel2 = numpy.array\
    ([
        [ 1, 1, 1],
        [ 0, 0, 0],
        [-1,-1,-1],
    ])

    #边缘检测
    kernel3 = numpy.array\
    ([
        [-1,-1,-1],
        [-1, 8,-1],
        [-1,-1,-1],
    ])

    convolution_image1 = Convolution_Same(image1, kernel1)
    convolution_image2 = Convolution_Same(image1, kernel2)
    convolution_image3 = Convolution_Same(image1, kernel3)

    '''两种显示图片的方式'''
    '''CV2中显示图片，但是矩阵需要保存然后在读取才能显示'''
    # cv2.imshow('image1', image1)

    # cv2.imwrite('D:/Project/Python/PDL_Python/Convolution/test1.png', image2)
    # image2 = cv2.imread('D:/Project/Python/PDL_Python/Convolution/test1.png')
    # cv2.imshow('image2', image2)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    '''matplotlib.pyplot显示图片'''
    matplotlib.pyplot.subplot(221)      #切割位置
    matplotlib.pyplot.axis('off')       #关闭坐标轴
    matplotlib.pyplot.imshow(image1, cmap='gray')

    matplotlib.pyplot.subplot(223)
    matplotlib.pyplot.axis('off')
    matplotlib.pyplot.imshow(convolution_image1, cmap='gray')

    matplotlib.pyplot.subplot(222)
    matplotlib.pyplot.axis('off')
    matplotlib.pyplot.imshow(convolution_image2, cmap='gray')

    matplotlib.pyplot.subplot(224)
    matplotlib.pyplot.axis('off')
    matplotlib.pyplot.imshow(convolution_image3, cmap='gray')

    matplotlib.pyplot.show()

#测试用
if __name__ == '__main__':
    test()