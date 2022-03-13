from torch.utils.data import Dataset
import cv2
import os

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
    
    #根据索引来获取相应值
    def __getitem__(self, idx):
        img_name = self.img_path[idx]   #根据上面得到的图片列表根据索引获取图片名字
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = img = cv2.imread(img_item_path, cv2.IMREAD_COLOR) #读取图片
        label = self.label_dir  #读取标签
        return img, label

    def __len__(self):
        return len(self.img_path)

root_dir = 'Data\\hymenoptera_data\\hymenoptera_data\\train'
ants_lable_dir = 'ants'
bees_lable_dir = 'bees'

ants_dataset = MyDataSet(root_dir, ants_lable_dir)
bees_dataset = MyDataSet(root_dir, bees_lable_dir)
img1, label1 = ants_dataset[2]
img2, label2 = bees_dataset[2]

cv2.imshow('test1', img1)
cv2.imshow('test2', img2)


cv2.waitKey(0)
cv2.destroyAllWindows()