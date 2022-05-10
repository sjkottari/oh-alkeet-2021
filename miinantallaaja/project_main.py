"""
    Miinantallaaja-lopputyö - Ohjelmoinnin alkeet syksy 2021
    @author: Santeri Kottari (Oodi: 2588410) (Peppi: 52934672)
    TOL, Oulun yliopisto
"""

"""
Ohjelman vaatimat kirjastomoduulit:
    - haravasto: Yksinkertainen graafinen käyttöliittymäkirjasto
      miinaharavalle. @author: Mika Oja, Oulun yliopisto
    - random: Käytetään miinakentän satunnaiseen miinoittamiseen.
    - time: Käytetään pelin ajankohdan ja keston merkitsemiseksi
      tilastoihin.
    - pyglet.window.key: Näppäinpainallusten käsittelyä varten.
"""
import haravasto
import random
import time
from pyglet.window import key


"""
Ohjelman tietorakenteet:
    - ikkuna: Sanakirja, sisältää pelin aikana käytetyt taulukot
      miinakentälle ja peli-ikkunan sisältämille ruuduille.
      Seurataan myös pelin etenemistä bool-arvolla.
    - kesto: Sanakirja, jossa pelin aloitus- ja lopetushetki.
    - tilastot: Koostaa yhteen senhetkisen pelin keskeiset tiedot.
      Tiedot viedään pelin päättyessä erilliseen tilastot-tiedostoon.
"""
ikkuna = {
    "miinakentta": [],
    "lippu_ruudut": [],
    "tyhjat_ruudut": [],
    "miina_ruudut": [],
    "peli_meneillaan": True
}

kesto = {
    "START_TIME": 0.0,
    "END_TIME": 0.0
}

tilastot = {
    "ajankohta": "",
    "kesto_min": "",
    "vuorot": 0,
    "nimimerkki": "",
    "lopputulos": {
        "kentan_koko": "",
        "miinat_lkm": "",
        "tulos": ""
    }
}


def kirjoita_tilastot():
    """
    Funktio, jota kutsutaan pelin päätyttyä. Kirjoittaa
    tiedostoon päättyneen pelin keskeiset tiedot
    myöhempää tarkastelua varten.
        aika - ajankohta (kellonaika hh:mm:ss ja päivämäärä yyyy-mm-dd)
        koko - miinakentän koko
        miinat - miinojen määrä
        kesto - pelin kesto minuuteissa (m:ss -muodossa)
        vuorot - tehtyjen siirtojen lukumäärä
        tulos - pelin lopputulos (voitto/häviö)
    """
    try:
        with open("tilastot.txt", "a") as kohde:
            kohde.write("{aika}, {nimim}, {koko}, {miinat}, {kesto}, {vuorot}, {tulos}\n".format(
                aika=tilastot["ajankohta"],
                nimim=tilastot["nimimerkki"],
                koko=tilastot["lopputulos"]["kentan_koko"],
                miinat=tilastot["lopputulos"]["miinat_lkm"],
                kesto=tilastot["kesto_min"],
                vuorot=tilastot["vuorot"],
                tulos=tilastot["lopputulos"]["tulos"]
            ))
    except FileNotFoundError:
        print("Tiedostoa ei voitu luoda/avata")


def tarkastele_tilastot():
    """
    Funktio, joka avaa tilastot-tiedoston tarkastelua
    varten. Varsinainen tietojen tulostus käyttäjälle
    tapahtuu toisessa funktiossa (ks. alla). Tiedot
    tulostetaan aina yksi rivi kerrallaan.
    """
    try:
        with open("tilastot.txt") as lahde:
            for i, rivi in enumerate(lahde.readlines()):
                tulosta_tilastot(i, rivi)
    except FileNotFoundError:
        print("Tilastoja ei ole vielä. Aloita ensin uusi peli.")


def tulosta_tilastot(laskuri, luettu_rivi):
    """
    Jos tilastot-tiedosto löytyi, tulostetaan sieltä aina
    rivi kerrallaan rivillä olevat tiedot. Tätä funktiota
    kutsutaan kutakin riviä kohden. Tulostusta varten tiedot
    on myös muotoiltu luettavampaan muotoon.
    """
    try:
        aika, nimim, koko, miinat, kesto_min, vuorot, tulos = luettu_rivi.split(",")
        klo, pvm = aika.split(" ")
        print("\n{i}. Pelaajan nimi: {n} | pvm. {ymd} klo. {hms}:".format(
            i=laskuri+1,
            n=nimim.strip(),
            hms=klo.strip(),
            ymd=pvm.strip()
        ))
        print("> Kentän koko: {k} ruutua, jossa miinoja {m} kpl".format(
            k=koko.strip(),
            m=miinat.strip()
        ))
        print("> Peli kesti {min} minuuttia, minkä aikana tehtiin {v} siirtoa".format(
            min=kesto_min.strip(),
            v=vuorot.strip()
        ))
        print("> Lopputulos: {}".format(tulos.strip()))
    except ValueError:
        print("Riviä ei voitu tulostaa: {}".format(luettu_rivi))


