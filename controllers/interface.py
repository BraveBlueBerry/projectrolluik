from tkinter import *

class interface:
    def __init__(self, root):
        print("Hello world")
        self.root = root
        self.master = Tk()
        self.master.geometry("500x500")
        self.width = 500
        self.height = 500
        self.frame = Frame(width=self.width, height=self.height, bg="#e0e0e0")
        self.frame.place(relx=0, rely=0)
        self.master.bind("<Configure>", self.updatesize)


    def update(self):
        self.master.update()

    def updatesize(self, e):
        print([self.width, self.height])
        self.width = self.master.winfo_width()
        self.height = self.master.winfo_height()
        self.frame.config(width=self.width, height=self.height)
        self.frame.pack()


if __name__ == '__main__':
    interface('x')
