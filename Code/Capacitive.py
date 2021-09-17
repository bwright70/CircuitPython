
import time
import board
import touchio
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.A2, frequency=100)
my_servo = servo.Servo(pwm)

touch_A1 = touchio.TouchIn(board.A1)
touch_A2 = touchio.TouchIn(board.A2)

while True:
    if touch_A1.value:
        print("Touched!")
        for angle in range(0, 180, 5):
            my_servo.angle = angle
        time.sleep(0.05)
    if touch_A2.value:
        print("Negative touch")
        for angle in range(180, 0, -5):
            my_servo.angle = angle
        time.sleep(0.05)