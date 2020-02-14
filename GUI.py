from tkinter import *
import function


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master,bg='LightYellow')

        self.focus_set()

        # combine the w-a-s-d to car control function
        self.bind("<w>", function.xFunc1)  # TODO replace with car control function
        self.bind("<s>", function.xFunc1)  # TODO replace with car control function
        self.bind("<a>", function.xFunc1)      # TODO replace with car control function
        self.bind("<d>", function.xFunc1)     # TODO replace with car control function

        self.pack(expand=YES, fill=BOTH)
        self.fm1 = Frame(self, bg='LightYellow')
        self.fm2=Frame(self,bg='black')

        self.window_init()
        self.createwidght()

    def window_init(self):
        self.master.title('welcome to my raspberry car')
        self.master.bg = 'black'
        width, height = self.master.maxsize()
        self.master.geometry("{}x{}".format(width, height))

    def createwidght(self):
        # fm1
        # Button是一种按钮组件，与Label类似，只是多出了响应点击的功能

        # TODO replace with car control function
        b1=Button(self.fm1, text='W-Forward',bg='DeepSkyBlue',command = self.function ).pack(side=TOP, anchor=CENTER, fill=X, expand=YES)
        b2=Button(self.fm1, text='A-Left',bg='DeepSkyBlue', command = self.function).pack(side=LEFT, anchor=W, fill=X, expand=YES)
        b3=Button(self.fm1, text='S-Backward',bg='DeepSkyBlue',command = self.function).pack(side=LEFT, anchor=W, fill=X, expand=YES)
        b4=Button(self.fm1, text='D-Right',bg='DeepSkyBlue',command = self.function).pack(side=LEFT, anchor=W, fill=X, expand=YES)
        # TODO replace with car control function

        self.fm1.pack(side=TOP, fill=BOTH, expand=NO)

        # fm2
        Label(self.fm2, text='video').pack(side=BOTTOM, anchor=W, fill=X, expand=YES)
        self.fm2.pack(side=BOTTOM, fill=BOTH, expand=YES)

    # TODO onyl for test, can be delete later
    def function(self):
        print("hello")



app = Application()
app.mainloop()