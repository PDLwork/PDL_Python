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
# from torch.utils.tensorboard import SummaryWriter
# writer = SummaryWriter('logs')

# '''使用writer.__add啥啥啥的就生成一个类似于日志文件的东西，然后就可以在TenserBoard中展示出来'''
# #第三个参数为步骤，执行时可以拖动不同步骤看图片？
# writer.add_image("test", img2, 2, dataformats='HWC')
# # y = x
# for i in range(100):
#     writer.add_scalar('y = 2x', 2*i, i)

# writer.close()


'''###################################################################################################################'''
'''learn transforms'''
'''主要是对图片进行一些变换'''
'''常用工具：
totensor：转换成tensor
resize：改变大小'''
from torchvision import transforms

#先创建一个类对象
tensor_train = transforms.ToTensor()
tensor_img = tensor_train(img1)
print(type(tensor_img))