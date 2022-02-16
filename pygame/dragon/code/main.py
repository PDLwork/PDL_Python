import pygame
import sys

pygame.init()  # 初始化pygame
size = width, height = 734, 286  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
clock = pygame.time.Clock()

background = pygame.image.load('D:/project/Python/PDL_Python/pygame/dragon/picture/background1.png')  # 加载图片
backgroundrect = background.get_rect()  # 获取矩形区域

dragon1 = pygame.image.load('D:/project/Python/PDL_Python/pygame/dragon/picture/dragon1.png')
dragon2 = pygame.image.load('D:/project/Python/PDL_Python/pygame/dragon/picture/dragon2.png')
dragonrect = dragon1.get_rect()
dragonrect = dragonrect.move(50,210)

flag = True
while True:  # 死循环确保窗口一直显示
    clock.tick(6)
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()

    screen.blit(background, backgroundrect)  # 将图片画到窗口上
    if flag == True:
        screen.blit(dragon1, dragonrect)
    else:
        screen.blit(dragon2, dragonrect)
    flag = not flag

    pygame.display.flip()  # 更新全部显示