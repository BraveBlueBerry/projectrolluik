from views.view import view
from tkinter import *
import math
# Hackathon taught me to write ugly code, im so sorry
class settings(view):
    def __init__(self,root):
        self.root = root
        # Tabs
        self.activeFrame = 0
        self.tabs = [Frame(width=0, height=0, bg='#eee'),Frame(width=0, height=0, bg='#eee')]
        self.menuFrame = Frame(width=0, height=0, bg='#e0e0e0')
        self.tabButtonOne = Button(self.menuFrame, text="Control Units", command=(lambda: self.switchFrame(0)))
        self.tabButtonTwo = Button(self.menuFrame, text="Program Settings", command=(lambda: self.switchFrame(1)))
        self.tabButtonOne.invoke()

        #
        #       Tab 1
        #
        self.sendButton = Button(self.tabs[0], text="Send", command=self.send)
        self.saveButton = Button(self.tabs[1], text="Send", command=self.send)
        self.resetButton = Button(self.tabs[0], text="Reset", command=self.reset)
        # Setting Labels
        self.settingMessage = Label(self.tabs[0], text="Waarden voor automatische regeling instellen")
        self.optionlabel = Label(self.tabs[0], text="Arduino")
        self.statuslabel = Label(self.tabs[0], text="Rolluik besturing")
        self.minHeightlabel = Label(self.tabs[0], text="Minimale hoogte")
        self.minHeightlabelunit = Label(self.tabs[0], text="cm")
        self.maxHeightlabel = Label(self.tabs[0], text="Maximale hoogte")
        self.maxHeightlabelunit = Label(self.tabs[0], text="cm")
        self.minTemplabel = Label(self.tabs[0], text="Minimale temperatuur")
        self.minTemplabelunit = Label(self.tabs[0], text="°C")
        self.maxTemplabel = Label(self.tabs[0], text="Maximale temperatuur")
        self.maxTemplabelunit = Label(self.tabs[0], text="°C")
        self.luxlabel = Label(self.tabs[0], text="Minimale lichtintensiteit")
        self.luxlabelunit = Label(self.tabs[0], text="Lux")

        # Status radio buttons
        self.statusValue = IntVar(self.tabs[0])
        self.statuslabel = Label(self.tabs[0], text="Rolluik besturing")
        self.statusradio = [Radiobutton(self.tabs[0], text="Automated", variable=self.statusValue, value=0),
                            Radiobutton(self.tabs[0], text="Open", variable=self.statusValue, value=1),
                            Radiobutton(self.tabs[0], text="Closed", variable=self.statusValue, value=2)]
        # Height settings
        self.minHeight = Entry(self.tabs[0])
        self.maxHeight = Entry(self.tabs[0])

        # Temp settings
        self.minTemp = Entry(self.tabs[0])
        self.maxTemp = Entry(self.tabs[0])

        # Licht settings
        self.lux = Entry(self.tabs[0])

        self.optionmenuvalue = StringVar(self.tabs[0])
        self.optionmenuvalue.set("all") # default value
        self.optionmenu = OptionMenu(self.tabs[0], self.optionmenuvalue, "all", "one", "two", "three")


        #
        #       Tab 2
        #
        self.gfill_value = BooleanVar(self.tabs[1])
        self.gfill_label = Label(self.tabs[1], text="Fill empty spaces in overview")
        self.gfill_radio = [Radiobutton(self.tabs[1], text="Fill", variable=self.gfill_value, value=True),
                            Radiobutton(self.tabs[1], text="Leave Open", variable=self.gfill_value, value=False)]
        if self.root.settings['graph_fill']:
            self.gfill_radio[0].select()
        else:
            self.gfill_radio[1].select()

        self.ggrid_growth_value = BooleanVar(self.tabs[1])
        self.ggrid_growth_label = Label(self.tabs[1], text="Grow graph grid in direction")
        self.ggrid_growth_radio = [Radiobutton(self.tabs[1], text="Horizontal", variable=self.ggrid_growth_value, value=True),
                                 Radiobutton(self.tabs[1], text="Vertical", variable=self.ggrid_growth_value, value=False)]
        if self.root.settings['graph_grid_growth_x']:
            self.ggrid_growth_radio[0].select()
        else:
            self.ggrid_growth_radio[1].select()

        self.ggraph_fill_growth_value = BooleanVar(self.tabs[1])
        self.ggraph_fill_growth_label = Label(self.tabs[1], text="Graph fill in direction")
        self.ggraph_fill_growth_radio = [Radiobutton(self.tabs[1], text="Horizontal", variable=self.ggraph_fill_growth_value, value=True),
                                 Radiobutton(self.tabs[1], text="Vertical", variable=self.ggraph_fill_growth_value, value=False)]
        if self.root.settings['graph_growth_x']:
            self.ggraph_fill_growth_radio[0].select()
        else:
            self.ggraph_fill_growth_radio[1].select()




        self.drawframe()

    def switchFrame(self, frameTo):
        self.activeFrame = frameTo
        if frameTo == 0: # Set program active button
            self.tabButtonOne.config(bg='#fcc')
            self.tabButtonTwo.config(bg='#eee')
        else:
            self.tabButtonOne.config(bg='#eee')
            self.tabButtonTwo.config(bg='#fcc')
        self.drawframe()
    def drawframe(self):
        # Go check for controlunits

        #

        xoffset = math.floor(self.root.interface.width * 0.25)
        width = math.ceil(self.root.interface.width * 0.75)
        heightTen = math.floor((self.root.interface.height-50) * 0.10)

        # Arduino bordje menu
        self.optionmenu.place(x=(width*0.5), y=20, width=100)
        self.optionlabel.place(x=(width*0.5)-100, y=25, width=100)
        # Settings labels
        self.settingMessage.place(x=(width*0.05), y=heightTen*2)
        self.minHeightlabel.place(x=(width*0.05), y=heightTen*3)
        self.maxHeightlabel.place(x=(width*0.05), y=heightTen*4)
        self.minTemplabel.place(x=(width*0.05), y=heightTen*5)
        self.maxTemplabel.place(x=(width*0.05), y=heightTen*6)
        self.luxlabel.place(x=(width*0.05), y=heightTen*7)

        # Setting entries
        self.minHeight.place(x=(width*0.35), y=heightTen*3, width=(width*0.20))
        self.maxHeight.place(x=(width*0.35), y=heightTen*4, width=(width*0.20))
        self.minTemp.place(x=(width*0.35), y=heightTen*5, width=(width*0.20))
        self.maxTemp.place(x=(width*0.35), y=heightTen*6, width=(width*0.20))
        self.lux.place(x=(width*0.35), y=heightTen*7, width=(width*0.20))
        # Units
        self.minHeightlabelunit.place(x=(width*0.55), y=heightTen*3, width=(width*0.1))
        self.maxHeightlabelunit.place(x=(width*0.55), y=heightTen*4, width=(width*0.1))
        self.minTemplabelunit.place(x=(width*0.55), y=heightTen*5, width=(width*0.1))
        self.maxTemplabelunit.place(x=(width*0.55), y=heightTen*6, width=(width*0.1))
        self.luxlabelunit.place(x=(width*0.55), y=heightTen*7, width=(width*0.1))
        # Rolluik besturing
        self.statuslabel.place(x=(width*0.70), y=heightTen*2)
        for i in range(0,len(self.statusradio)):
            self.statusradio[i].place(x=(width*0.70), y=heightTen*(3+i), height=heightTen)

        buttonHeight = 47 if heightTen > 47 else heightTen
        self.sendButton.place(x=width*0.5-200, y=heightTen*8.5, width=100, height=buttonHeight)
        self.resetButton.place(x=width*0.5+100, y=heightTen*8.5, width=100, height=buttonHeight)

        #Tab 2
        self.ggrid_growth_label.place(x=width*0.5-150, y=10, width=300, height=heightTen)
        self.ggrid_growth_radio[0].place(x=width*0.5-150, y=heightTen*1, width=300, height=heightTen)
        self.ggrid_growth_radio[1].place(x=width*0.5-150, y=heightTen*2, width=300, height=heightTen)

        self.ggraph_fill_growth_label.place(x=width*0.5-150, y=heightTen*3, width=300, height=heightTen)
        self.ggraph_fill_growth_radio[0].place(x=width*0.5-150, y=heightTen*4, width=300, height=heightTen)
        self.ggraph_fill_growth_radio[1].place(x=width*0.5-150, y=heightTen*5, width=300, height=heightTen)

        self.gfill_label.place(x=width*0.5-150, y=heightTen*6, width=300, height=heightTen)
        self.gfill_radio[0].place(x=width*0.5-150, y=heightTen*7, width=300, height=heightTen)
        self.gfill_radio[1].place(x=width*0.5-150, y=heightTen*8, width=300, height=heightTen)

        self.saveButton.place(x=width*0.5-50, y=heightTen*9, width=100, height=heightTen)
        # Place active tab at X,Y 0,30
        # Width = full
        # Height = full-30
        self.tabs[self.activeFrame].config(width=self.root.interface.width-xoffset, height=self.root.interface.height-30)
        self.tabs[self.activeFrame].place(x=xoffset,y=30)
        self.tabs[self.activeFrame].tkraise()
        # Place menu at X,Y 0,0
        # Width = full
        # Height = 30
        self.menuFrame.config(width=self.root.interface.width-xoffset, height=30)
        self.menuFrame.place(x=xoffset,y=0)
        self.menuFrame.tkraise()

        # Labels for settings

        buttonWidth = math.floor(self.root.interface.width * 0.15) if math.floor(self.root.interface.width * 0.15) > 100 else 100
        self.tabButtonOne.place(x=0,y=0,width=buttonWidth,height=30)
        self.tabButtonTwo.place(x=buttonWidth,y=0,width=buttonWidth,height=30)
    def buttonstatus(self,e):
        print(e)
    def send(self):
        if self.activeFrame == 1:   # Tab 2
            self.root.settings = {
                'graph_growth_x'     :self.ggraph_fill_growth_value.get(),
                'graph_fill'         :self.gfill_value.get(),
                'graph_grid_growth_x':self.ggraph_fill_growth_value.get()
            }
        else:                       # Tab 1
            pass
    def reset(self):
        pass
    def drawlines(self):
        # Send shit to graph model
        pass

if __name__ == '__main__':
    quit("Not main")
