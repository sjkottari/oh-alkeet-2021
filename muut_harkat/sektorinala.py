
import math

def laske_sektorin_ala(sade, sisakulma):
    return (sisakulma * math.pi * (sade ** 2)) / 360
    
r = float(input("Anna ympyran sade: "))
kulma = float(input("Anna sektorin sisakulma asteina: "))

pinta_ala = round(laske_sektorin_ala(r, kulma), 4)
print("Sektorin pinta-ala: ", pinta_ala)
