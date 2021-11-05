import cv2
import numpy
import matplotlib.pyplot

#定义Valid卷积函数
def convolution_Valid(input, kernel):

    input_row, input_column = input.shape
    kernel_row, kernel_column = kernel.shape

    array_new = []
    for i in range(input_row - kernel_row + 1):
        array_new_row = []
        for j in range(input_column - kernel_column + 1):
            array1 = input[i : i + kernel_row, j : j + kernel_column]
            array_new_row.append(numpy.sum(numpy.multiply(array1, kernel)))
        array_new.append(array_new_row)

    return numpy.array(array_new)

#主函数
def main():
    pass

#测试函数
def test():
    image1 = cv2.imread('D:/Project/Python/PDL_Python/Convolution/test.png', cv2.IMREAD_GRAYSCALE)

    #定义卷积核
    #在numpy.array后加“\”为了换行美观，不加会出错
    kernel1 = numpy.array\
    ([
        [1,0,-1],
        [1,0,-1],
        [1,0,-1],
    ])

    image2 = convolution_Valid(image1, kernel1)

    '''两种显示图片的方式'''
    '''CV2中显示图片，但是矩阵需要保存然后在读取才能显示'''
    # cv2.imshow('image1', image1)

    # cv2.imwrite('D:/Project/Python/PDL_Python/Convolution/test1.png', image2)
    # image2 = cv2.imread('D:/Project/Python/PDL_Python/Convolution/test1.png')
    # cv2.imshow('image2', image2)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    '''matplotlib.pyplot显示图片'''
    matplotlib.pyplot.subplot(121)
    matplotlib.pyplot.axis('off')
    matplotlib.pyplot.imshow(image1, cmap='gray')

    matplotlib.pyplot.subplot(122)
    matplotlib.pyplot.axis('off')
    matplotlib.pyplot.imshow(image2, cmap='gray')

    matplotlib.pyplot.show()

#测试用
if __name__ == '__main__':
    test()