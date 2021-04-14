import serial, time
from Adafruit_IO import Client
import logging

logging.basicConfig(format=' %(levelname)s - %(asctime)s - %(message)s ', level=logging.INFO)
aio = Client ('karcio', 'aio_ithi91m18v4RzOGgIGSpM16jSjNg')
 
ser = serial.Serial('/dev/ttyUSB0')
 
data = []
for index in range(0,10):
    datum = ser.read()
    data.append(datum)

def getPm25():
    pmtwofive = int.from_bytes(b''.join(data[2:4]), byteorder='little') / 10
    #aio.send('air-quality-pm-2-5', pmtwofive)
    logging.info("PM 2.5:\t %s",pmtwofive)

    return pmtwofive

def getPm10():
    pmten = int.from_bytes(b''.join(data[4:6]), byteorder='little') / 10
    #aio.send('air-quality-pm-10', pmten)
    logging.info("PM 10:\t %s",pmten)

    return pmten


