import haravasto


planeetta = [
    [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "],
    [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "],
    [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "],
    ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "],
    ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "],
    [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
]


def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    for i in range(len(planeetta)):
        for j in range(len(planeetta[i])):
            if planeetta[i][j] == 'x':
                haravasto.lisaa_piirrettava_ruutu('x', j * 40, i * 40)
            elif planeetta[i][j] == ' ':
                haravasto.lisaa_piirrettava_ruutu(' ', j * 40, i * 40)
    haravasto.piirra_ruudut()


def tulvataytto(planeetta, x, y):
    """
    Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
    täyttö aloitetaan annetusta x, y -pisteestä.
    """
    if planeetta[y][x] != 'x':
        temp = [(x, y)]
        while len(temp) > 0:
            koordinaatit = temp.pop()
            x_koordinaatti, y_koordinaatti = koordinaatit
            planeetta[y_koordinaatti][x_koordinaatti] = "0"
            for i in range(koordinaatit[1]-1, koordinaatit[1]+2):
                for j in range(koordinaatit[0]-1, koordinaatit[0]+2):
                    if -1 < i < len(planeetta) and -1 < j < len(planeetta[0]):
                        if planeetta[i][j] == ' ':
                            temp.append((j, i))
    else:
        print("Osuit miinaan!")



def main(planeetta):
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(len(planeetta[0]) * 40, len(planeetta) * 40)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aloita()


if __name__ == "__main__":
    tulvataytto(planeetta, 3, 5)
    main(planeetta)
