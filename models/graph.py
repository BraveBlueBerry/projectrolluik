from random import randint

class graph:
    def __init__(self, canvas):
        self.canvas = canvas
        print(self.canvas)
        #self.controlunit = controlunit
        self.width = 0
        self.height = 0
        self.lines = {
            'light':[],
            'temp':[]
        }
        self.steps = 10
        self.canvas.after(300,self.makelines)
    def update(self):
        # Draw lines
        self.canvas.delete('light')
        self.canvas.delete('temp')
        light_to_pixel_ratio = (self.height - 10) / 1000
        temp_to_pixel_ratio = (self.height - 10) / 100
        count = 0
        # Draw light
        for line in self.lines['light']:
            self.canvas.create_line(
                5+((self.width-20)/self.steps)*count,
                line['y1']*light_to_pixel_ratio,
                5+((self.width-20)/self.steps)*(count+1),
                line['y2']*light_to_pixel_ratio, tag='light', fill='#E00')
            count+=1
        # Draw temp
        count = 0
        for line in self.lines['temp']:
            self.canvas.create_line(
                5+((self.width-20)/self.steps)*count,
                line['y1']*temp_to_pixel_ratio,
                5+((self.width-20)/self.steps)*(count+1),
                line['y2']*temp_to_pixel_ratio, tag='temp', fill='#0AA')
            count+=1
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
        if len(self.lines['light']) == 0:
            self.lines['light'].append({
                'y1':randint(10,1000),
                'y2':randint(10,1000)
            })
        else:
            if len(self.lines['light']) >= self.steps:
                self.lines['light'].pop(0)
            self.lines['light'].append({
                'y1': self.lines['light'][len(self.lines['light'])-1]['y2'],
                'y2': randint(10,1000)
            })

        if len(self.lines['temp']) == 0:
            self.lines['temp'].append({
                'y1':randint(10,100),
                'y2':randint(10,100)
            })
        else:
            if len(self.lines['temp']) == self.steps:
                self.lines['temp'].pop(0)
            self.lines['temp'].append({
                'y1': self.lines['temp'][len(self.lines['temp'])-1]['y2'],
                'y2': randint(10,100)
            })
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
        for i in range(1, lines):
            pass
            #self.canvas.create_line(axis*i,self.width-5, axis*i, 10, dash=(2,5), tag='grid')

    def onclick():
        # Als op de graph geklikt word... van vroeger ook nog
        pass
    def getval():
        # Geeft een tuple met welke lijnen worden weergegeven
        # Wordt toch niet geïmplementeerd, is voor tijd over
        pass

if __name__ == '__main__':
    quit("Not main")
