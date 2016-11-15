from tkinter import Button
from tkinter import PhotoImage


class menubutton(Button):
    def __init__(self, string, root, iconstring, menu, view):
        self.menu = menu
        self.view = view
        if iconstring == None:
            Button.__init__(self, root.interface.frame, text=string, command=self.onclick, relief='flat')
        else:
            self.icon = PhotoImage(file=iconstring)
            Button.__init__(self, root.interface.frame, compound="right", image=self.icon, text=string, command=self.onclick, relief='flat')
        self.id = str(self)
        pass
    def disable(self):
        pass
    def enable(self):
        pass
    def onhover(self, e):
        pass
    def onclick(self):
        self.menu.setactive(self.id)
        self.view.drawframe()

        pass
    def onleave(self, e):
        pass

if __name__ == '__main__':
    quit("Not main")
