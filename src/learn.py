# -*- coding: UTF-8 -*-

# width和height属性，以及一个只读属性resolution

from tkinter import *  # 导入Tkinter模块


def test(a):
    global x
    print(a)
    s = Label(x, text="123")
    s.pack()


x = Tk()

b1 = Button(x, text="aa")
b1.bind("<Button-1>", test)
b1.pack()

x.mainloop()
