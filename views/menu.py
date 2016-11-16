from models.menubutton import menubutton
from views.controlunitoverview import controlunitoverview
from views.view import view
from views.settings import settings
from views.general import general
import math

class menu(view):
    def __init__(self, root):
        super().__init__(root)
        self.arduinobuttons = {}
        self.colours = {
            'active':'#fcc',
            'normal':'#eee',
            'disabled':'#555'
        }
        self.settings = menubutton("Settings", root, "assets\settings.png", self, settings(root))
        self.general = menubutton("General", root, "assets\whitespace.png", self, general(root))
        self.active = str(self.general)
        self.draw()
    def draw(self):
        w = math.floor(self.root.interface.width * 0.25)
        h = 30 if self.root.interface.height > 300 else self.root.interface.height * 0.10
        if self.active == self.settings.id:
            self.settings.view.drawframe()
        elif self.active == self.general.id:
            self.general.view.drawframe()
        else:
            for x in self.arduinobuttons:
                if x.id == self.active:
                    x.view.drawframe()
        self.settings.place(y=(self.root.interface.height-h), x=0, width=w, height=h)
        i = 0;
        for x in sorted(self.arduinobuttons.keys()):
            i += 1
            self.arduinobuttons[x]['button'].place(y=h*i, x=0, width=w, height=h)
        self.general.place(y=0, x=0, width=w, height=h)
    def setcontrolunits(self, cudict):
        # geef een nieuwe dict met controlunits als er controlunits gevonden zijn
        for serial in cudict:
            cu = cudict[serial]
            self.arduinobuttons[cu['friendlyid']] = {
                'id': serial,
                'button': menubutton("Control Unit {}".format(cu['friendlyid']), self.root, "assets\whitespace.png", self, controlunitoverview(self.root, cu))
            }
        self.draw()
    def setactive(self, id):
        self.general.config(bg=self.colours['normal'])
        self.settings.config(bg=self.colours['normal'])
        for x in self.arduinobuttons:
            print(self.arduinobuttons[x]['button'])
            self.arduinobuttons[x]['button'].config(bg=self.colours['normal'])
            if str(self.arduinobuttons[x]['button']) == id:
                print("Its this one")
                self.arduinobuttons[x]['button'].config(bg=self.colours['active'])
        # check settings en general
        if self.settings.id == id:
            self.settings.config(bg=self.colours['active'])
        if self.general.id == id:
            self.general.config(bg=self.colours['active'])
        self.active = id
        # switch naar geklikt knopje
    def setbuttonstate(self,id):
        # Is dit switch of ben ik een methode vergeten? :D
        pass

if __name__ == '__main__':
    quit("Not main")
