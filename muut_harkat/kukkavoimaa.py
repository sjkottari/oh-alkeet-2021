from turtle import *
import math

colormode(255)

color("red")
for i in range(5):
    begin_fill()
    kulma = 72 * i
    x = math.cos(math.radians(kulma)) * 50
    y = math.sin(math.radians(kulma)) * 50
    up()
    goto(x, y)
    down()
    circle(30)
    end_fill()
    
    
for i in range(10):
    r = 50 - 5 * i
    up()    
    goto(0, 30 - r)
    down()
    color((255, 255 - i * 5, 110 - (i * 10)))
    begin_fill()
    circle(r)
    end_fill()  

done()

