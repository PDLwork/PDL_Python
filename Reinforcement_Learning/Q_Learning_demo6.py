'''2D寻宝例子'''
'''该版本为放到一个陌生环境，不知道一共有多少状态量'''

import tkinter
import numpy
import time
import random

'''----------------------------Q-Learning算法部分-----------------------------------'''
# 初始化矩阵
Q = numpy.zeros((1, 4))

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
Up = 2
Down = 3

position_x = 0
position_y = 0
position_list = [[0, 0]]

#根据当前状态选择下一动作 
def choose_action(state):
    position_x = position_list[state][0]
    position_y = position_list[state][1]
    action_list = [Right, Left, Up, Down]
    #print(action_list)

    if (random.random() > ε) or ((Q[state] == 0).all()):
        if position_x == 0:
            action_list.remove(Left)
        if position_x == 5:
            action_list.remove(Right)
        if position_y == 0:
            action_list.remove(Up)
        if position_y == -5:
            action_list.remove(Down)
        #print(action_list)
        action = random.choice(action_list)
    else:
        action = numpy.argmax(Q[state])
    
    return action

#根据当前状态和动作与环境交互得到奖励和下一状态
def get_environment_feedback(state, action):
    global Q
    position_x = position_list[state][0]
    position_y = position_list[state][1]

    if action == Up:
        canvas.move(circle_anget, 0, -50)
        position_y += 1
    if action == Down:
        canvas.move(circle_anget, 0, 50)
        position_y -= 1
    if action == Right:
        canvas.move(circle_anget, 50, 0)
        position_x += 1
    if action == Left:
        canvas.move(circle_anget, -50, 0)
        position_x -= 1

    if [position_x, position_y] in position_list:
        next_state = position_list.index([position_x, position_y])
    else:
        position_list.append([position_x, position_y])
        Q = numpy.row_stack([Q, [0, 0, 0, 0]])
        # print(Q)
        next_state = len(Q) - 1
    #print(next_state)
    # print(position_list)

    if position_x == 5 and position_y == -5:
        R = 100
    else:
        R = 0
    
    return R, next_state

#Q-Learning主程序
def main():
    state = 0
    while True:
        action = choose_action(state)
        R, next_state = get_environment_feedback(state, action)
        Q_target = R + γ * Q[next_state].max()
        Q_predict= Q[state][action]
        Q[state][action] += α * (Q_target - Q_predict)
        state = next_state
        
        if position_list[state] == [5, -5]:
            break


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
        global position_x, position_y
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
        if event.keysym == 'space':
            main()

        Text1.insert("end", '(%d,'%position_x + '%d)'%position_y)
    
    windows.bind('<Key>', Press_Key)

test()

windows.mainloop()