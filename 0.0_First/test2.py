from tkinter import *

def show(event):
    s=event.keysym
    if s == 'Up':
        lb.insert("end", s)

root=Tk()
root.title('按键实验')
root.geometry('200x200')
lb=Text(root, font=("黑体",20), height=10, width=50)
root.bind('<Up>',show)
lb.pack()
root.mainloop()
