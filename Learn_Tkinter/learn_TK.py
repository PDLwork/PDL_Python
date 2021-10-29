import tkinter

window = tkinter.Tk()       #实例化object，建立窗口window
window.title('Learn')       #给窗口的可视化起名字
window.geometry('500x300')  #设定窗口的大小(长 * 宽)这里的乘是小x

var = tkinter.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
Label1 = tkinter.Label(window, text='Test', bg='red', font=('Arial', 15), width=25, height=2)
Label2 = tkinter.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=1)
# bg为背景，font为字体，width为长，height为高
# 这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

Label1.pack()    # Label内容content区域放置位置，自动调节尺寸
Label2.place(x = 0, y = 200)
# 放置的方法有：
# 1）l.pack(); pack(side = top/bottom/left/right)默认top
# 2)l.place();place(x=50, y=100, anchor='nw')anchor='nw'，锚定点是西北角。

var_InputPath = tkinter.StringVar()
var_CsvName = tkinter.StringVar()
Entry1 = tkinter.Entry(window, textvariable = var_InputPath, show='*', font=('Arial', 14))   # 显示成密文形式
Entry2 = tkinter.Entry(window, textvariable = var_CsvName, show=None, font=('Arial', 14))  # 显示成明文形式
Entry1.pack()
Entry2.pack() 

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
hit_flag = False
def hit_button1():
    global hit_flag
    if hit_flag == False:
        hit_flag = True
        var.set(var_InputPath.get())
    else:
        hit_flag = False
        var.set(var_CsvName.get())

Button1 = tkinter.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_button1)

Button1.pack()

window.mainloop()
# 注意，loop因为是循环的意思
# #window.mainloop就会让window不断的刷新
# 如果没有mainloop,就是一个静态的window
# 传入进去的值就不会有循环，mainloop就相当于一个很大的while循环
# 有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。