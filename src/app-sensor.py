from RPLCD.i2c import CharLCD
import time
from airquality import getPm25, getPm10

lcd = CharLCD('PCF8574', 0x3f)

while True:
    lcd.clear()
    pm25 = str(getPm25())
    pm10 = str(getPm10())


    lcd.cursor_pos = (0, 0) 
    lcd.write_string('PM2.5: ')
    lcd.cursor_pos = (0, 7) 
    lcd.write_string(pm25)

    lcd.cursor_pos = (1, 0)
    lcd.write_string('PM10: ')
    lcd.cursor_pos = (1, 7)
    lcd.write_string(pm10)


    time.sleep(5)


