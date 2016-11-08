import time

class controlunit:
    def __init__(self):
        self.data = {}
    def appenddata(self, timestamp, typeof, value):
        if timestamp not in self.data:
            print(type(timestamp))
    def pollcommunication(self, opcode, value):
        pass
    def reset(self):
        pass
    def getgraph(self):
        pass
    def getsettings(self):
        pass
    def getdata(self):
        pass

if __name__ == '__main__':
    cu = controlunit()
    cu.appenddata(time.time(), 'x','y')
