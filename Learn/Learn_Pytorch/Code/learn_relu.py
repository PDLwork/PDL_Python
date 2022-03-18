import torch

input = torch.tensor([[1, 2, 3, 4, 5, 6],
                      [-1, 6, 8, 5, 3, 1],
                      [0, -5, 3, 5, 9, 9],
                      [3, 1, -7, 2, 3, 5],
                      [1, 6, -8, -5, -9, -7]])

input = torch.reshape(input, (-1, 1, 5, 6))

class Mynet(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu1 = torch.nn.ReLU(inplace=True)   #参数inplace为True则将原来的的tensor进行改变 是否覆盖的意思  如果不覆盖就得在给一个变量

    def forward(self, input):
        return self.relu1(input)

test = Mynet()
output = test(input)
print(output)