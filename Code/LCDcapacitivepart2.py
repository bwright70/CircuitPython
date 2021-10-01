import board
import time
import touchio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface


# get and i2c object
i2c = board.I2C()

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

counter = 0
pasta1 = 0
pasta2 = 0
Positive = 0

while True:
    if touch_A1.value and pasta1 == 0 and Positive == 0:
        counter += 1
        print(counter)
        lcd.clear()
        lcd.print(str(counter))
        time.sleep(0.1)
        lcd.print("\nCounting Up")
    pasta1 = touch_A1.value
    if touch_A1.value and pasta1 == 0 and Positive == 1:
        counter -= 1
        print(counter)
        lcd.clear()
        lcd.print(str(counter))
        time.sleep(0.1)
        lcd.print("\nCounting Down")
    pasta1 = touch_A1.value
    if touch_A2.value and pasta2 == 0 and Positive == 0:
        Positive = 1
        lcd.clear()
        time.sleep(0.1)
        lcd.print("negative")
    if touch_A2.value and pasta2 == 0 and Positive == 1:
        Positive = 0
        lcd.clear()
        time.sleep(0.1)
        lcd.print("positive")
