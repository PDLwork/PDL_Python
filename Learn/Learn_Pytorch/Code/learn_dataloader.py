import torchvision
from torch.utils.data import DataLoader

#准备的测试集
test_set = torchvision.datasets.CIFAR10(root="./dataset", train=False, download=True, transform=torchvision.transforms.ToTensor())

# 常用参数：
# dataset:数据集      batch_size：一次取多少张图片      shuffle：是否随机取
# num_workers：暂时忘了            drop_last：如果不整除是否丢掉
#应该是不会取同样的照片吧
test_dataloader = DataLoader(dataset=test_set, batch_size=4, shuffle=True,num_workers=0, drop_last=False)

#这个使用方法是有点奇怪
# i = 0
# for data in test_dataloader:
#     img, target = data
#     print(img.shape)
#     print(target)
#     i = i + 1
#     if i > 10:
#         break