import serial, time
from Adafruit_IO import Client
import logging

logging.basicConfig(format=' %(levelname)s - %(asctime)s - %(message)s ', level=logging.INFO)
 
ser = serial.Serial('/dev/ttyUSB0')
 
def getPm25():
    data = []
    for index in range(0,10):
        datum = ser.read()
        data.append(datum)

        pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
        logging.info("PM 2.5:\t %s",pmtwofive)
    return pmtwofive

def getPm10():
    data = []  
    for index in range(0,10):
        datum = ser.read()
        data.append(datum)
     
        pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
        logging.info("PM 10:\t %s",pmten)

    return pmten
