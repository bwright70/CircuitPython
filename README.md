# CircuitPython
#### Yay Python
-------------

## Red Servo

### Description

This is the first assignment for engineering 3. We were tasked with turning the color of the imbedded led, in our metro express servo, from blue to red. I chose to take it one step further and make the led repeat a rainbow pattern. 

### Process

We were given the basic code and a website that allowed us to determine the RGB vaules of colors (https://www.w3schools.com/colors/colors_picker.asp). Changing the color to red was as simple as changing two numbers in the code from (0, 0, 255) to (255, 0, 0). After that I used time.sleep(#) to tell the metro when to pause and then just copied and pasted a bunch of color vaules so that the end result was my led flashing a rainbow pattern 

### [Code](Code/Red.py)

### Image

<img src="Images/ezgif-3-125a11c069bc.gif" width="400" height="400" />

---------

## 180 Servo

### Description

This is the second assignment using circuit python. We just needed to make a servo turned back and forth but I chose to do the extra spicy option which involved using capacitive touch to turn the servo. 

### Process

The first thing to do was make the servo turn. It was fairly simple, all I did was download the code that tells the servo to run and then use "angle =" to tell the servo what direction to turn to. Next came the more complicated part. Capacitive touch is how touch screens work. Basically it sends a small charge down a wire and measures the discharge. Because you are 80% water and a much better conducter than air, when you touch the end of the wire the charge discharges a lot faster, the code measures this and then tells the servo to spin whenever is happens 

### Code

### Image 

-------
