import haravasto
import random

tila = {
    "kentta": []
}


def miinoita(miinakentta, vapaat_ruudut, miinat_lkm):
    """
    Asettaa kentälle N kpl miinoja satunnaisiin paikkoihin.
    """
    for i in range(miinat_lkm):
        x, y = random.choice(vapaat_ruudut)
        miinakentta[y][x] = 'x'
        vapaat_ruudut.remove((x, y))



def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    temp = tila["kentta"]
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == 'x':
                haravasto.lisaa_piirrettava_ruutu('x', j * 40, i * 40)
            elif temp[i][j] == ' ':
                haravasto.lisaa_piirrettava_ruutu(' ', j * 40, i * 40)
    haravasto.piirra_ruudut()


def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(600, 400)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aloita()


if __name__ == "__main__":
    kentta = []
    for rivi in range(10):
        kentta.append([])
        for sarake in range(15):
            kentta[-1].append(" ")

    tila["kentta"] = kentta

    jaljella = []
    for x in range(15):
        for y in range(10):
            jaljella.append((x, y))

    miinoita(tila["kentta"], jaljella, 35)
    main()
