import haravasto

def kasittele_hiiri(x, y, nappi, muokkausnapit):
    """
    Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä.
    Tulostaa hiiren sijainnin sekä painetun napin terminaaliin.
    """
    if nappi == haravasto.HIIRI_VASEN:
        print("Hiiren nappia vasen painettiin kohdassa {} {}".format(x, y))
    elif nappi == haravasto.HIIRI_OIKEA:
        print("Hiiren nappia oikea painettiin kohdassa {} {}".format(x, y))
    elif nappi == haravasto.HIIRI_KESKI:
        print("Hiiren nappia keski painettiin kohdassa {} {}".format(x, y))

def main():
    """
    Luo sovellusikkunan ja asettaa käsittelijäfunktion hiiren klikkauksille.
    Käynnistää sovelluksen.
    """
    haravasto.luo_ikkuna()
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()

if __name__ == "__main__":
    main()
