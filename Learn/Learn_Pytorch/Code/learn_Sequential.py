import torch

class Mynet(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=5, padding=2)
        self.maxpool1 = torch.nn.MaxPool2d(2)
        self.conv2 = torch.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=5, padding=2)
        self.maxpool2 = torch.nn.MaxPool2d(2)
        self.conv3 = torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, padding=2)
        self.maxpool3 = torch.nn.MaxPool2d(2)
        self.faltten = torch.nn.Flatten()
        self.linear1 = torch.nn.Linear(1024, 64)
        self.linear2 = torch.nn.Linear(64, 10)

    def forward(self, input):
        input = self.conv1(input)
        input = self.maxpool1(input)
        input = self.conv2(input)
        input = self.maxpool2(input)
        input = self.conv3(input)
        input = self.maxpool3(input)
        input = self.faltten(input)
        input = self.linear1(input)
        output = self.linear2(input)
        return output

'''另一种方式'''
class Mynet2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        #实际上就是一个组合
        self.Mymodule = torch.nn.Sequential(
            torch.nn.Conv2d(in_channels=3, out_channels=32, kernel_size=5, padding=2),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=5, padding=2),
            torch.nn.MaxPool2d(2),
            torch.nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, padding=2),
            torch.nn.MaxPool2d(2),
            torch.nn.Flatten(),
            torch.nn.Linear(1024, 64),
            torch.nn.Linear(64, 10)
        )

    def forward(self, input):
        output = self.Mymodule(input)
        return output

'''用于调试网络写对了没'''
Test = Mynet2()
input = torch.ones((64, 3, 32, 32))
output = Test(input)
print(output.shape)