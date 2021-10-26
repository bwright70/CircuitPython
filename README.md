# CircuitPython
#### Yay Python
-------------

## Red Servo

### Description

This is the first assignment for engineering 3. We were tasked with turning the color of the imbedded led, in our metro express servo, from blue to red. I chose to take it one step further and make the led repeat a rainbow pattern. 

### Process

We were given the basic code and [a website that allowed us to determine the RGB vaules of colors](https://www.w3schools.com/colors/colors_picker.asp). Changing the color to red was as simple as changing two numbers in the code from (0, 0, 255) to (255, 0, 0). After that I used time.sleep(#) to tell the metro when to pause and then just copied and pasted a bunch of color vaules so that the end result was my led flashing a rainbow pattern 

### [Code](Code/Red.py)

### Image

<img src="Images/ezgif-3-125a11c069bc.gif" width="400" height="400" />

## Useful Tips 

* The RGB vaules need to be whole integers 
* https://www.w3schools.com/colors/colors_picker.asp
* You can reduce the brightness of your led using dot.brightness = a value less than one 

---------

## 180 Servo

### Description

This is the second assignment using circuit python. We just needed to make a servo turned back and forth but I chose to do the extra spicy option which involved using capacitive touch to turn the servo. 

### Process

The first thing to do was make the servo turn. It was fairly simple, all I did was download the code that tells the servo to run and then use "angle =" to tell the servo what direction to turn to. Next came the more complicated part. Capacitive touch is how touch screens work. Basically it sends a small charge down a wire and measures the discharge. Because you are 80% water and a much better conducter than air, when you touch the end of the wire the charge discharges a lot faster, the code measures this and then tells the servo to spin whenever is happens 

### [Code](Code/Capacitive.py) 

```
touch_A1 = touchio.TouchIn(board.A1)

while True:
    if touch_A1.value:
        print("Touched!")
```
This is the section of the code that senses capacitive touch 

### Image 

<img src="Images/ezgif-3-e8f5a2736d0e.gif" width="400" Height="400">

## Useful Tips

* Changing the third value in the "for angle in range" statement makes it spin faster or slower 
* Frequency also changes the speed because its changing the intervals that the servo moves at. 
* The other two numbers in the "for angle in range" statement are defining the direction the servo turns. Its moving from 0 to 180 or from 180 to 0 

-------

## Rainbow Distance Servo 

### Description

In this assignment we were tasked with getting an led to change color based on the distance of a distance sensor. Not only that but the RGB vaules had to be calculated based on the distance and so has you moved your hand closer or futher away it went through the colors of the rainbow 

### Process

The first thing I did was just get a servo to change a led's color, so that when the ditance was less than 5 it would be red and greater than 5 blue. After I got that working I used some premade code to allow the led to change vaules based off the distance values  

### [Code](Code/RainbowDistance.py)

Heres the part of the code that did the calculations

```
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
```

### Image 

<img src="Images/ezgif-4-805969dfd2c8.gif" width="400" height="400" />

## Useful Tips 

* Its very important to have your serial moniter open so you know exactly what vaules the distance sensor is producing
* Once again the RGB vaules need to be whole integers so that it does break
* In the "Color = int(simpleio.map_range(distance, 5, 20, 0, 255))" statement the two numbers define the distance at which its occuring and the second two nnumbers tell the color which direction its moving 
* So has one color increases the other decreases and the final unused color is zero 

-------

## Photo Interruptor 

### Description 
### Process
### Code
### Image 
-------

## LCD

### Description 
### Process
### Code
### Image 
-------
