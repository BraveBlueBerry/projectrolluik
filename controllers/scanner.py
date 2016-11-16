import serial.tools.list_ports
from controllers.communication import communication
from controllers.controlunit import controlunit
class scanner:
    def __init__(self, root):
        self.root = root
        # Moet system checken voor poorten... Windows is COM# en Linux is
        pass

    def scanforports(self):
        for device in serial.tools.list_ports.comports():
            if device.description.find('Arduino Uno') != -1: # Gevonden
                if device.serial_number not in self.root.controlunits.keys():   # Make controlunit
                    c = communication(device.device)
                    cu = controlunit(c)
                    if cu.communication.connected:
                        self.root.addcontrolunit(device.serial_number, cu)
