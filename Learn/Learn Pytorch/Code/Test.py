from torch.utils.data import Dataset
import cv2

img_path = "F:/Project/PDL_Python/Learn/Learn Pytorch/Data/hymenoptera_data/hymenoptera_data/train/ants/0013035.jpg"
img = cv2.imread(img_path, cv2.IMREAD_COLOR)

cv2.imshow('test', img)

# class MyData(Dataset):
#     def __init__(self):
    
#     def __getitem__(self, idx):


cv2.waitKey(0)
cv2.destroyAllWindows()
