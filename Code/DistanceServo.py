import time
import board
import adafruit_hcsr04
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A1)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5
distance = 0

while True:
    try:
        distance = sonar.distance
        print((distance))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    if distance <= 5:
        dot.fill((0, 0, 255))
    time.sleep(0.1)
    if distance > 5:
        dot.fill((255, 0, 0))
    time.sleep(0.1)