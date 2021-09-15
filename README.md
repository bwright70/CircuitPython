# CircuitPython
#### Yay Python
-------------
## Red Servo

### Description:

This is the first assignment for engineering 3. We were tasked with turning the color of the imbedded led, in our metro express servo, from blue to red. I chose to take it one step further and make the led repeat a rainbow pattern. 

### Process:

We were given the basic code and a website that allowed us to determine the RGB vaules of colors (https://www.w3schools.com/colors/colors_picker.asp). Changing the color to red was as simple as changing two numbers in the code from (0, 0, 255) to (255, 0, 0). After that I used time.sleep(#) to tell the metro when to pause and then just copied and pasted a bunch of color vaules so that the end result was my led flashing a rainbow pattern 

### Code:

```Python 
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5

print("Make it red!")
while True:
    dot.fill((255, 0, 0))
```

### Images:

<img src="Images/ezgif-3-125a11c069bc.gif" width="400" height="400" />
