from controllers.interface import interface
from controllers.controlunit import controlunit
from controllers.scanner import scanner
from views.view import view
from views.menu import menu

class main:
    def __init__(self):
        # init interface

        self.interface = interface(self)
        self.menu = menu(self)
        self.size = []
        self.loop()
    def addcontrolunit(self, cu):
        pass
    def removecontrolunit(self, id):
        pass
    def loop(self):
        while 1:
            try:
                testsize = [self.interface.master.winfo_width(), self.interface.master.winfo_height()]
                if testsize != self.size:
                    self.size = testsize
                    self.interface.updatesize(self.size[0],self.size[1])
                    self.menu.draw()
                    self.interface.frame.tkraise()
                self.interface.update()
            except:
                print("Quitting")
                quit()
    def getdefaultsettings(self):
        pass

if __name__ == "__main__":
    m = main()
