import serial
import glob

class scanner:
    def __init__(self):
        # Moet system checken voor poorten... Windows is COM# en Linux is
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)] # Make a list with COM1 to COM255
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*') # Makes a list with the Linux ports... or so it should
        #This needs work
        self.ports = ports

    def scanforports(self):
        for p in self.ports:
            pass
        pass
