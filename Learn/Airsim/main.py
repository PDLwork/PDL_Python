import airsim
import numpy
import cv2
import matplotlib.pyplot
import tkinter

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
    cv2.imwrite('img/RGB/'+str(prefix)+'.png', img_rgb)
    cv2.imwrite('img/Grayscale/'+str(prefix)+'.png', img_gray)

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

if __name__ == "__main__":
    client = airsim.MultirotorClient()  # 与airsim创建链接
    client.confirmConnection()  # 查询是否建立连接
    client.enableApiControl(True)   # 打开API控制权
    client.armDisarm(True)  # 解锁

    client.takeoffAsync().join()   # 起飞
    client.moveToZAsync(-15, 1).join()   # 上升到3m高度

    drivetrain = airsim.DrivetrainType.ForwardOnly
    yaw_mode = airsim.YawMode(False, 90)

    client.moveToPositionAsync(10, 0, -15, 1, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 飞到（5,0）点坐标
    client.moveToPositionAsync(10, 10, -15, 1, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 飞到（5,5）点坐标
    client.moveToPositionAsync(0, 10, -15, 1, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 飞到（0,5）点坐标
    client.moveToPositionAsync(0, 0, -15, 1, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 回到（0,0）点坐标

    client.landAsync().join()     # 降落

    client.armDisarm(False)     # 上锁
    client.enableApiControl(False)   # 关闭API控制权

    print('测试完成')