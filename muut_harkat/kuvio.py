import math

def laske_nelio_ala(sivun_pituus):
    return sivun_pituus * sivun_pituus

def laske_sektorin_ala(sade, sisakulma):
    return (sisakulma * math.pi * (sade ** 2)) / 360
    
def laske_sivun_pituus(hypotenuusa):
    return hypotenuusa / math.sqrt(2)
    
def laske_kuvion_ala(x):
    pieni_nelio = laske_nelio_ala(x)
    kateetin_pituus = laske_sivun_pituus(x)
    
    pieni_kolmio = (kateetin_pituus * kateetin_pituus) / 2
    
    r = kateetin_pituus
    sektorin_kulma = 45
    pieni_sektori = laske_sektorin_ala(r, sektorin_kulma)
    
    iso_x = r * 2
    iso_nelio = laske_nelio_ala(iso_x)
    
    iso_sektorin_kulma = 270
    iso_sektori = laske_sektorin_ala(iso_x, iso_sektorin_kulma)
    
    return pieni_nelio + pieni_kolmio + pieni_sektori + iso_nelio + iso_sektori

x_sivu = float(input("Anna x: "))
kuvion_ala = round(laske_kuvion_ala(x_sivu), 4)
print("Kuvion ala: ", kuvion_ala)
