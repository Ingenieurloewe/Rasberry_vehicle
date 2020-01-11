from tkinter import *

import function


class App:
    def __init__(self, master):
        # 使用Frame增加一层容器

        fm1 = Frame(master)
        # Button是一种按钮组件，与Label类似，只是多出了响应点击的功能
        Button(fm1, text='Top').pack(side=TOP, anchor=W, fill=X, expand=NO)
        Button(fm1, text='Center').pack(side=TOP, anchor=W, fill=X, expand=YES)
        Button(fm1, text='Bottom').pack(side=TOP, anchor=W, fill=X, expand=YES)
        fm1.pack(side=LEFT, fill=BOTH, expand=YES)

        fm2 = Frame(master)
        Button(fm2, text='Left').pack(side=LEFT)
        Button(fm2, text='This is the Center button').pack(side=LEFT)
        Button(fm2, text='Right').pack(side=LEFT)
        fm2.pack(side=LEFT, padx=10)

        la=Label(master)
        Label(root,text = 'pack1',bg = 'red').pack()

root = Tk()
root.title("Pack - Example")
display = App(root)
root.mainloop()



win = tkinter.Tk()
win.title("Kahn Software v1")  # #窗口标题
win.geometry("600x500+200+20")  # #窗口位置500后面是字母x
'''
响应所有事件(键盘)
<Key>   所有键盘按键会触发
'''
xLabel = tkinter.Label(win, text="KAHN Hello world")
xLabel.focus_set()
xLabel.pack()
xLabel.bind("<w>", function.xFunc1)

win.mainloop()  # #窗口持久化c