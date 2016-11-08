from tkinter import Button
from views.controlunitoverview import controlunitoverview

class menubutton(Button):
    def __init__(self, string, root, icon, menu):
        self.menu = menu
        self.configview = controlunitoverview(root, string)
        Button.__init__(self, root.interface.frame, text=string, command=self.onclick)
        self.config(relief='flat')
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
        self.configview.drawframe()

        pass
    def onleave(self, e):
        pass
