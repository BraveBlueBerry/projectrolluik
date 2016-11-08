from tkinter import *

class interface:
    def __init__(self, root):
        print("Hello world")
        self.root = root
        self.master = Tk()
        frame = Frame(width=500, height=500, bg="#e0e0e0")
        frame.pack()

if __name__ == '__main__':
    interface('x')
