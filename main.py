from controllers.interface import interface

class main:
    def __init__(self):
        # init interface
        self.interface = interface(self)
        self.loop()
    def addcontrolunit(self, cu):
        pass
    def removecontrolunit(self, id):
        pass
    def loop(self):
        while 1:
            self.interface.master.update()
    def getdefaultsettings(self):
        pass

if __name__ == "__main__":
    main()
