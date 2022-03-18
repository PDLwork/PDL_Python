#注意torch.nn.functional中的conv2d和torch.nn中的conv2d是不一样的
#这个就是普通的卷积，那个卷积是不需要输入卷积核的
import torch
import torch.nn.functional as F

input = torch.tensor([[1, 2, 3, 4, 5, 6],
                      [1, 6, 8, 5, 3, 1],
                      [0, 5, 3, 5, 9, 9],
                      [3, 1, 7, 2, 3, 5],
                      [1, 6, 8, 5, 9, 7]])

kernel = torch.tensor([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])

input = torch.reshape(input, (1, 1, 5, 6))  #conv2需要4参数的形式  所以需要转换  之前只是宽和高2参数
kernel = torch.reshape(kernel, (1, 1, 3, 3)) #tensor4参数形式一般为batch_size，chanels，Hight(行), Whild(列)

'''conv2d输入参数
input：输入图像  kernel：输入卷积核， stride：步长
panding：填充'''
output = F.conv2d(input, kernel, stride=1)
print(output)