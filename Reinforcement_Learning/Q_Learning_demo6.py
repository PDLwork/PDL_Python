'''2D寻宝例子'''
'''该版本为放到一个陌生环境，不知道一共有多少状态量'''

import tkinter
import numpy
import time
import random

'''----------------------------Q-Learning算法部分-----------------------------------'''
position_x = 0
position_y = 0
position_list = []


def main():
    pass

'''----------------------------------GUI页面-------------------------------------'''
windows = tkinter.Tk()
windows.title('Window_Test')

canvas = tkinter.Canvas(windows, height=300, width=300)
canvas.pack()

canvas.create_line(0,  50,  300,  50,fill="black")
canvas.create_line(0, 100,  300, 100,fill="black")
canvas.create_line(0, 150,  300, 150,fill="black")
canvas.create_line(0, 200,  300, 200,fill="black")
canvas.create_line(0, 250,  300, 250,fill="black")
canvas.create_line( 50, 0,   50, 300,fill="black")
canvas.create_line(100, 0,  100, 300,fill="black")
canvas.create_line(150, 0,  150, 300,fill="black")
canvas.create_line(200, 0,  200, 300,fill="black")
canvas.create_line(250, 0,  250, 300,fill="black")

canvas.create_rectangle(255, 255, 295, 295,fill="blue")
canvas.create_rectangle( 55, 105,  95, 145,fill="black")
canvas.create_rectangle( 55, 155,  95, 195,fill="black")
canvas.create_rectangle( 55, 205,  95, 245,fill="black")
canvas.create_rectangle(155, 105, 195, 145,fill="black")
canvas.create_rectangle(155, 205, 195, 245,fill="black")

circle_anget = canvas.create_oval(5, 5, 45, 45,fill="red")

'''测试可删'''
def test():
    Text1 = tkinter.Text(windows, font=("黑体",20), height=10, width=50)
    Text1.pack()

    def Press_Key(event):
        global position_y
        global position_x
        if event.keysym == 'Up':
            canvas.move(circle_anget, 0, -50)
            position_y += 1
        if event.keysym == 'Down':
            canvas.move(circle_anget, 0, 50)
            position_y -= 1
        if event.keysym == 'Right':
            canvas.move(circle_anget, 50, 0)
            position_x += 1
        if event.keysym == 'Left':
            canvas.move(circle_anget, -50, 0)
            position_x -= 1

        Text1.insert("end", '(%d,'%position_x + '%d)'%position_y)
    
    windows.bind('<Key>', Press_Key)

test()

windows.mainloop()

