python 库 -- pygame

1、安装pygame

win + r 输入cmd打开命令窗口：输入pip install pygame

2、使用方法

初始化、设置窗口大小并显示、死循环让窗口保持显示

```
pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
```

3、添加图片

```
pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
color = (0, 0, 0)  # 设置颜色
ball = pygame.image.load('D:/project/Python/PDL_Python/pygame/ball.png')  # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
    screen.fill(color)  # 填充颜色
    screen.blit(ball, ballrect)  # 将图片画到窗口上
    pygame.display.flip()  # 更新全部显示
```

上述代码中使用iamge模块的load()方法加载图片，返回值ball是一个Surface对象。Surface是用来代表图片的pygame对象，可以对一个Surface对象进行涂画、变形、复制等各种操作。事实上，屏幕也只是一个Surface，pygame.display.set_mode()就返回了一个屏幕Surface对象。如果将ball这个Surface对象画到screen Surface 对象，需要使用blit()方法，最后使用display模块的flip()方法更新整个待显示的Surface对象到屏幕上。

4、把图片动起来

下面让小球动起来，ball.get_rect()方法返回值ballrect是一个Rect对象，该对象有一个move()方法可以用于移动矩形。move(x, y)函数有两个参数，第一个参数是 X 轴移动的距离，第二个参数是 Y 轴移动的距离。窗口的左上角是(0, 0)，如果是move(100, 50)就是右移100下移50。

```
import pygame
import sys

pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
color = (0, 0, 0)  # 设置颜色
ball = pygame.image.load('ball.png')  # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域

speed = [5, 5]  # 设置移动的X轴、Y轴
while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
    ballrect = ballrect.move(speed)  # 移动小球
    screen.fill(color)  # 填充颜色(设置为0，执不执行这行代码都一样)
    screen.blit(ball, ballrect)  # 将图片画到窗口上
    pygame.display.flip()  # 更新全部显示

pygame.quit()  # 退出pygame
```

4、解决球碰到墙边返回的问题

```
import pygame
import sys

pygame.init()  # 初始化pygame
size = width, height = 640, 480  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口

color = (0, 0, 255)  # 设置颜色
ball = pygame.image.load('D:/project/Python/PDL_Python/pygame/ball.png')  # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域
print(ballrect)
print(ballrect.right)
ballrect = ballrect.move(10,20)   #移动图片
print(ballrect)
print(ballrect.right)

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
```

