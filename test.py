import serial as s
import time

ser = s.Serial()  # open serial port
ser.port = 'COM3'
ser.baudrate = 9600
ser.timeout = 2
ser.setDTR(False)
ser.open()
print(ser.name)         # cehck which port was really used

opcode = '00001100'
tosend = chr(int(opcode,2)).encode('utf-8')


print("Python value sent: ")
print('12')
ser.write(tosend)     # write a string
inn = ser.read(5)
print("Arduino send back: ")
print(inn)
ser.close()             # close port

