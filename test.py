import serial
import serial.tools.list_ports
import threading
import sys

class SerialPort:

    def __init__(self,com):
        try:
            self.ser = serial.Serial(port=com, baudrate=9600, timeout=1)
            #self.ser.open()
            self.inwaiting = 0
        except:
            print("Port in use")

    def read(self):
        toread = ""
        if self.inwaiting > 0:
            toread = self.ser.read(self.inwaiting).decode('utf-8')
            self.inwaiting = 0
        if toread != b'':
            print(toread)
        else:
            print("Timeout: didn't read JACK")

    def write(self):
        towrite = ""
        while towrite == "":
            try:
                towrite = int(input("Wat wil je zeggen?"))
            except:
                print("Int value pls")
        print(towrite)
        if towrite == 1:
            self.ser.write(b'1')
            self.inwaiting = 1
        if towrite == 2:
            self.ser.write(b'2')
            self.inwaiting = 1
        if towrite == 0:
            quit()


ser_arr = []
for device in serial.tools.list_ports.comports():
    print("Looking")
    if device.description.find('Arduino Uno') != -1: # Gevonden
        print(device.serial_number)
        print(device.device)
        #x = SerialPort(device.device)
        #ser_arr.append(x)

quit()
while 1:
    for x in ser_arr:
        x.write()
        x.read()
