from models.graph import graph
from views.view import view
from tkinter import *
import math

class controlunitoverview(view):
    def __init__(self,root,controlunit):
        self.root = root
        self.controlunit = controlunit
        self.frame = Frame(width=0, height=0, bg='#eee')
        self.tempCanvas = Canvas(self.frame, bg='#ccc')
        self.lightCanvas = Canvas(self.frame, bg='#ccc')
        self.tempGraph = graph(self.tempCanvas, controlunit)
        self.lightGraph = graph(self.lightCanvas, controlunit)
        self.lightGraph.drawtemp = False
        self.tempGraph.drawlight = False

        #Labels
        self.l_temp = Label(self.frame, text="Temperatuur: {} C".format(0))
        self.l_light = Label(self.frame, text="Lichtintensiteit: {} Lux".format(0))
        self.l_state = Label(self.frame, text="Status: {}".format("Onbekend"))

        #Radio
        self.statusValue = IntVar(self.frame)
        self.statuslabel = Label(self.frame, text="Rolluik besturing")
        self.statusradio = [Radiobutton(self.frame, text="Automatisch", variable=self.statusValue, value=0),
                            Radiobutton(self.frame, text="Opgerold", variable=self.statusValue, value=1),
                            Radiobutton(self.frame, text="Uitgerold", variable=self.statusValue, value=2)]
        self.optionbutton = Button(self.frame, text="Send", command=self.send)
        self.drawframe()
        pass
    def drawframe(self):
        # Generic for everything
        xoffset = math.floor(self.root.interface.width * 0.25)
        width = math.ceil(self.root.interface.width * 0.75)
        ht = math.floor(self.root.interface.height * 0.10)
        self.tempCanvas.config(width=width//2,height=ht*5)
        self.lightCanvas.config(width=width//2,height=ht*5)
        self.tempCanvas.place(x=0,y=0)
        self.lightCanvas.place(x=width//2,y=0)
        self.tempGraph.setdimensions(width//2,ht*5)
        self.lightGraph.setdimensions(width//2,ht*5)

        #labels
        d = self.controlunit.getdata()
        if len(d) > 0:
            highest = sorted(d.keys(), reverse=True)[0]
            s = "Opgerold" if d[highest][0] == 0 else "Uitgerold"
            self.l_temp.config(text="Temperatuur: {} C".format(d[highest][2]))
            self.l_light.config(text="Lichtintensiteit: {} Lux".format(d[highest][1]))
            self.l_state.config(text="Status: {}".format(s))
        self.l_temp.place(x=width*0.25-150,y=ht*6)
        self.l_light.place(x=width*0.25-150,y=ht*7)
        self.l_state.place(x=width*0.25-150,y=ht*8)



        for i in range(0,len(self.statusradio)):
            self.statusradio[i].place(x=(width*0.70), y=ht*(6+i-0.5), height=ht)
        self.optionbutton.place(x=(width*0.70),y=ht*(9), height=ht-10)
        self.frame.config(width=self.root.interface.width-xoffset, height=self.root.interface.height)
        self.frame.place(x=xoffset,y=0)
        self.frame.tkraise()
        # End-generic
    def send(self):
        v = int(self.statusValue.get())
        v = 2 if v > 2 else v
        v = 0 if v < 0 else v
        self.controlunit.communication.pollcommunication('00000000', v)
        self.controlunit.communication.ser.read(1)
    def reset(self):
        pass
    def drawlines(self):
        # Send shit to graph model
        pass

if __name__ == '__main__':
    quit("Not main")
