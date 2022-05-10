
def laske_nelion_ala(sivun_pituus):
    return sivun_pituus * sivun_pituus
    
sivu = float(input("Anna nelion sivun pituus: "))
pinta_ala = round(laske_nelion_ala(sivu), 4)
print("Nelion pinta-ala: ", pinta_ala)
