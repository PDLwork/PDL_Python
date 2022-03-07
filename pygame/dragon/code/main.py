import pygame
import sys
import os

#获取当前文件的目录，方便在别的电脑运行时读取相应文件
Current_path = os.path.join(os.getcwd(), 'pygame', 'dragon', 'picture')
Current_path = Current_path.replace('\\', '/')

pygame.init()  # 初始化pygame
size = width, height = 734, 286  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
clock = pygame.time.Clock()

background = pygame.image.load(Current_path + '/background1.png')  # 加载图片
backgroundrect = background.get_rect()  # 获取矩形区域

dragon1 = pygame.image.load(Current_path + '/dragon1.png')
dragon2 = pygame.image.load(Current_path + '/dragon2.png')
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