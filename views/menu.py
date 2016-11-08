from models.menubutton import menubutton
from views.view import view
import math

class menu(view):
    def __init__(self, root):
        super().__init__(root)
        self.arduinobuttons = []
        self.settings = menubutton("Settings", root, None, self)
        self.general = menubutton("General", root, None, self)
        self.active = str(self.general)
        self.draw()
    def draw(self):
        w = math.floor(self.root.interface.width * 0.25)
        h = 30 if self.root.interface.height > 300 else self.root.interface.height * 0.10
        if self.active == self.settings.id:
            self.settings.configview.drawframe()
        elif self.active == self.general.id:
            self.general.configview.drawframe()
        else:
            for x in self.arduinobuttons:
                if x.id == self.active:
                    x.configview.drawframe()
        self.settings.place(y=(self.root.interface.height-h), x=0, width=w, height=h)
        self.general.place(y=0, x=0, width=w, height=h)
    def setcontrolunits(self, cudict):
        # geef een nieuwe dict met controlunits als er controlunits gevonden zijn
        pass
    def setactive(self, id):
        for x in self.arduinobuttons:
            x.config(bg='#eee')
            if x.id == id:
                x.config(bg='#fcc')
        # check settings en general
        if self.settings.id == id:
            self.settings.config(bg='#fcc')
            self.general.config(bg='#eee')
        if self.general.id == id:
            self.settings.config(bg='#eee')
            self.general.config(bg='#fcc')
        # switch naar geklikt knopje
    def setbuttonstate(self,id):
        # Is dit switch of ben ik een methode vergeten? :D
        pass
