from models.graph import graph
from views.view import view
from tkinter import *
import math

class controlunitoverview(view):
    def __init__(self,root,text):
        print(text)
        #self.graph = graph("cu")
        self.root = root
        self.text = text
        self.frame = Frame(width=0, height=0, bg='#fff')
        self.label = Label(self.frame, text=self.text)
        self.drawframe()
        pass
    def drawframe(self):
        # Generic for everything
        xoffset = math.floor(self.root.interface.width * 0.25)
        width = math.ceil(self.root.interface.width * 0.75)
        self.frame.config(width=self.root.interface.width-xoffset, height=self.root.interface.height)
        self.frame.place(x=xoffset,y=0)
        self.frame.tkraise()
        # End-generic
        self.label.place(x=(xoffset+100), y=math.floor(self.root.interface.height * 0.50), width=100, height=100)
    def send(self):
        pass
    def reset(self):
        pass
    def drawlines(self):
        # Send shit to graph model
        pass

if __name__ == '__main__':
    quit("Not main")
