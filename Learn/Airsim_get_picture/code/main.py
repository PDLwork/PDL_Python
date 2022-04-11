import airsim
import tkinter
import numpy
import cv2
import time

# 定义一个保存图片的函数，保存rgb和灰度图
# 输入的是读取相机的数据和保存图片的索引
def save_image(responses, prefix = ""):
    response = responses[0]

    # frombuffer将data以流的形式读入转化成ndarray对象 这一步只得到一个一维数组
    buffer = numpy.frombuffer(response.image_data_uint8, dtype=numpy.uint8) 

    # reshape把1维数组改为三维数组（得到三通道的RGB图像）
    img_rgb = buffer.reshape(response.height, response.width, -1)
    # 得到灰度图
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    # 保存图片
    cv2.imwrite('./img/RGB/'+str(prefix)+'.png', img_rgb)
    cv2.imwrite('./img/Grayscale/'+str(prefix)+'.png', img_gray)

    '''
    # plt展示图片
    matplotlib.pyplot.subplot(121)
    matplotlib.pyplot.title('RGB image')
    matplotlib.pyplot.axis('off')
    img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
    matplotlib.pyplot.imshow(img_rgb)

    matplotlib.pyplot.subplot(122)
    matplotlib.pyplot.title('Grayscale image')
    matplotlib.pyplot.axis('off')
    matplotlib.pyplot.imshow(img_gray, cmap='gray')

    matplotlib.pyplot.show(block = False)      # 垃圾函数  设计得一点都不好
    # matplotlib.pyplot.ion()     # 可交互
    matplotlib.pyplot.pause(0.01)   #给他反应时间？
    '''

if __name__ == "__main__":
    client_get_picture = airsim.MultirotorClient()   # 与airsim创建链接
    client_get_picture.confirmConnection()   # 查询是否建立连接
    client_get_picture.enableApiControl(True)   # 打开API控制权
    client_get_picture.armDisarm(True)   # 解锁

    i = 0
    while True:
        responses = client_get_picture.simGetImages([airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])   # 每一个的参数：相机名称，图像类型，是否浮点数，是否压缩图像（默认压缩）
        save_image(responses, i)
        time.sleep(1)
        i += 1