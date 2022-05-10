import math
import pyglet
import random
import haravasto

LEVEYS = 800
KORKEUS = 600
ANIMAATIONOPEUS = 0.1

tila = {
    "pelaaja": {
        "x": 0,
        "y": 0,
        "suunta": 0,
        "nopeus": 0,
        "kiihtyvyys": 0,
        "kuva": 0
    },
    "aika": 0.0
}

def muunna_xy_koordinaateiksi(a, r):
    x = int(round(math.cos(a) * r))
    y = int(round(math.sin(a) * r))
    return x, y

def paivita_sijainti(hahmo):
    dx, dy = muunna_xy_koordinaateiksi(math.radians(hahmo["suunta"]), hahmo["nopeus"])
    hahmo["x"] += dx
    hahmo["y"] += dy

def aseta_suunta(hahmo, kohde_x, kohde_y):
    etaisyys_x = kohde_x - hahmo["x"]
    etaisyys_y = kohde_y - hahmo["y"]
    hahmo["suunta"] = math.degrees(math.atan2(etaisyys_y, etaisyys_x))

def kasittele_hiiri(x, y, nappi, muokkausnapit):
    aseta_suunta(tila["pelaaja"], x, y)
    tila["pelaaja"]["nopeus"] = 0

def paivita_peli(kulunut_aika):
    tila["pelaaja"]["nopeus"] += tila["pelaaja"]["kiihtyvyys"]
    tila["pelaaja"]["kuva"] = (tila["pelaaja"]["kuva"] + ANIMAATIONOPEUS) % 2
    paivita_sijainti(tila["pelaaja"])
    tila["aika"] += kulunut_aika
    
def piirra_peli():
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    haravasto.lisaa_piirrettava_ruutu(int(tila["pelaaja"]["kuva"]), tila["pelaaja"]["x"], tila["pelaaja"]["y"])
    haravasto.piirra_ruudut()

def luo_pelaaja():
    tila["pelaaja"] = {
        "x": random.randint(0, LEVEYS - 1),
        "y": random.randint(0, KORKEUS - 1),
        "suunta": 0,
        "nopeus": 0,
        "kiihtyvyys": 0.2,
        "kuva": 0
    }

def lataa_kuvat(polku):
    pyglet.resource.path = [polku]
    kuvat = {
        "0": pyglet.resource.image("plus_1.png"),
        "1": pyglet.resource.image("plus_2.png")
    }
    haravasto.grafiikka["kuvat"] = kuvat

def aloita_peli():
    luo_pelaaja()
    haravasto.luo_ikkuna(LEVEYS, KORKEUS)
    haravasto.aseta_piirto_kasittelija(piirra_peli)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aseta_toistuva_kasittelija(paivita_peli)
    haravasto.aloita()

if __name__ == "__main__":
    lataa_kuvat("spritet")
    aloita_peli()
