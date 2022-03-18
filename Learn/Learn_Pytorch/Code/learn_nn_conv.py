'''nn.conv2d中的卷积是不用输入卷积核的'''
import torch
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

test_set = torchvision.datasets.CIFAR10(root="./dataset", train=False, download=True, transform=torchvision.transforms.ToTensor())
test_dataloader = DataLoader(dataset=test_set, batch_size=64, shuffle=True,num_workers=0, drop_last=False)
writer = SummaryWriter('logs')

class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__() #用子类对象调用父类已被覆盖的方法 好像就是说将父类的优先级调高，可以参考菜鸟教程
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)
    
    def forward(self, input):   #注意这个forward，换成别的函数名不行，其内部调用了__call__的方法,所以在下面可以直接使用
        output = self.conv1(input)
        return output

test = MyModel()

step = 0
for data in test_dataloader:
    imgs, target = data
    output = test(imgs)
    writer.add_images("input", imgs, step)
    output = torch.reshape(output, (-1, 3, 30, 30))     #将output的trnsor的形状改变 -1是自适应，这里就把64个batch改成128个
    writer.add_images("output", output, step)
    step += 1

writer.close()