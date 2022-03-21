import torch
import torchvision
from torch.utils.data import DataLoader

#还有交叉熵误差示例，一般用于分类   
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

test_set = torchvision.datasets.CIFAR10(root="./dataset", train=False, download=True, transform=torchvision.transforms.ToTensor())
test_dataloader = DataLoader(dataset=test_set, batch_size=10, shuffle=True,num_workers=0, drop_last=False)
test_net = Mynet2() #创建网络
loss = torch.nn.CrossEntropyLoss()  #求误差
optimizer = torch.optim.SGD(test_net.parameters(), lr=0.01)   #随机梯度下降法  一种优化器

for epoch in range(20):
    running_loss = 0.0  #设置一个变量用于存储这一轮循环中的误差总和
    for img, target in test_dataloader:
        optimizer.zero_grad()   #将梯度初始化为0，不然回累计
        output = test_net(img)  #输入求输出，相当于正向传播
        result_loss = loss(output, target)  #求这次的误差
        result_loss.backward()  #这一步实际上是为了求梯度
        optimizer.step()    #开始修正参数
        running_loss = running_loss + result_loss   #误差求和
    print(running_loss)