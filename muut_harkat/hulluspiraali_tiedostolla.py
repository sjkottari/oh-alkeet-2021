import turtle as t

def piirra_spiraali(vari, kaaret, alkusade, sade_kasvu, viiva_paksuus=1):
    t.color(vari)
    t.pensize(viiva_paksuus)

    t.down()

    for i in range(kaaret):
        t.circle(alkusade, 90)
        alkusade += sade_kasvu

def piirra_tiedostosta(tiedosto):
    try:
        with open(tiedosto) as lahde:
            for rivi in lahde.readlines():
                try:
                    vari, kaaret, alkusade, sade_kasvu, viiva_paksuus = rivi.split(',')
                    kaaret = int(kaaret)
                    alkusade = int(alkusade)
                    sade_kasvu = float(sade_kasvu)
                    viiva_paksuus = int(viiva_paksuus.strip())
                    piirra_spiraali(vari, kaaret, alkusade, sade_kasvu, viiva_paksuus)
                except ValueError:
                    print("Rivia ei saatu luettua")
    except IOError:
        print("Kohdetiedostoa ei voitu avata")


piirra_tiedostosta("spiraali.txt")
t.done()