def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä. Kenttä piirretään eri lailla riippuen esimerkiksi,
    onko peli päättynyt tai onko ruudussa lippu.
    """
    temp = ikkuna["miinakentta"]
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == 'x' and ikkuna["peli_meneillaan"] == False:
                haravasto.lisaa_piirrettava_ruutu('x', j * 40, i * 40)
            elif (j, i) in ikkuna["lippu_ruudut"]:
                haravasto.lisaa_piirrettava_ruutu('f', j * 40, i * 40)
            elif temp[i][j] == 'x':
                haravasto.lisaa_piirrettava_ruutu(' ', j * 40, i * 40)
            elif temp[i][j] == ' ':
                haravasto.lisaa_piirrettava_ruutu(' ', j * 40, i * 40)
            else:
                haravasto.lisaa_piirrettava_ruutu(temp[i][j], j * 40, i * 40)
    haravasto.piirra_ruudut()


def laske_miinat(x, y, kentta):
    """
    Laskee annetussa kentässä yhden ruudun ympärillä olevat miinat ja palauttaa
    niiden lukumäärän. Funktio toimii sillä oletuksella, että valitussa ruudussa ei
    ole miinaa - jos on, sekin lasketaan mukaan. Valitun ruudun tarkistaminen miinan
    varalta tapahtuu kuitenkin jo ennen kuin tätä funktiota kutsutaan.
    """
    miinat = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if -1 < i < len(kentta) and -1 < j < len(kentta[0]):
                if kentta[i][j] == 'x':
                    miinat = miinat + 1
    return miinat


def tulvataytto(kentta, x_alkupiste, y_alkupiste):
    """
    Muuttaa avatuiksi sellaiset miinakentän ruudut, joiden ympärillä
    ei ole yhtäkään miinaa. Täyttö aloitetaan annetusta (x,y)-pisteestä.
    """
    tyhjat = ikkuna["tyhjat_ruudut"]
    liput = ikkuna["lippu_ruudut"]
    temp = [(x_alkupiste, y_alkupiste)]
    while len(temp) > 0:
        koordinaatit = temp.pop()
        x, y = koordinaatit
        miinat_lkm = laske_miinat(x, y, kentta)
        if miinat_lkm == 0:
            if koordinaatit in liput:
                liput.remove(koordinaatit)
            if koordinaatit in tyhjat:
                tyhjat.remove(koordinaatit)
            kentta[y][x] = "0"
            for i in range(koordinaatit[1]-1, koordinaatit[1]+2):
                for j in range(koordinaatit[0]-1, koordinaatit[0]+2):
                    if -1 < i < len(kentta) and -1 < j < len(kentta[0]):
                        if kentta[i][j] == ' ':
                            temp.append((j, i))
        else:
            kentta[y][x] = "{}".format(miinat_lkm)
            if koordinaatit in tyhjat:
                tyhjat.remove(koordinaatit)


def kasittele_hiiri(x, y, nappi, muokkausnapit):
    """
    Funktio, jossa käsitellään hiiren nappien painallukset.
    Vasemman napin käsittely on koodin selkeyttämiseksi viety
    omaan alikäsittelijään (ks. alla). Oikean napin käsittely
    (lippujen asetus) kuitenkin hoidetaan tässä funktiossa.
    Jos tyhjiä ruutuja ei enää ole, peli päättyy voittoon. 
    Piirtofunktiota myös kutsutaan joka kerta napin painalluksen
    yhteydessä mahdollisten grafiikan muutosten vuoksi.
    """
    miinakentta = ikkuna["miinakentta"]
    liput = ikkuna["lippu_ruudut"]
    x = int(x / 40)
    y = int(y / 40)
    if ikkuna["peli_meneillaan"] == False:
        print("Peli on jo päättynyt")
    else:
        if nappi == haravasto.HIIRI_VASEN:
            hiiri_vasen_kasittelija(x, y, miinakentta, liput)
        elif nappi == haravasto.HIIRI_OIKEA:
            if miinakentta[y][x] == 'x' or miinakentta[y][x] == ' ':
                if (x, y) in liput:
                    liput.remove((x, y))
                else:
                    liput.append((x, y))
        if not ikkuna["tyhjat_ruudut"]:
            print("\nVoitit pelin! Paina <ENTER> jatkaaksesi")
            kasittele_tulos()
    piirra_kentta()


def hiiri_vasen_kasittelija(x, y, kentta, liput):
    """
    Vasemman hiiren painikkeen alikäsittelijäfunktio. Hoitaa
    pelilogiikan eri tilanteissa, kuten pelaajan osuessa
    miinaan tai pelaajan klikatessa ruutua, jonka lähellä
    on miinoja. Jos osutaan miinaan, peli päätetään häviöön.
    Tyhjien ruutujen, lippujen sekä tehtyjen siirtojen arvoja
    päivitetään myös.
    """
    tyhjat = ikkuna["tyhjat_ruudut"]
    miinat_lkm = laske_miinat(x, y, kentta)
    if kentta[y][x] == 'x':
        tilastot["vuorot"] += 1
        print("\nOsuit miinaan! Paina <ENTER> jatkaaksesi")
        kasittele_tulos((x, y))
    elif 0 < miinat_lkm < 9 and kentta[y][x] == ' ':
        tilastot["vuorot"] += 1
        if (x, y) in liput:
            liput.remove((x, y))
        kentta[y][x] = '{}'.format(miinat_lkm)
        if (x, y) in tyhjat:
            tyhjat.remove((x, y))
    elif miinat_lkm == 0 and kentta[y][x] == ' ':
        tilastot["vuorot"] += 1
        tulvataytto(kentta, x, y)
    else:
        print("\nLaiton siirto!")


def kasittele_tulos(koordinaatit=None):
    """
    Käsittelee pelitilanteen, joka johtaa pelin päättymiseen.
    Tilanteita on kaksi: 1) Jos pelaaja osuu miinaan ja 2) Jos
    ei ole enää avaamattomia ruutuja. Käytännössä siis muutetaan
    "peli_meneillaan"-lippu False-arvoon, jolla on vaikutusta
    muissa ohjelmafunktioissa, kuten grafiikan piirrossa. Pelin
    päättymisaika myös määritellään täällä.
    """
    if koordinaatit in ikkuna["miina_ruudut"]:
        ikkuna["peli_meneillaan"] = False
        tilastot["lopputulos"]["tulos"] = "Häviö!"
    elif not ikkuna["tyhjat_ruudut"]:
        ikkuna["peli_meneillaan"] = False
        tilastot["lopputulos"]["tulos"] = "Voitto!"
    kesto["END_TIME"] = time.time()


def kasittele_nappain(symboli, muokkausnapit):
    """
    Käsittelee ohjelmalle annetut näppäinpainallukset.
    Käytännössä tunnistaa pelin päätyttyä ENTER-näppäimen
    painalluksen, joka kutsuu peli-ikkunan sulkevaa
    paata_peli()-funktiota.
    """
    if symboli == key.ENTER:
        if ikkuna["peli_meneillaan"] == False:
            paata_peli()


def paata_peli():
    """
    Pelin päätyttyä ja Enterin painalluksen jälkeen lasketaan
    päättyneen pelin kesto ja kutsutaan alustusfunktiota
    valmistelemaan pelin tietorakenteet uutta pelisessiota
    varten. Tilastojen kirjoitusfunktiota kutsutaan tässä kohdin.
    Sulkee myös peli-ikkunan ja palaa tekstikäyttöliittymään.
    """
    haravasto.lopeta()
    kesto_sek = round(kesto["END_TIME"] - kesto["START_TIME"])
    # Inspiraatiota haettiin: https://stackoverflow.com/a/775075
    minuutit, sekunnit = divmod(kesto_sek, 60)
    tilastot["kesto_min"] = "{:d}:{:02d}".format(minuutit, sekunnit)
    tilastot["nimimerkki"] = input("Anna nimimerkkisi: ").strip()
    kirjoita_tilastot()
    alusta_peli()


def alusta_peli():
    """
    Alustaa (resetoi) pelin tarvitsemat tietorakenteet
    seuraavaa peliä varten. Kutsutaan ennen haravasto.lopeta()
    -kirjastofunktiota. "peli_meneillaan"-lippu myös
    vaihdetaan True-arvoon valmiiksi.
    """
    ikkuna["miinakentta"] = []
    ikkuna["lippu_ruudut"] = []
    ikkuna["miina_ruudut"] = []
    ikkuna["tyhjat_ruudut"] = []
    ikkuna["peli_meneillaan"] = True
    kesto["START_TIME"] = 0.0
    kesto["END_TIME"] = 0.0
    tilastot["vuorot"] = 0


def luo_kentta(leveys, korkeus):
    """
    Luodaan kenttä käyttäjän syöttämistä tilatiedoista.
    Kenttä luodaan kaksiulotteisena listana, ja se täytetään
    tuntemattomia ruutuja merkitsevillä välilyönneillä.
    Tyhjät ruudut (eli tässä kaikki) kerätään taulukkoon.
    """
    kentta = []
    for i in range(korkeus):
        kentta.append([])
        for j in range(leveys):
            kentta[-1].append(" ")
    ikkuna["miinakentta"] = kentta

    tyhjat = []
    for x in range(leveys):
        for y in range(korkeus):
            tyhjat.append((x, y))
    ikkuna["tyhjat_ruudut"] = tyhjat


def miinoita(miinakentta, vapaat_ruudut, miinat_lkm):
    """
    Asettaa kentälle N kpl miinoja satunnaisiin paikkoihin.
    Ruudut, joihin miinat asetellaan, merkitään ylös omaan
    taulukkoonsa.
    """
    for i in range(miinat_lkm):
        x, y = random.choice(vapaat_ruudut)
        miinakentta[y][x] = 'x'
        ikkuna["miina_ruudut"].append((x, y))
        vapaat_ruudut.remove((x, y))


def kysy_tiedot():
    """
    Yksinkertainen kysyjäfunktio, joka tiedustelee käyttäjältä
    miinakentän keskeiset tiedot. Kaikki syötteet on oltava
    kokonaislukuja. Palauttaa tiedot main()-funktioon.
    """
    try:
        leveys = int(
            input("\nAnna kentän leveys ruutujen lukumääränä: ").strip())
        korkeus = int(
            input("Anna kentän korkeus ruutujen lukumääränä: ").strip())
        miinat = int(input("Anna sijoitettavien miinojen määrä: ").strip())
    except ValueError:
        print("Syötä kentän tiedot vain kokonaislukuina")
    else:
        return leveys, korkeus, miinat


def kaynnista_peli(leveys, korkeus, miinat_lkm):
    """
    Funktio, joka polkaisee pelin käyntiin. Aloitettavan pelin
    tiedot kirjataan ylös tilastoihin. Myös itse miinakenttä
    luodaan ja miinoitetaan. Lopuksi seuraa haravasto-kirjaston
    funktioiden kutsumista pelin käynnistämiseksi.
    """
    luo_kentta(leveys, korkeus)
    miinoita(ikkuna["miinakentta"], ikkuna["tyhjat_ruudut"], miinat_lkm)
    kesto["START_TIME"] = time.time()
    tilastot["ajankohta"] = time.strftime(
        "%H:%M:%S %Y-%m-%d", time.localtime())
    tilastot["lopputulos"]["kentan_koko"] = "{w}x{h}".format(
        w=leveys, h=korkeus)
    tilastot["lopputulos"]["miinat_lkm"] = "{}".format(miinat_lkm)
    haravasto.luo_ikkuna(leveys * 40, korkeus * 40)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aseta_nappain_kasittelija(kasittele_nappain)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aloita()


def main():
    """
    Miinantallaaja-harjoitustyön main()-funktio. Sisältää pelin
    valikkorakenteen ja keskittyy käyttäjän syötteiden virheenkäsittelyyn.
    Kutsuu muita funktiota esim. pelin käynnistämiseksi ja tilastojen
    tarkastelemiseksi. Koko ohjelma myös lopetetaan tämän funktion kautta.
    """
    print("\nTervetuloa Miinantallaajaan! Voit valita seuraavista toiminnoista:")
    print("1. Uusi peli")
    print("2. Tarkastele tilastoja")
    print("3. Lopeta")
    while True:
        try:
            valinta = int(input("\nTee valintasi (1-3): ").strip())
        except ValueError:
            print("Syötä vain kokonaislukuja 1-3")
        else:
            if valinta == 1:
                try:
                    leveys, korkeus, miinat_lkm = kysy_tiedot()
                except TypeError:
                    print("Tiedot annettiin väärässä muodossa!")
                else:
                    if leveys < 2 or korkeus < 2:
                        print("Kenttä on liian pieni!")
                    elif miinat_lkm >= (leveys * korkeus):
                        print(
                            "Liikaa miinoja suhteessa ruutujen määrään! Syötä pienempi luku")
                    elif miinat_lkm <= 0:
                        print("Peliä ei voi pelata ilman miinoja")
                    else:
                        kaynnista_peli(leveys, korkeus, miinat_lkm)
            elif valinta == 2:
                tarkastele_tilastot()
            elif valinta == 3:
                break
            else:
                print("Yritäpä uudestaan")


if __name__ == "__main__":
    """
    Ladataan pelin grafiikat ennen main()-funktiota.
    """
    haravasto.lataa_kuvat("spritet")
    main()
