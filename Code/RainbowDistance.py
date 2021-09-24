import time
import board
import adafruit_hcsr04
import neopixel
import simpleio


sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A1)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5
distance = 0

while True:
    try:
        distance = sonar.distance
        print((distance))
        if distance <= 5:
            dot.fill((255, 0, 0))
        if distance > 5 and distance < 20:
            BLUE = int(simpleio.map_range(distance, 5, 20, 0, 255))
            RED = int(simpleio.map_range(distance, 5, 20, 255, 0))
            GREEN = 0
            dot.fill((RED, GREEN, BLUE))
            print(RED, GREEN, BLUE)
        if distance >= 20 and distance <= 35:
            GREEN = int(simpleio.map_range(distance, 20, 35, 0, 255))
            BLUE = int(simpleio.map_range(distance, 5, 20, 255, 0))
            RED = 0
            dot.fill((RED, GREEN, BLUE))
            print(RED, GREEN, BLUE)
    except RuntimeError:
            print("Retrying!")
    time.sleep(0.1)