ELAIMET = {
    "a": "aasi",
    "k": "koira",
    "@": "kissa",
    "h": "hemuli",
    "l": "lammas"
}

pelto = [
    [" ", "a", " ", " ", "l"],
    [" ", "k", "@", "k", " "],
    ["h", " ", "a", "k", " "]
]


def tutki_ruutu(merkki, rivi, sarake):
    """
    Funktio tutkii ruudun - jos siellä on eläin, se tulostaa eläimen sijainnin sekä nimen.
    """
    if ELAIMET.get(merkki) is not None:
        print("Ruudusta ({x},{y} loytyy {elikko})".format(
            x=sarake, y=rivi, elikko=ELAIMET.get(merkki)))


def tutki_kentta(kentta):
    """
    Funktio tutkii kentän sisällön käymällä sen kokonaan läpi kutsuen tutki_ruutu-funktiota
    jokaiselle kentän sisällä olevalle alkiolle.
    """
    for i in range(len(kentta)):
        for j in range(len(kentta[i])):
            tutki_ruutu(kentta[i][j], i, j)


tutki_kentta(pelto)
