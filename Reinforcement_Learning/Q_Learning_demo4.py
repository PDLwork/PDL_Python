'''直线寻宝例子'''

import numpy
import random
import tkinter

# 初始化矩阵
Q = numpy.zeros((6, 3))

# 折扣因子
γ = 0.8

# 学习因子
α = 0.9

# 学习次数
learn_number = 0

# 动作代表值
Left = 0
Right = 1
keep = 2

#根据当前状态选择下一动作 
def choose_action(state):
    if state == 0:
        next_action = random.choice([Right, keep])
    elif state == 5:
        next_action = random.choice([Left, keep])
    else:
        next_action = random.choice([Left, Right, keep])

    return next_action

#根据当前状态和动作与环境交互得到奖励和下一状态
def get_environment_feedback(state, action):
    if action == Right:
        next_state = state + 1
    
    if action == Left:
        next_state = state - 1

    if action == keep:
        next_state = state

    if (state == 4) and (next_state == 5):
        R = 100
    elif (state == 5) and (next_state == 5):
        R = 100
    else:
        R = 0

    return R, next_state

# Q-Learning主程序
def main(count):
    global learn_number
    learn_number += count

    for i in range(count):
        # 对每一个训练,随机选择一种状态
        state = random.randint(0, 5)

        while True:
            next_action = choose_action(state)      #根据当前状态选择动作

            R, next_state = get_environment_feedback(state, next_action)        #根据状态和动作确定奖励和下一状态

            Q_target = R + γ * Q[next_state].max()
            Q_predict= Q[state][next_action]
            Q[state][next_action] += α * (Q_target - Q_predict)                 #计算Q值更新Q表

            state = next_state      #进入下一个状态

            # 到达目的地跳出该回合训练
            if state == 5:
                break

#GUI页面设计
def windows():
    Window = tkinter.Tk()      #创建调参的窗口
    Window.title('Window_Test')    #设置窗口名字

    #定义文本框
    Text1 = tkinter.Text(Window, font=("黑体",20), height=10, width=50)
    Text1.pack()
    Text1.insert("end", 'Q-Learning\nNumber of studies :  \n\nQ Table\n')
    Text1.insert("end", Q)

    #定义按钮函数
    def hit_Button_1():
        main(1)
        Text1.delete(2.21, 2.26)
        Text1.insert(2.21, str(learn_number))
        Text1.delete(5.0, tkinter.END)
        Text1.insert("end", '\n')
        Text1.insert("end", Q)

    def hit_Button_100():
        main(100)
        Text1.delete(2.21, 2.26)
        Text1.insert(2.21, str(learn_number))
        Text1.delete(5.0, tkinter.END)
        Text1.insert("end", '\n')
        Text1.insert("end", Q)

    #定义按钮并放置
    Button_1 = tkinter.Button(Window,\
                            text='1',\
                            font=('Arial', 12),\
                            width=10,\
                            height=1,\
                            command=hit_Button_1)
    Button_1.pack()

    Button_100 = tkinter.Button(Window,\
                            text='100',\
                            font=('Arial', 12),\
                            width=10,\
                            height=1,\
                            command=hit_Button_100)
    Button_100.pack()

    Window.mainloop()

if __name__ == "__main__": 
    windows()