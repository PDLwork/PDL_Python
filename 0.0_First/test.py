from tkinter import *
root = Tk()
# 获取屏幕尺寸，使窗口位于屏幕中央
width = 380
heigh = 300
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.geometry('500x300+%d+%d'%((screenwidth-500)/2, (screenheight-300)/2))

mainloop()

