from controllers.interface import interface
from controllers.controlunit import controlunit
from controllers.scanner import scanner
from views.view import view
from views.menu import menu
import time
from threading import Thread
import traceback

class main:
    def __init__(self):
        # init interface
        self.settings = {
            'graph_growth_x'     :True,
            'graph_fill'         :True,
            'graph_grid_growth_x':True
        }
        self.staticidlist = {}
        self.controlunits = {}
        self.interface = interface(self)
        self.menu = menu(self)
        self.size = []
        self.scanner = scanner(self)

        self.running = True
        self.send = []
        self.thread = Thread(None,self.getdata)
        self.thread.start()

        self.loop()
    def addcontrolunit(self, serial, cu):
        if serial not in self.staticidlist.keys():
            self.staticidlist[serial] = len(self.staticidlist)+1
        self.controlunits[serial] = {
            'controlunit':cu,
            'friendlyid': self.staticidlist[serial]
        }
        self.menu.setcontrolunits(self.controlunits)
        self.menu.general.view.addarduino(cu)
    def removecontrolunit(self, id):
        pass
    def loop(self):
        counter = 0
        lightcounter = 0
        while 1:
            time.sleep(0.01)
            # Make the CPU not blow up  (Went from 25% usage to 0.3%)
            # This works because tkinter buttons are interrupt based
            # And ports are threaded
            counter += 1
            lightcounter += 1

            if lightcounter == 300:
                lightcounter = 0
                for cu in self.controlunits:
                    self.controlunits[cu]['controlunit'].communication.pollcommunication("00001010")
                    self.controlunits[cu]['controlunit'].communication.pollcommunication("00001011")
                    self.controlunits[cu]['controlunit'].communication.pollcommunication("00001100")

            if counter == 50:
                counter = 0
                for cu in self.controlunits:
                    if len(self.controlunits[cu]['controlunit'].communication.data) >= 4:
                        t = int(time.time())
                        # Temp
                        temp = self.controlunits[cu]['controlunit'].communication.get_data(1)
                        self.controlunits[cu]['controlunit'].appenddata(t,'temp',temp[0])
                        # Light
                        light = self.controlunits[cu]['controlunit'].communication.get_data(2)
                        light = light[0] * 256 + light[1]
                        self.controlunits[cu]['controlunit'].appenddata(t,'light',light)
                        # State
                        state = self.controlunits[cu]['controlunit'].communication.get_data(1)
                        self.controlunits[cu]['controlunit'].appenddata(t,'state',state[0])
                        self.menu.draw()

            try:
                testsize = [self.interface.master.winfo_width(), self.interface.master.winfo_height()]
                if testsize != self.size:
                    self.size = testsize
                    self.interface.updatesize(self.size[0],self.size[1])
                    self.menu.draw()
                    self.interface.frame.tkraise()
                self.interface.update()
            except:
                 traceback.print_exc()
                 print("Quitting")
                 self.running = False
                 quit()

            #Try scanner
            self.scanner.scanforports()
    def getdata(self):
        time.sleep(2)
        while self.running:
            for cu in self.controlunits:
                self.controlunits[cu]['controlunit'].communication.has_data_available()
            time.sleep(0.01)
        print("Stopping thread")
    def getdefaultsettings(self):
        pass

if __name__ == "__main__":
    m = main()
