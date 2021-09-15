import board
import pwmio
import time
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.A2, frequency=50)
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 10):
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -10):
        my_servo.angle = angle
        time.sleep(0.05)