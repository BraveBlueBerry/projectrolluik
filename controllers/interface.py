from tkinter import *
import math

class interface:
    def __init__(self, root):
        print("Hello world")
        self.root = root
        self.master = Tk()
        self.master.geometry("500x500")
        self.width = 500
        self.height = 500
        self.frame = Frame(width=math.floor(self.width*0.25), height=self.height, bg="#e0e0e0")
        self.frame.place(relx=0, rely=0)
        self.change = True

    def update(self):
        self.master.update()
    def haschanged(self):
        retval = True if self.change else False
        self.change = False
        return retval

    def updatesize(self, width, height):

        self.width = width
        self.height = height
        self.frame.config(width=math.floor(self.width*0.25), height=self.height)
        self.frame.place(x=0, y=0)


if __name__ == '__main__':
    interface('x')
