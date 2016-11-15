from tkinter import *
import math

class interface:
    def __init__(self, root):
        self.root = root
        self.master = Tk()
        self.master.geometry("1100x500")
        self.width = 1100
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
        if self.height < 300:
            self.master.geometry(str(width) + "x300")
        if self.width < 550:
            self.master.geometry("550x" + str(height))
        if self.height == 1 and self.width == 1:
            self.master.geometry("1100x500")

        self.frame.config(width=math.floor(self.width*0.25), height=self.height)
        self.frame.place(x=0, y=0)


if __name__ == '__main__':
    quit("Not main")
