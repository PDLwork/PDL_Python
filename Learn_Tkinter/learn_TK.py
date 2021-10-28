import tkinter

window = tkinter.Tk()       # 第1步，实例化object，建立窗口window
window.title('My Window')       # 第2步，给窗口的可视化起名字
window.geometry('500x300')  #第3步，设定窗口的大小(长 * 宽)这里的乘是小x

var = tkinter.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上

Label1 = tkinter.Label(window, text='骚气小云哥', bg='red', font=('Arial', 15), width=25, height=2)
Label2 = tkinter.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=1)
# bg为背景，font为字体，width为长，height为高
# 这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

Label1.pack()    # Label内容content区域放置位置，自动调节尺寸
Label2.pack() 
# 放置lable的方法有：1）l.pack(); 2)l.place();

# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
hit_flag = False
def hit_me():
    global hit_flag
    if hit_flag == False:
        hit_flag = True
        var.set('you hit me')
    else:
        hit_flag = False
        var.set('')

Button1 = tkinter.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me)

Button1.pack()

# 第6步，主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思
# #window.mainloop就会让window不断的刷新
# 如果没有mainloop,就是一个静态的window
# 传入进去的值就不会有循环，mainloop就相当于一个很大的while循环
# 有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。