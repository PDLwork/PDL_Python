import pygame
import sys

pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口

color = (0, 0, 255)  # 设置颜色
ball = pygame.image.load('D:/project/Python/PDL_Python/pygame/ball.png')  # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域

speed = [5, 8]
clock = pygame.time.Clock()

while True:  # 死循环确保窗口一直显示
    clock.tick(60)
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()

    screen.fill(color)  # 填充颜色
    screen.blit(ball, ballrect)  # 将图片画到窗口上

    ballrect = ballrect.move(speed)   #移动图片

    # 碰到左右边缘
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    pygame.display.flip()  # 更新全部显示

pygame.quit()  # 退出pygame