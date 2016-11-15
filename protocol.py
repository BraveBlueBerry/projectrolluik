import serial as s
import codecs
import math
import time

# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:  # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False


ser = s.Serial()  # open serial port
ser.port = 'COM3'
ser.baudrate = 9600
ser.timeout = 5
ser.setDTR(False)
ser.open()
print("Opened serial connection with port {}".format(ser.name))

# Voor wanneer je twee bytes( of kan ook 1 zijn) moet versturen en twee bytes moet ontvangen
# ser.write(value[0].to_bytes(2,'big'))
# response = int(codecs.encode(ser.read(2),'hex').decode('utf-8'),16)

def blub(opcode, value = None):
    for case in switch(opcode):
        if case('00000000'):        # set status
            toSend = chr(int(opcode,2)).encode('utf-8')
            ser.write(toSend)
            for x in value:
                ser.write(chr(int(bin(x),2)).encode('utf-8'))
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00000001'):        # set min temp
            toSend = chr(int(opcode,2)).encode('utf-8')
            ser.write(toSend)
            for x in value:
                ser.write(chr(int(bin(x), 2)).encode('utf-8'))
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00000010'):        # set max temp
            toSend = chr(int(opcode,2)).encode('utf-8')
            ser.write(toSend)
            for x in value:
                ser.write(chr(int(bin(x), 2)).encode('utf-8'))
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00000011'):        # set max light
            toSend = chr(int(opcode,2)).encode('utf-8')
            ser.write(toSend)
            ser.write(value[0].to_bytes(2,'big'))
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00000100'):        # set min hoogte zonnescherm
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            ser.write(value[0].to_bytes(2, 'big'))
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00000101'):        # set max hoogte zonnescherm
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            ser.write(value[0].to_bytes(2, 'big'))
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00000110'):        # reset
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00000111'):        # setId
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            print(value)
            ser.write(int(value[0]).to_bytes(4, 'big'))
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00001000'):        # getId
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            response = int(codecs.encode(ser.read(4), 'hex').decode('utf-8'), 16)
            return response
        if case('00001001'):        # debug
            pass
        if case('00001010'):        # get temp
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00001011'):        # get light
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            response = int(codecs.encode(ser.read(2), 'hex').decode('utf-8'), 16)
            return response
        if case('00001100'):        # get status van zonnescherm
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00001101'):        # get hoogte van zonnescherm (hoe ver hij van de onderkant af zit)
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            response = int(codecs.encode(ser.read(2), 'hex').decode('utf-8'), 16)
            return response
        if case('00001110'):        # get min temp
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00001111'):        # get max temp
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            response = ord(ser.read(1).decode('utf-8'))
            return response
        if case('00010000'):        # get max licht
            toSend = chr(int(opcode, 2)).encode('utf-8')
            ser.write(toSend)
            response = int(codecs.encode(ser.read(2), 'hex').decode('utf-8'), 16)
            return response

# raar =int(time.time()).to_bytes(4, 'big')
# print(raar)
# print(int(codecs.encode(raar, 'hex').decode('utf-8'), 16))
print(time.time())
# print(blub('00000111', [time.time()]))

print(blub('00001000'))


ser.close()
