import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5

print("Make it red!")
dot.brightness(.29)
while True:
    dot.fill((255, 0, 255))