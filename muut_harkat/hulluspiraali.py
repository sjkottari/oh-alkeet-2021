from turtle import *

def piirra_spiraali(vari, kaaret, alkusade, sade_kasvu, viiva_paksuus=1):
    color(vari)
    pensize(viiva_paksuus)

    down()

    for i in range(kaaret):
        circle(alkusade, 90)
        alkusade += sade_kasvu

piirra_spiraali("black", 20, 10, 3)
piirra_spiraali("red", 10, 20, 4, 3)
piirra_spiraali("blue", 10, -20, -4, 3)
done()

