from tkinter import Button

class menubutton(Button):
    def __init__(self, string, root, icon, menu):
        self.menu = menu
        Button.__init__(self, root.interface.frame, text=string, command=self.onclick)
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
        pass
    def onleave(self, e):
        pass
