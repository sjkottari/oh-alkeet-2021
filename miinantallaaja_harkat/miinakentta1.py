
TULOSTUKSET = {
    "ulkona": "Antamasi ruutu on kentän ulkopuolella.",
    "nurkassa": "Antamasi ruutu on kentän nurkassa.",
    "laidalla": "Antamasi ruutu on kentän laidalla.",
    "keskellä": "Antamasi ruutu on keskikentällä."
}


def sijainti_kentalla(x, y, leveys, korkeus):
    if x == (leveys - 1) and y == (korkeus - 1):
        return "nurkassa"
    elif x == (leveys - 1) and 0 < y < (korkeus - 1):
        return "laidalla"
    elif x == (leveys - 1) and y == 0:
        return "nurkassa"
    elif 0 < x < (leveys - 1) and y == 0:
        return "laidalla"
    elif x == 0 and y == 0:
        return "nurkassa"
    elif x == 0 and 0 < y < (korkeus - 1):
        return "laidalla"
    elif x == 0 and y == (korkeus - 1):
        return "nurkassa"
    elif 0 < x < (leveys - 1) and y == (korkeus - 1):
        return "laidalla"
    elif x >= leveys or y >= korkeus or x < 0 or y < 0:
        return "ulkona"
    else:
        return "keskellä"


def tulosta_sijainti(avain):
    print(TULOSTUKSET[avain])


leveys = int(input("Anna kentän leveys: "))
korkeus = int(input("Anna kentän korkeus: "))

if leveys > 0 and korkeus > 0:
    x_koordinaatti = int(input("Anna x-koordinaatti: "))
    y_koordinaatti = int(input("Anna y-koordinaatti: "))

    tulos = sijainti_kentalla(x_koordinaatti, y_koordinaatti, leveys, korkeus)
    tulosta_sijainti(tulos)
else:
    print("Noin pienelle kentälle ei mahdu ainuttakaan ruutua!")
