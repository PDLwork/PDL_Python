import torch
import torchvision

#太大了不给下  download命令无法使用
# train_data = torchvision.datasets.ImageNet(root='./imagenet_dataset', split='train', download=True, transform=torchvision.transforms.ToTensor())

#这个操作实际上就是人家的网络下载下来，而且可以选择是否下载训练好的参数
vgg16_false = torchvision.models.vgg16(pretrained=False)
vgg16_true = torchvision.models.vgg16(pretrained=True)  #当pretrained为True时，即下载之前训练好的权值

# print(vgg16_true)     #打印看看网络模型


#在整体网络后面加上一个线性层
# vgg16_true.add_module('add_linear', torch.nn.Linear(1000, 10))
# print(vgg16_true)


#在其中一个模块加上线性层
# vgg16_true.classifier.add_module('add_linear', torch.nn.Linear(1000, 10))
# print(vgg16_true)


#或者可以修改原来模型  序号这里我更改了，注意一下
# vgg16_true.classifier[7] = torch.nn.Linear(4096, 10)
# print(vgg16_true)