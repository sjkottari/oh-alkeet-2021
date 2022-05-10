
import math

def laske_sivun_pituus(hypotenuusa): 
    return hypotenuusa / math.sqrt(2)
    
c = float(input("Anna tasakylkisen kolmion hypotenuusan pituus: "))

kateetit = round(laske_sivun_pituus(c), 4)
print("Kylkien pituus: ", kateetit)
