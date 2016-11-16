import time

class controlunit:
    def __init__(self, comm):
        self.communication = comm
        self.data = {}
    def appenddata(self, timestamp, typeof, value):
        if timestamp not in self.data:
            if len(self.data) == 0:
                state = 0 if typeof != "state" else value
                light = 0 if typeof != "light" else value
                temp = 0 if typeof != "temp" else value
            else:
                lastkey = sorted(self.data.keys(), reverse=True)
                state = self.data[lastkey][0] if typeof != "state" else value
                light = self.data[lastkey][1] if typeof != "light" else value
                temp = self.data[lastkey][2] if typeof != "temp" else value

        else:  # This will probably never happen but w/e
            state = self.data[timestamp][0] if typeof != "state" else value
            light = self.data[timestamp][1] if typeof != "light" else value
            temp = self.data[timestamp][2] if typeof != "temp" else value
        self.data[timestamp] = (state,light,temp)

    def pollcommunication(self, opcode, value):
        pass
    def reset(self):
        pass
    def getgraph(self):
        pass
    def getsettings(self):
        pass
    def getdata(self):
        # {timestamp: (State, Temp, Lux)}
        pass

if __name__ == '__main__':
    cu = controlunit()
    cu.appenddata(time.time(), 'x','y')
