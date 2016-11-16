from models.graph import graph
from views.view import view
from tkinter import *
import math

class general:
    def __init__(self,root):
        self.root = root
        self.frame = Frame(width=500, height=500, bg='#fff')
        cvlist = [
            Canvas(self.frame, background='#222'),
            Canvas(self.frame, background='#444'),
            Canvas(self.frame, background='#666'),
            Canvas(self.frame, background='#888'),
            Canvas(self.frame, background='#aaa'),
            Canvas(self.frame, background='#CCC'),
            Canvas(self.frame, background='#eee')
        ]
        self.canvasList = []
        for x in cvlist:
            self.canvasList.append({
                'graph':graph(x),
                'canvas':x
            })
        self.drawframe()
        pass
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
        for canv in self.canvasList:
            if self.root.settings['graph_growth_x']:  # Grow X
                if curx == x:
                    curx = 0
                    cury += 1
                if self.root.settings['graph_fill']:   # Use odd spacing
                    if curx == 0 and cury == 0: # First one
                        canv['canvas'].config(width=graphodd, height=graphheight)
                        canv['canvas'].place(x=0,y=0)
                        canv['graph'].setdimensions(graphodd, graphheight)
                        curx += limit - len(self.canvasList) + 1
                    else:   # Rest
                        canv['canvas'].config(width=graphwidth, height=graphheight)
                        canv['canvas'].place(x=graphwidth*curx,y=graphheight*cury)
                        canv['graph'].setdimensions(graphwidth, graphheight)
                        curx += 1
                else:
                    canv['canvas'].config(width=graphwidth, height=graphheight)
                    canv['canvas'].place(x=graphwidth*curx,y=graphheight*cury)
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
                        canv['graph'].setdimensions(graphwidth, graphodd)
                        cury += limit - len(self.canvasList) + 1
                    else:   # Rest
                        canv['canvas'].config(width=graphwidth, height=graphheight)
                        canv['canvas'].place(x=graphwidth*curx,y=graphheight*cury)
                        canv['graph'].setdimensions(graphwidth, graphheight)
                        cury += 1
                else:
                    canv['canvas'].config(width=graphwidth, height=graphheight)
                    canv['canvas'].place(x=graphwidth*curx,y=graphheight*cury)
                    canv['graph'].setdimensions(graphwidth, graphheight)
                    cury += 1

        # Loop Canvas for lines
        # Generic for everything
        self.frame.config(width=self.root.interface.width-xoffset, height=self.root.interface.height)
        self.frame.place(x=xoffset,y=0)
        self.frame.tkraise()
        # End-generic
    def send(self):
        pass
    def reset(self):
        pass
    def drawlines(self):
        # Send shit to graph model
        pass
