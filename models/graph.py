from random import randint
import time

class graph:
    def __init__(self, canvas, controlunit, general=None):
        self.canvas = canvas
        #self.controlunit = controlunit
        self.width = 0
        self.controlunit = controlunit
        self.height = 0
        self.lines = {
            'light':[],
            'temp':[]
        }
        self.lastLight = 0
        self.lastTemp = 0
        self.steps = 10
        self.checkingSeconds = 3
        self.general = general
        self.time = int(time.time())
        self.canvas.after(300,self.makelines)
        self.previousFirstLight = 0
        self.previousFirstTemp = 0
        self.data = {}
        self.drawlight = True
        self.drawtemp = True
    def update(self):   # Im so sorry its 3 hours to the presentations
        # Draw lines
        self.canvas.delete('light')
        self.canvas.delete('temp')
        light_to_pixel_ratio = (self.height - 10) / 1024
        temp_to_pixel_ratio = (self.height - 10) / 100
        count = 0
        if self.general is not None:
            ouroptions = False
            for i in range(0,len(self.general.canvasList)):
                if str(self.general.canvasList[i]['canvas']) == str(self.canvas):
                    ouroptions = i
            if ouroptions is not False:
                self.drawlight = self.general.canvasOptions[ouroptions]['c_light'].get()
                self.drawtemp = self.general.canvasOptions[ouroptions]['c_temp'].get()
        # Draw light
        if self.drawlight:
            for line in self.lines['light']:
                self.canvas.create_line(
                    5+((self.width-20)/self.steps)*count,
                    (1024-line['y1'])*light_to_pixel_ratio,
                    5+((self.width-20)/self.steps)*(count+1),
                    (1024-line['y2'])*light_to_pixel_ratio, tag='light', fill='#E00')
                self.lastLight = line['y2']
                count+=1
            # Draw temp
            count = 0
        if self.drawtemp:
            for line in self.lines['temp']:
                self.canvas.create_line(
                    5+((self.width-20)/self.steps)*count,
                    (100-line['y1'])*temp_to_pixel_ratio,
                    5+((self.width-20)/self.steps)*(count+1),
                    (100-line['y2'])*temp_to_pixel_ratio, tag='temp', fill='#0AA')
                self.lastTemp = line['y2']
                count+=1
        if self.general is not None:
            ouroptions = False
            for i in range(0,len(self.general.canvasList)):
                if str(self.general.canvasList[i]['canvas']) == str(self.canvas):
                    ouroptions = i
            if ouroptions is not False:
                drawlight = self.general.canvasOptions[ouroptions]['v_light'].config(text="{} Lux".format(self.lastLight))
                drawtemp = self.general.canvasOptions[ouroptions]['v_temp'].config(text="{} C".format(self.lastTemp))
    def setdata(self, data):
        pass
    def setxaxis(self, labellist):
        pass
    def setyaxis(self, labellist):
        pass
    def setdimensions(self, width, height):
        self.width = width
        self.height = height
        self.drawgrid()

    def makelines(self):
        # maak een lijst met coordinaten voor de lijnen... NIET TEKENEN
        if self.data != self.controlunit.getdata():
            data = self.controlunit.getdata()
            sortedkeys = sorted(data.keys())
            if len(sortedkeys) > self.steps:
                sortedkeys.pop(0)

            prevlight = self.previousFirstLight if self.previousFirstLight != 0 else data[sortedkeys[0]][1]
            self.previousFirstLight = data[sortedkeys[0]][1]
            prevtemp = self.previousFirstTemp if self.previousFirstTemp != 0 else data[sortedkeys[0]][2]
            self.previousFirstTemp = data[sortedkeys[0]][2]
            self.lines = {
                'light':[],
                'temp':[]
            }
            for key in sortedkeys:
                self.lines['light'].append({
                    'y1':prevlight,
                    'y2':data[key][1]
                })
                prevlight = data[key][1]
                self.lines['temp'].append({
                    'y1':prevtemp,
                    'y2':data[key][2]
                })
                prevtemp = data[key][2]
            self.update()
        self.canvas.after(500,self.makelines)

    def drawgrid(self):
        self.canvas.delete('grid')
        # x to x
        if self.height < 200:
            lines = 4
        else:
            lines = 6
        axis = self.height // lines
        for i in range(1, lines):
            self.canvas.create_line(5,axis*i, self.width-5, axis*i, dash=(2,5), tag='grid')
        # y to y
        if self.width < 300:
            lines = 4
        elif self.width < 500:
            lines = 6
        elif self.width < 700:
            lines = 8
        else:
            lines = 10
        axis = self.width // lines

    def onclick():
        # Als op de graph geklikt word... van vroeger ook nog
        pass
    def getval():
        # Geeft een tuple met welke lijnen worden weergegeven
        # Wordt toch niet geïmplementeerd, is voor tijd over
        pass

if __name__ == '__main__':
    quit("Not main")
