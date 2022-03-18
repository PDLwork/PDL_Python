from turtle import forward
import torch

input = torch.tensor([[1, 2, 3, 4, 5, 6],
                      [1, 6, 8, 5, 3, 1],
                      [0, 5, 3, 5, 9, 9],
                      [3, 1, 7, 2, 3, 5],
                      [1, 6, 8, 5, 9, 7]], dtype=torch.float32)
input = torch.reshape(input, (1, 1, 5, 6))

class Mynet(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.maxpool1 = torch.nn.MaxPool2d(kernel_size=3, ceil_mode=True)   #ceil_mode为True就是将数据保留,而且池化只能对浮点数进行处理，所以一开始需要设置成浮点数

    def forward(self, input):
        output = self.maxpool1(input)
        return output

test = Mynet()
output = test(input)
print(output)