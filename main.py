from controllers.interface import interface
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
                self.interface.update()
                self.menu.draw()
            except:
                print("Quitting")
                quit()
    def getdefaultsettings(self):
        pass

if __name__ == "__main__":
    main()
