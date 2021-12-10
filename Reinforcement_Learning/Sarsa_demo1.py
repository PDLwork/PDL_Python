'''2D寻宝例子'''
'''该版本为放到一个陌生环境，不知道一共有多少状态量'''
'''更多陷阱且设计避免同一方式掉入陷阱'''

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

#运动时间
step_time = 0.05

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

    action_list = [Left, Right, Up, Down]
    if position_x == 0:
        action_list.remove(Left)
    if position_x == 5:
        action_list.remove(Right)
    if position_y == 0:
        action_list.remove(Up)
    if position_y == -5:
        action_list.remove(Down)

    if (random.random() > ε) or ((Q[state] == 0).all()):
        action = random.choice(action_list)
    else:
        temporary_list = []
        for i in action_list:
            temporary_list.append(Q[state][i])
        max_value = max(temporary_list)
        if max_value == 0:
            for i in range(4):
                if (i in action_list) and (Q[state][i] == 0):
                    action = i
        else:
            action = numpy.argwhere(Q[state] == max_value)[0][0]

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
        next_state = len(Q) - 1

    if position_x == 5 and position_y == -5:
        R = 100
    elif position_x == 1 and position_y == -2:
        R = -100
    elif position_x == 1 and position_y == -3:
        R = -100
    elif position_x == 1 and position_y == -4:
        R = -100
    elif position_x == 3 and position_y == -2:
        R = -100
    elif position_x == 3 and position_y == -4:
        R = -100
    else:
        R = 0
    
    trap_flag = False
    treasure_flag = False
    if R == -100:
        trap_flag = True
    elif R == 100:
        treasure_flag = True
    
    time.sleep(step_time)
    windows.update()

    return R, next_state, trap_flag, treasure_flag

#Q-Learning主程序
def main():
    state = 0
    environment_renew()
    step = 0
    action = choose_action(state)
    while True:
        R, next_state, trap_flag, treasure_flag = get_environment_feedback(state, action)
        next_action = choose_action(next_state)
        Q_target = R + γ * Q[next_state][next_action]
        Q_predict= Q[state][action]
        Q[state][action] += α * (Q_target - Q_predict)
        state = next_state
        action = next_action
        
        step += 1

        if treasure_flag:
            Text1.insert("end", '%d\t'%step)
            break
        if trap_flag:
            Text1.insert("end", 'F\t')
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

#环境初始化更新
def environment_renew():
    global circle_anget
    canvas.delete(circle_anget)
    circle_anget = canvas.create_oval(5, 5, 45, 45, fill="red")

    windows.update()

'''测试可删'''
def test():
    global Text1, Text2
    Text1 = tkinter.Text(windows, font=("黑体",15), height=10, width=50)
    Text1.pack()

    def Press_Key(event):
        global position_x, position_y
        if event.keysym == 'Up':
            canvas.move(circle_anget, 0, -50)
            position_y += 1
            Text1.insert("end", '(%d,'%position_x + '%d)'%position_y)
        if event.keysym == 'Down':
            canvas.move(circle_anget, 0, 50)
            position_y -= 1
            Text1.insert("end", '(%d,'%position_x + '%d)'%position_y)
        if event.keysym == 'Right':
            canvas.move(circle_anget, 50, 0)
            position_x += 1
            Text1.insert("end", '(%d,'%position_x + '%d)'%position_y)
        if event.keysym == 'Left':
            canvas.move(circle_anget, -50, 0)
            position_x -= 1
            Text1.insert("end", '(%d,'%position_x + '%d)'%position_y)
        if event.keysym == 'space':
            def test():
                main()
                windows.after(1000, test)
            test()
    
    windows.bind('<Key>', Press_Key)

test()

windows.mainloop()