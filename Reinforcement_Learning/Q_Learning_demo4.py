'''直线寻宝例子'''

import numpy
import random
import tkinter
import time

# 初始化矩阵
Q = numpy.zeros((6, 3))

# 折扣因子
γ = 0.8

# 学习因子
α = 0.9

#选择概率
ε = 0.8

# 学习次数
learn_number = 0

# 动作代表值
Left = 0
Right = 1
keep = 2

#根据当前状态选择下一动作 
def choose_action(state):
    if (random.random() > ε) or ((Q[state] == 0).all()):
        if state == 0:
            next_action = random.choice([Right, keep])
        elif state == 5:
            next_action = random.choice([Left, keep])
        else:
            next_action = random.choice([Left, Right, keep])
    else:
        next_action = numpy.argmax(Q[state]) 

    return next_action

#根据当前状态和动作与环境交互得到奖励和下一状态
def get_environment_feedback(state, action):
    if action == Right:
        canvas1.move(circle1, 60, 0)
        next_state = state + 1
    
    if action == Left:
        canvas1.move(circle1, -60, 0)
        next_state = state - 1

    if action == keep:
        next_state = state

    if (state == 4) and (next_state == 5):
        R = 100
    elif (state == 5) and (next_state == 5):
        R = 100
    else:
        R = 0

    time.sleep(0.2)
    Window.update()

    return R, next_state

# Q-Learning主程序
def main(count):
    global learn_number
    learn_number += count
    environment_renew()

    for i in range(count):
        # 对每一个训练,随机选择一种状态
        state = 0
        # state = random.randint(0, 5)

        step = 0

        while True:
            next_action = choose_action(state)      #根据当前状态选择动作

            R, next_state = get_environment_feedback(state, next_action)        #根据状态和动作确定奖励和下一状态

            Q_target = R + γ * Q[next_state].max()
            Q_predict= Q[state][next_action]
            Q[state][next_action] += α * (Q_target - Q_predict)                 #计算Q值更新Q表

            Q_table_renew()

            state = next_state      #进入下一个状态

            step += 1

            # 到达目的地跳出该回合训练
            if state == 5:
                break
        
        Text2.insert("end", '%d\t'%step)

#GUI页面设计
Window = tkinter.Tk()      #创建调参的窗口
Window.title('Window_Test')    #设置窗口名字

#定义文本框
Text1 = tkinter.Text(Window, font=("黑体",20), height=10, width=50)
Text1.pack()
Text1.insert("end", 'Q-Learning\nNumber of studies :  \n\nQ Table\n')
Text1.insert("end", Q)

canvas1 = tkinter.Canvas(Window, height=120, width=370)
canvas1.pack()

line1 = canvas1.create_line( 10, 100,  60, 100,fill="black")
line2 = canvas1.create_line( 70, 100, 120, 100,fill="black")
line3 = canvas1.create_line(130, 100, 180, 100,fill="black")
line4 = canvas1.create_line(190, 100, 240, 100,fill="black")
line5 = canvas1.create_line(250, 100, 300, 100,fill="black")
line6 = canvas1.create_line(310, 100, 360, 100,fill="black")

rectangle1 = canvas1.create_rectangle(315, 50, 355, 90,fill="blue")
circle1 = canvas1.create_oval(15, 50, 55, 90,fill="red")

Text2 = tkinter.Text(Window, font=("黑体",30), height=10, width=50)
Text2.pack()

def Q_table_renew():
    Text1.delete(5.0, tkinter.END)
    Text1.insert("end", '\n')
    Text1.insert("end", Q)
    Window.update()

def environment_renew():
    global circle1
    canvas1.delete(circle1)
    circle1 = canvas1.create_oval(15, 50, 55, 90,fill="red")

    Text1.delete(2.21, 2.26)
    Text1.insert(2.21, str(learn_number))
    Window.update()

count_flag = False
def move():
    global count_flag
    if count_flag:
        main(1)
    Window.after(1000, move)
    count_flag = True

move()

Window.mainloop()
