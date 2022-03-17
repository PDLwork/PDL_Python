import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

#准备的测试集
test_set = torchvision.datasets.CIFAR10(root="./dataset", train=False, download=True, transform=torchvision.transforms.ToTensor())

# 常用参数：
# dataset:数据集      batch_size：一次取多少张图片      shuffle：是否随机取
# num_workers：暂时忘了            drop_last：为True时如果不整除是否丢掉
#应该是不会取同样的照片吧 内部逻辑应该是先打乱然后逐渐取完
test_dataloader = DataLoader(dataset=test_set, batch_size=64, shuffle=True,num_workers=0, drop_last=False)


#这个使用方法是有点奇怪
# i = 0
# for data in test_dataloader:
#     img, target = data  #这时的img并不是单张图片，而是四张图片了，和设置的batch_size有关
#     print(img.shape)
#     print(target)
#     i = i + 1
#     if i > 10:
#         break


#和tensorboard联合调试
Writer = writer = SummaryWriter('logs')
step = 0
for data in test_dataloader:
    imgs, target = data  #这时的imgs并不是单张图片，而是64张图片了，和设置的batch_size有关
    writer.add_images("dataloader", imgs, step) #注意是add_images
    step += 1
Writer.close()