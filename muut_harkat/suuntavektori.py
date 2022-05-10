def laske_suuntavektori(x0, y0, x1, y1):
    pituus = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    ux = (x1 - x0) / pituus
    uy = (y1 - y0) / pituus
    return ux, uy

def laske_sijainti(suunta_x, suunta_y, nopeus):
    x = suunta_x * nopeus
    y = suunta_y * nopeus
    return x, y

print("Tämä ohjelma laskee kahden pisteen välisen suuntavektorin 2-ulotteisella tasolla")
alku_x = input("Anna alkupisteen x-koordinaatti: ")
alku_y = input("Anna alkupisteen y-koordinaatti: ")
kohde_x = input("Anna päätepisteen x-koordinaatti: ")
kohde_y = input("Anna päätepisteen y-koordinaatti: ")
vektori_x, vektori_y = laske_suuntavektori(alku_x, alku_y, kohde_x, kohde_y)
print("Suuntavektori (x y):", vektori_x, vektori_y)
