if __name__ == '__main__':
    print("Not main")
    quit()

import time
import serial
import math
import traceback
import codecs
from models.switch import switch    # For ease of use


class communication:
    def __init__(self, com):
        self.writing = False    # Semaphore
        self.connected = False
        try:
            self.ser = serial.Serial()  # open serial port
            self.ser.port = com
            self.ser.baudrate = 9600
            self.ser.timeout = 1
            self.ser.setDTR(False)       # Not sure what this does but it stops the controlunit from resetting
            self.ser.open()
            self.connected = True
        except:
            print("Could not init port")
        self.data = []

    def scan_port(self):        # Threaded function, loops indefinitely
        pass

    def has_data_available(self, pop = False):
        try:
            while self.ser.inWaiting():
                if not self.writing:
                    self.writing = True # Lock data
                    self.data.append(int(codecs.encode(self.ser.read(1), 'hex').decode('utf-8'), 16))
                    self.writing = False
        except:
            self.connected = False
        self.writing = False    # open data
        return len(self.data)

    def get_data(self, bytes):
        while self.writing:
            time.sleep(0.01)    # Wait for scan_port to finish without blowing up the cpu
        self.writing = True
        returnList = []
        for i in range(0,bytes):
            try:
                returnList.append(self.data.pop(0))
            except:
                return False
        self.writing = False
        return returnList

    def pollcommunication(self, opcode, value=None, wait=False):
        responseBytes = 0
        print(opcode)
        print(value)
        for case in switch(opcode):
            if case('00000000'):        # set status
                print("Hello")
                toSend = chr(int(opcode,2)).encode('utf-8')
                responseBytes = 1
            if case('00000001'):        # set min temp
                toSend = chr(int(opcode,2)).encode('utf-8')
                responseBytes = 1
            if case('00000010'):        # set max temp
                toSend = chr(int(opcode,2)).encode('utf-8')
                responseBytes = 1
            if case('00000011'):        # set max light
                toSend = chr(int(opcode,2)).encode('utf-8')
                responseBytes = 1
            if case('00000100'):        # set min hoogte zonnescherm
                toSend = chr(int(opcode, 2)).encode('utf-8')
                responseBytes = 1
            if case('00000101'):        # set max hoogte zonnescherm
                toSend = chr(int(opcode, 2)).encode('utf-8')
                responseBytes = 1
            if case('00000110'):        # reset
                toSend = chr(int(opcode, 2)).encode('utf-8')
                responseBytes = 1
            if case('00001001'):        # debug
                pass    # Not implemented
            if case('00001010'):        # get temp
                toSend = chr(int(opcode, 2)).encode('utf-8')
                responseBytes = 1
            if case('00001011'):        # get light
                toSend = chr(int(opcode, 2)).encode('utf-8')
                responseBytes = 2

            if case('00001100'):        # get status van zonnescherm
                toSend = chr(int(opcode, 2)).encode('utf-8')
                responseBytes = 1
            if case('00001101'):        # get hoogte van zonnescherm (hoe ver hij van de onderkant af zit)
                toSend = chr(int(opcode, 2)).encode('utf-8')
                responseBytes = 2
            if case('00001110'):        # get min temp
                toSend = chr(int(opcode, 2)).encode('utf-8')
                responseBytes = 1
            if case('00001111'):        # get max temp
                toSend = chr(int(opcode, 2)).encode('utf-8')
                responseBytes = 1
            if case('00010000'):        # get max licht
                toSend = chr(int(opcode, 2)).encode('utf-8')
                responseBytes = 2
            print(opcode)
        # Opcodes have been made, all functions say what they expect
        self.ser.write(toSend)
        print(value)
        if value != None:
            bytesToSend = math.ceil(value.bit_length() / 8)
            print("???")
            if opcode == '00000000':
                print(value.to_bytes(bytesToSend, 'big'))
            self.ser.write(value.to_bytes(bytesToSend, 'big'))

        if wait:
            return self.get_data(responseBytes)
        return
