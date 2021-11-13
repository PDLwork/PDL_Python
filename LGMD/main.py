import tkinter
import cv2
import numpy
from array_test import array_print_excel

'''-------------------------初始参数设计-------------------------'''
sigma_E = 1.5
sigma_I = 5
r = 6
a = 1.2
alfa = -0.1
beta = 0.5
lamda = 0.7

'''-------------------------LGMD函数部分-------------------------'''
def main():
    print(sigma_E, sigma_I, r, a, alfa, beta, lamda)


'''-------------------------调试窗口部分-------------------------'''
def GUI_design():
    Window_Tool = tkinter.Tk()      #创建调参的窗口
    Window_Tool.title('Window_Tool')    #设置窗口名字
    Window_Tool.geometry('300x650+0+50')    #设置窗口大小和放置位置

    #设置sigma_E滑动条并放置（参数设置参考使用手册）
    Scale_sigma_E = tkinter.Scale(Window_Tool,\
                        from_=1,\
                        to=5,\
                        resolution=0.1,\
                        length=300,\
                        label='sigma_E',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_sigma_E.set(sigma_E)
    Scale_sigma_E.pack()

    #设置sigma_I滑动条并放置
    Scale_sigma_I = tkinter.Scale(Window_Tool,\
                        from_=1.0,\
                        to=5.0,\
                        resolution=0.1,\
                        length=300,\
                        label='sigma_I',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_sigma_I.set(sigma_I)
    Scale_sigma_I.pack()

    #设置r滑动条并放置
    Scale_r = tkinter.Scale(Window_Tool,\
                        from_=1,\
                        to=7,\
                        resolution=1,\
                        length=300,\
                        label='r',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_r.set(r)
    Scale_r.pack()

    #设置a滑动条并放置
    Scale_a = tkinter.Scale(Window_Tool,\
                        from_=1.0,\
                        to=3.0,\
                        resolution=0.1,\
                        length=300,\
                        label='a',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_a.set(a)
    Scale_a.pack()

    #设置alfa滑动条并放置
    Scale_alfa = tkinter.Scale(Window_Tool,\
                        from_=-1.0,\
                        to=2.0,\
                        resolution=0.1,\
                        length=300,\
                        label='alfa',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_alfa.set(alfa)
    Scale_alfa.pack()

    #设置beta滑动条并放置
    Scale_beta = tkinter.Scale(Window_Tool,\
                        from_=-1.0,\
                        to=2.0,\
                        resolution=0.1,\
                        length=300,\
                        label='beta',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_beta.set(beta)
    Scale_beta.pack()

    #设置lamda滑动条并放置
    Scale_lamda = tkinter.Scale(Window_Tool,\
                        from_=-1.0,\
                        to=2.0,\
                        resolution=0.1,\
                        length=300,\
                        label='lamda',\
                        tickinterval=1,\
                        orient=tkinter.HORIZONTAL,\
                        variable=tkinter.DoubleVar)
    Scale_lamda.set(lamda)
    Scale_lamda.pack()

    #点击按钮激活函数
    #用于调试判断gui有没有问题，执行到最后调用LGMD_main函数
    #获取滑动条数值并全局共享
    def hit_Button_Run():
        global sigma_E
        global sigma_I
        global r
        global a
        global alfa
        global beta
        global lamda
        sigma_E = Scale_sigma_E.get()
        sigma_I = Scale_sigma_I.get()
        r = Scale_r.get()
        a = Scale_a.get()
        alfa = Scale_alfa.get()
        beta = Scale_beta.get()
        lamda = Scale_lamda.get()
        main()

    #设计按钮并放置
    Button_Run = tkinter.Button(Window_Tool,\
                            text='run',\
                            font=('Arial', 12),\
                            width=10,\
                            height=1,\
                            command=hit_Button_Run)
    Button_Run.pack()

    #窗口循环显示
    Window_Tool.mainloop()

if __name__ == '__main__':
    GUI_design()