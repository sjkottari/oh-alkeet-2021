from turtle import *

def piirra_nelio(sivu, x, y):
    if x > 0:
        color("blue")
    elif x < 0:
        color("red")
    up()
    setx(x)
    down()
    begin_fill()
    forward(sivu)
    left(90)
    forward(sivu)
    left(90)
    forward(sivu)
    left(90)
    forward(sivu)
    end_fill()
    up()
    
piirra_nelio(40, -100, 100)
piirra_nelio(60, 100, -100)
piirra_nelio(100, -50, -20)
piirra_nelio(80, 90, 30)
done()