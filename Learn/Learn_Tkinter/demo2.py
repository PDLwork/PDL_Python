import cv2
import tkinter

img = cv2.imread('D:/Project/Python/PDL_Python/Learn_cv2/test.png', cv2.IMREAD_COLOR)

window = tkinter.Tk()       #实例化object，建立窗口window
window.title('Learn')       #给窗口的可视化起名字
window.geometry('1500x1300')  #设定窗口的大小(长 * 宽)这里的乘是小x

canvas = tkinter.Canvas(window, bg='green', height=200, width=500)
image = canvas.create_image(250, 0, anchor='n',image='D:/Project/Python/PDL_Python/Learn_cv2/test.png')

canvas.pack()

window.mainloop()