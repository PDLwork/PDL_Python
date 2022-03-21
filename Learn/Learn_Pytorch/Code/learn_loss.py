import torch
import torchvision

'''
input = torch.tensor([1, 2, 3], dtype=torch.float32)
target = torch.tensor([1, 2, 5], dtype=torch.float32)

input = torch.reshape(input, (1, 1, 1, 3))
target = torch.reshape(target, (1, 1, 1, 3))

loss = torch.nn.L1Loss()    #总差求平均若是loss = torch.nn.L1Loss(reduction='sum')则为求总差距
result = loss(input, target)

loss_mse = torch.nn.MSELoss()  #平方差求平均
result_mes = loss_mse(input, target)

print(result)
print(result_mes)
'''

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
test_dataloader = DataLoader(dataset=test_set, batch_size=64, shuffle=True,num_workers=0, drop_last=False)
torch.uti