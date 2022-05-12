import airsim

if __name__ == "__main__":
    client = airsim.MultirotorClient()  # 与airsim创建链接
    client.confirmConnection()  # 查询是否建立连接
    client.enableApiControl(True)   # 打开API控制权
    client.armDisarm(True)  # 解锁

    client.takeoffAsync().join()   # 起飞
    client.moveToZAsync(-10, 2).join()   # 上升到15m高度

    drivetrain = airsim.DrivetrainType.ForwardOnly
    yaw_mode = airsim.YawMode(False, 90)

    client.moveToPositionAsync(10, 0, -10, 1, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 飞到（10,0）点坐标
    client.moveToPositionAsync(10, 10, -10, 1, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 飞到（10,10）点坐标
    client.moveToPositionAsync(0, 10, -30, 1, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 飞到（0,10）点坐标
    client.moveToPositionAsync(0, 0, -30, 1, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 回到（0,0）点坐标

    # client.goHomeAsync().join()
    client.moveToZAsync(-1, 2).join()

    client.landAsync().join()     # 降落

    client.armDisarm(False)     # 上锁
    client.enableApiControl(False)   # 关闭API控制权

    print('测试完成')