import torch
import torchvision
from torch.utils.data import DataLoader

test_set = torchvision.datasets.CIFAR10(root="./dataset", train=False, download=True, transform=torchvision.transforms.ToTensor())
test_dataloader = DataLoader(dataset=test_set, batch_size=64, shuffle=True,num_workers=0, drop_last=False)

class MyModel(torch.nn.Module):
    def __init__(self):
        super().__init__() #用子类对象调用父类已被覆盖的方法 好像就是说将父类的优先级调高，可以参考菜鸟教程
        self.conv1 = torch.nn.Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)
    
    def forward(self, input):   #注意这个forward，换成别的函数名不行，其内部调用了__call__的方法,所以在下面可以直接使用
        output = self.conv1(input)
        return output

test = MyModel()
i = 0

for data in test_dataloader:
    i += 1
    imgs, target = data
    output = test(imgs)
    print(imgs.shape)
    print(output.shape)
    if i == 1:
        break