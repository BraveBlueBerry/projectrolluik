from models.graph import graph
from views.view import view
from tkinter import *
import math

class general:
    def __init__(self,root):
        self.root = root
        self.frame = Frame(width=500, height=500, bg='#fff')

        self.canvasList = []
        self.canvasOptions = []
        self.drawframe()

    def drawframe(self):
        xoffset = math.floor(self.root.interface.width * 0.25)
        width = math.ceil(self.root.interface.width * 0.75)
        # Canvas place loop
        limit = 0
        x = 1
        y = 1
        while x*y < len(self.canvasList):
            if x == y:
                if self.root.settings['graph_grid_growth_x']:
                    x+=1
                else:
                    y+=1
            elif x > y:
                y+=1
            else:
                x+=1
            limit+=1
        # Limit should be 2 with 3 Canvas objects
        limit = x*y # Makes 4
        graphheight = self.root.interface.height // y
        graphwidth = width // x
        graphodd = graphwidth * (limit-len(self.canvasList) +1) if self.root.settings['graph_growth_x'] else graphheight * (limit-len(self.canvasList)+1)

        curx = 0
        cury = 0
        counter = -1
        for canv in self.canvasList:
            counter += 1
            if self.root.settings['graph_growth_x']:  # Grow X
                if curx == x:
                    curx = 0
                    cury += 1
                if self.root.settings['graph_fill']:   # Use odd spacing
                    if curx == 0 and cury == 0: # First one
                        canv['canvas'].config(width=graphodd, height=graphheight)
                        canv['canvas'].place(x=0,y=0)
                        self.canvasOptions[counter]['frame'].place(x=5+xoffset,y=5)
                        canv['graph'].setdimensions(graphodd, graphheight)
                        curx += limit - len(self.canvasList) + 1
                    else:   # Rest
                        canv['canvas'].config(width=graphwidth, height=graphheight)
                        canv['canvas'].place(x=graphwidth*curx,y=graphheight*cury)
                        self.canvasOptions[counter]['frame'].place(x=5+xoffset+graphwidth*curx,y=5+graphheight*cury)
                        canv['graph'].setdimensions(graphwidth, graphheight)
                        curx += 1
                else:
                    canv['canvas'].config(width=graphwidth, height=graphheight)
                    canv['canvas'].place(x=graphwidth*curx,y=graphheight*cury)
                    self.canvasOptions[counter]['frame'].place(x=5+xoffset+graphwidth*curx,y=5+graphheight*cury)
                    canv['graph'].setdimensions(graphwidth, graphheight)
                    curx += 1

            else:   # Grow Y
                if cury == y:
                    cury = 0
                    curx += 1
                if self.root.settings['graph_fill']:   # Use odd spacing
                    if curx == 0 and cury == 0: # First one
                        canv['canvas'].config(width=graphwidth, height=graphodd)
                        canv['canvas'].place(x=0,y=0)
                        self.canvasOptions[counter]['frame'].place(x=5+xoffset,y=5)
                        canv['graph'].setdimensions(graphwidth, graphodd)
                        cury += limit - len(self.canvasList) + 1
                    else:   # Rest
                        canv['canvas'].config(width=graphwidth, height=graphheight)
                        canv['canvas'].place(x=graphwidth*curx,y=graphheight*cury)
                        self.canvasOptions[counter]['frame'].place(x=5+xoffset+graphwidth*curx,y=5+graphheight*cury)
                        canv['graph'].setdimensions(graphwidth, graphheight)
                        cury += 1
                else:
                    canv['canvas'].config(width=graphwidth, height=graphheight)
                    canv['canvas'].place(x=graphwidth*curx,y=graphheight*cury)
                    self.canvasOptions[counter]['frame'].place(x=5+xoffset+graphwidth*curx,y=5+graphheight*cury)
                    canv['graph'].setdimensions(graphwidth, graphheight)
                    cury += 1

        # Loop Canvas for lines
        # Generic for everything
        self.frame.config(width=self.root.interface.width-xoffset, height=self.root.interface.height)
        self.frame.place(x=xoffset,y=0)
        self.frame.tkraise()
        for opt in self.canvasOptions:
            opt['frame'].tkraise()
        # End-generic
    def send(self):
        pass
    def reset(self):
        pass
    def addarduino(self, controlunit):
        canvas = Canvas(self.frame, bg='#ccc')
        g = graph(canvas,controlunit, self)
        self.canvasList.append({
            'graph': g,
            'canvas':canvas
        })
        f = Frame(width=135, height=40)
        d = {
            'frame': f,
            'graph': g,
            'v_temp': Label(f),
            'v_light': Label(f),
            'c_temp': BooleanVar(),
            'c_light': BooleanVar()
        }
        d['c_temp'].set(True)
        d['c_light'].set(True)
        d['b_light'] = Checkbutton(d['frame'], text="Light", variable=d['c_light'], onvalue=True, offvalue=False)
        d['b_temp'] = Checkbutton(d['frame'], text="Temperature", variable=d['c_temp'], onvalue=True, offvalue=False)
        d['b_light'].place(x=-3,y=-3)
        d['b_temp'].place(x=-3,y=17)
        d['v_light'].place(x=90,y=0)
        d['v_temp'].place(x=90,y=20)
        self.canvasOptions.append(d)
        self.drawframe()
