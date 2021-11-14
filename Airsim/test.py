"""
test python environment
"""
import airsim

# connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()

# get control
client.enableApiControl(True)       # get control

# unlock
client.armDisarm(True)      # 解锁

# Async methods returns Future. Call join() to wait for task to complete.
client.takeoffAsync().join()    # 起飞

client.moveToZAsync(-3, 1).join()               # 上升到3m高度

drivetrain = airsim.DrivetrainType.ForwardOnly
yaw_mode = airsim.YawMode(False, 90)

client.moveToPositionAsync(10, 0, -3, 5, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 飞到（5,0）点坐标
client.moveToPositionAsync(10, 10, -3, 5, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 飞到（5,5）点坐标
client.moveToPositionAsync(0, 10, -3, 5, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 飞到（0,5）点坐标
client.moveToPositionAsync(0, 0, -3, 5, drivetrain=drivetrain, yaw_mode=yaw_mode).join()  # 回到（0,0）点坐标

client.landAsync().join()       # 降落

# lock
client.armDisarm(False)     # 上锁

# release control
client.enableApiControl(False)      # release control