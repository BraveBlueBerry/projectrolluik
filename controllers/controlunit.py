import time

class controlunit:
    def __init__(self, comm):
        self.communication = comm
        self.data = {}
        self.change = False
    def appenddata(self, timestamp, typeof, value):
        self.change = True
        if timestamp not in self.data:
            if len(self.data) == 0:
                state = 0 if typeof != "state" else value
                light = 0 if typeof != "light" else value
                temp = 0 if typeof != "temp" else value
            else:
                lastkey = sorted(self.data.keys(), reverse=True)[0]
                state = self.data[lastkey][0] if typeof != "state" else value
                light = self.data[lastkey][1] if typeof != "light" else value
                temp = self.data[lastkey][2] if typeof != "temp" else value

        else:  # This will probably never happen but w/e
            state = self.data[timestamp][0] if typeof != "state" else value
            light = self.data[timestamp][1] if typeof != "light" else value
            temp = self.data[timestamp][2] if typeof != "temp" else value
        self.data[timestamp] = (state,light,temp)

        if len(self.data) > 10:
            firstkey = sorted(self.data.keys())[0]
            self.data.pop(firstkey, None) # No exceptions pls
    def reset(self):
        pass
    def getsettings(self):
        pass
    def has_changed(self):
        return self.change
    def getdata(self):
        self.change = False
        return self.data

if __name__ == '__main__':
    cu = controlunit()
    cu.appenddata(time.time(), 'x','y')
