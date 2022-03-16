import torchvision
from torch.utils.tensorboard import SummaryWriter

'''#############################################################################################################'''
#测试下载以及最基础的使用
# train_set = torchvision.datasets.CIFAR10(root="./dataset", train=True, download=True)
# test_set = torchvision.datasets.CIFAR10(root="./dataset", train=False, download=True)

# print(train_set[0])
# print(train_set.classes)

# img, target = train_set[10]
# print(img)
# print(target)
# print(train_set.classes[target])

# img.show()

'''#############################################################################################################'''
#增加将PIL转换成Tensor形式
tensor_ToTensor = torchvision.transforms.ToTensor()

train_set = torchvision.datasets.CIFAR10(root="./dataset", train=True, download=True, transform=tensor_ToTensor)
test_set = torchvision.datasets.CIFAR10(root="./dataset", train=False, download=True, transform=tensor_ToTensor)

# print(test_set[0])
writer = SummaryWriter('logs')

for i in range(10):
    img, target = test_set[i]
    writer.add_image("img", img, i)

writer.close()