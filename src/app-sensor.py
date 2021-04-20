from RPLCD.i2c import CharLCD
import time
import csv
import datetime
from airquality import getPm25, getPm10

lcd = CharLCD('PCF8574', 0x3f)

now = '{:%Y%m%d-%H%M%S}'.format(datetime.datetime.now())
file = 'readings_' + now + '.csv'

while True:
    lcd.clear()
    pm25 = str(getPm25())
    pm10 = str(getPm10())
    
    lcd.cursor_pos = (0,4)
    lcd.write_string('AIR QUALITY')

    lcd.cursor_pos = (2, 0) 
    lcd.write_string('PM2.5: ')
    lcd.cursor_pos = (2, 7) 
    lcd.write_string(pm25)

    lcd.cursor_pos = (3, 0)
    lcd.write_string('PM10: ')
    lcd.cursor_pos = (3, 7)
    lcd.write_string(pm10)
        
    with open(file, 'a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([pm25,pm10])
        csvfile.close()

    time.sleep(5)
