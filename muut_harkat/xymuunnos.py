import math 

def muunna_xy_koordinaateiksi(kulma, osoitinvektori):
    x1 = int(round(math.cos(kulma) * osoitinvektori))
    y1 = int(round(math.sin(kulma) * osoitinvektori))
    return x1, y1
    
rad = float(input("Anna kulma radiaaneina: "))
vektori = float(input("Anna osoitinvektorin pituus: "))
x, y = muunna_xy_koordinaateiksi(rad, vektori)
print("x-koordinaatti: ", x)
print("y-koordinaatti: ", y)
