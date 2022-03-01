import pygame
import sys

pygame.init()  # 初始化pygame
size = width, height = 734, 286  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
clock = pygame.time.Clock()     #设置一个时钟对象用于控制游戏的速度

background = pygame.image.load('D:/project/Python/PDL_Python/pygame/dragon/picture/background1.png')  # 加载图片
backgroundrect = background.get_rect()  # 获取矩形区域

dragon1 = pygame.image.load('D:/project/Python/PDL_Python/pygame/dragon/picture/dragon1.png')   #加载小恐龙1图片
dragon2 = pygame.image.load('D:/project/Python/PDL_Python/pygame/dragon/picture/dragon2.png')   #加载小恐龙2图片
dragonrect = dragon1.get_rect()     #两个小恐龙图片的大小一样的所以我们只需要洗个矩形框
dragonrect = dragonrect.move(50,210)    #将框移动到地上，这样小恐龙才不会在左上角

flag = True     #创建一个变量用于交替更换小恐龙的图片，从而达成运动的效果
while True:     #死循环确保窗口一直显示
    clock.tick(6)   #设置小恐龙速度，越大越快
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果检测到点击关闭按钮
            sys.exit()      #关闭程序

    screen.blit(background, backgroundrect)  # 将背景画到背景框上
    
    if flag == True:    #通过flag这个变量判断显示的是哪个小恐龙图片
        screen.blit(dragon1, dragonrect)
    else:
        screen.blit(dragon2, dragonrect)
    flag = not flag

    pygame.display.flip()  # 更新全部显示