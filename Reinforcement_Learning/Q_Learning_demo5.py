import tkinter
import time

windows = tkinter.Tk()
windows.title('Window_Test')    #设置窗口名字

canvas1 = tkinter.Canvas(windows, height=100, width=370)
canvas1.pack()

line1 = canvas1.create_line( 10, 100,  60, 100,fill="black")
line2 = canvas1.create_line( 70, 100, 120, 100,fill="black")
line3 = canvas1.create_line(130, 100, 180, 100,fill="black")
line4 = canvas1.create_line(190, 100, 240, 100,fill="black")
line5 = canvas1.create_line(250, 100, 300, 100,fill="black")
line6 = canvas1.create_line(310, 100, 360, 100,fill="black")

rectangle1 = canvas1.create_rectangle(315, 50, 355, 90,fill="blue")
circle1 = canvas1.create_oval(15, 50, 55, 90,fill="red")

def hit_Button_Right():
    canvas1.move(circle1, 60, 0)

def hit_Button_Left():
    canvas1.move(circle1, -60, 0)

Button_Right = tkinter.Button(windows,\
                            text='Right',\
                            command=hit_Button_Right)
Button_Right.pack()

Button_Left = tkinter.Button(windows,\
                            text='Left',\
                            command=hit_Button_Left)
Button_Left.pack()

# def time_move():
#     time.sleep(1)
#     canvas1.move(circle1, 60, 0)

windows.mainloop()

count_flag = False
def move():
    global count_flag
    if count_flag:
        canvas1.move(circle1, 60, 0)
    windows.after(1000, move)
    count_flag = True
    print(1)

move()

# windows.mainloop()