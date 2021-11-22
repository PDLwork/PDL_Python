import numpy
import random
import tkinter

# 初始化矩阵
Q = numpy.zeros((6, 6))

# 回报矩阵R
# R = numpy.array\
# ([
#     [-1,    -1,    -1,    -1,    0,    -1],
#     [-1,    -1,    -1,     0,   -1,   100],
#     [-1,    -1,    -1,     0,   -1,    -1],
#     [-1,     0,     0,    -1,    0,    -1],
#     [ 0,    -1,    -1,     0,   -1,   100],
#     [-1,     0,    -1,    -1,    0,   100]
# ])

R = numpy.array\
([
    [-1,     0,    -1,    -1,   -1,    -1],
    [ 0,    -1,     0,    -1,   -1,    -1],
    [-1,     0,    -1,     0,   -1,    -1],
    [-1,    -1,     0,    -1,    0,    -1],
    [-1,    -1,    -1,     0,   -1,   100],
    [-1,    -1,    -1,    -1,    0,   100]
])

# 设立学习参数
γ = 0.8

#学习次数
learn_number = 0

# Q-Learning主程序
def main(count):
    global learn_number
    learn_number += count
    for i in range(count):
        # 对每一个训练,随机选择一种状态
        state = random.randint(0, 5)

        while True:
            # 创建列表存储当前状态下的所有可能动作
            possible_action = []
            for action in range(6):
                if R[state, action] >= 0:
                    possible_action.append(action)

            next_action = possible_action[random.randint(0, len(possible_action) - 1)]     #在可能动作种中随机挑选下一个动作

            Q[state][next_action] = R[state][next_action] + γ * (Q[next_action]).max()  #计算Q值更新Q表

            state = next_action      #进入下一个状态

            # 到达目的地跳出该E
            if state == 5:
                break

def windows():
    Window = tkinter.Tk()      #创建调参的窗口
    Window.title('Window_Test')    #设置窗口名字
    # Window.geometry('800x600')    #设置窗口大小
    
    #定义文本框
    Text1 = tkinter.Text(Window)
    Text1.pack()
    Text1.insert("end", 'Q-Learning\nNumber of studies :  \n\nR\n')
    Text1.insert("end", R)
    Text1.insert("end", '\n\nQ\n')
    Text1.insert("end", Q)

    #定义按钮函数
    def hit_Button_1():
        main(1)
        Text1.delete(2.21, 2.26)
        Text1.insert(2.21, str(learn_number))
        Text1.delete(13.0, tkinter.END)
        Text1.insert("end", '\n')
        Text1.insert("end", Q)

    def hit_Button_100():
        main(100)
        Text1.delete(2.21, 2.26)
        Text1.insert(2.21, str(learn_number))
        Text1.delete(13.0, tkinter.END)
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
    # print(numpy.ceil(Q))
    # print(Q)
    # print(numpy.amax(Q))
    # Q = numpy.ceil(Q)
    # print(Q / numpy.amax(Q))