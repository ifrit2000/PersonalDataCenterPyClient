# -*- coding: UTF-8 -*-

from tkinter import *


def login():
    root = Tk()

    Label(root, text='账号: ').grid(row=0, sticky=W)
    Entry(root).grid(row=0, column=1, sticky=E)

    Label(root, text='密码: ').grid(row=1, sticky=W)
    Entry(root).grid(row=1, column=1, sticky=E)

    Button(root, text="登陆").grid(row=2, column=1, sticky=E)
    root.mainloop()


if __name__ == '__main__':
    login()
