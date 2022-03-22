import torch
import torchvision

vgg16 = torchvision.models.vgg16(pretrained=False)

#保存方式1  占用空间大 而且这种方式有陷阱 自己的模型读取时需要导入
torch.save(vgg16, "vgg16_method1.pth")

#方式2  这种方式只保存参数 不保存网络结构（官方推荐） 但是大小也差不多啊  有这么大？
torch.save(vgg16.state_dict(), "vgg16_method2.pth")

