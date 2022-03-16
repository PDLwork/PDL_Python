'''###################################################################################################################'''
'''learn dataset
功能：检索数据集？
'''
from torch.utils.data import Dataset
import cv2
import os
import numpy

class MyDataSet(Dataset):     #子承父类
    '''
    root_dir:图片根目录 label的上一级 训练集地址
    lable_dir：标签目录如蚂蚁的文件夹 标签地址
    '''
    def __init__(self, root_dir, lable_dir):
        self.root_dir = root_dir
        self.label_dir = lable_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path)   #实际上是获取到一个标签的数据集下的图片的列表
    
    #根据索引来获取相应对象，如图片
    def __getitem__(self, idx):
        img_name = self.img_path[idx]   #根据上面得到的图片列表根据索引获取图片名字
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = img = cv2.imread(img_item_path, cv2.IMREAD_COLOR) #读取图片
        label = self.label_dir  #读取标签
        return img, label

    def __len__(self):
        return len(self.img_path)

root_dir = 'Data\\test\\train'
ants_lable_dir = 'ants_image'
bees_lable_dir = 'bees_image'

ants_dataset = MyDataSet(root_dir, ants_lable_dir)
bees_dataset = MyDataSet(root_dir, bees_lable_dir)
img1, label1 = ants_dataset[2]
img2, label2 = bees_dataset[2]

# print(type(img1))
# print(img1.shape)

'''可以将两个数据集加起来，长度就是加起来的长度，索引也会发生相应改变，加在后面'''
# train_dataset = ants_dataset + bees_dataset
# img2, label2 = train_dataset[124]

# cv2.imshow('test1', img1)
# cv2.imshow('test2', img2)


# cv2.waitKey(0)
# cv2.destroyAllWindows()


'''###################################################################################################################'''
'''learn tensorboard  SummaryWriter'''
'''功能：生成事件文件? 可以绘制曲线 也可以显示图片
好像可以用来观察每个阶段的显示，就可以不用保存每个步骤？'''
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter('logs')

# '''使用writer.__add啥啥啥的就生成一个类似于日志文件的东西，然后就可以在TenserBoard中展示出来'''
# #第三个参数为步骤，执行时可以拖动不同步骤看图片？
# writer.add_image("test", img2, 2, dataformats='HWC')      #dataformats='HWC' 是根据你输入的数据形式决定的 这里是用cv2读取的 也可以添加tensor型的就不需要指定了
# # y = x
# for i in range(100):
#     writer.add_scalar('y = 2x', 2*i, i)

# writer.close()


'''###################################################################################################################'''
'''learn transforms'''
'''主要是对图片进行一些变换,下面是一些常用工具的展示'''
from torchvision import transforms

writer.add_image("img", img1, dataformats='HWC')    #显示初始图片

#ToTensor  将array或者pil读取的图片转换成tensor
# 先创建一个类对象
tensor_ToTensor = transforms.ToTensor()
img_ToTensor = tensor_ToTensor(img1)     #转换
writer.add_image("ToTensor_img", img_ToTensor)      #显示转换成tensor的图片


#normalize 归一化
tensor_Normalize = transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])   #需要输入均值与标准差 三通道所以需要三个
img_Normalize = tensor_Normalize(img_ToTensor)
'''output[channel] = (input[channel] - mean[channel]) / std[channel]'''
writer.add_image("Normalize_img", img_Normalize)       #显示标准化后的图片


#resize：改变图片大小 只能改变pil形式或者tensor的？好像不能改变array形式的矩阵
#输入的是什么类型，返回的就是什么类型的
tensor_Resize = transforms.Resize((256, 256))       #如果只有一个参数的话那就是等比缩放（具体缩放的是那个边？）
img_Resize = tensor_Resize(img_ToTensor)
writer.add_image("Resize_img", img_Resize)          #显示改变后大小的图片


#Compose 中心取样在转换成tensor
#传入参数就是之前写的函数
tensor_Resize_2 = transforms.Resize(512)
tensor_Compose = transforms.Compose([tensor_ToTensor, tensor_Resize_2])   #比如这里先转换成tensor在缩放
img_Resize_2 = tensor_Compose(img1)
writer.add_image("Resize_img", img_Resize_2, 1)     #在上述通道显示复合函数使用后的图片


writer.close()