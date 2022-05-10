
def pyyda_syote(syote_pyynto, virheviesti):
    """
    Kysyy käyttäjältä kokonaislukua käyttäen kysymyksenä parametrina annettua
    merkkijonoa. Virheellisen syötteen kohdalla käyttäjälle näytetään toisena
    parametrina annettu virheilmoitus. Käyttäjän antama kelvollinen syöte
    palautetaan kokonaislukuna.
    """
    while True:
        try:
            kokonaisluku = int(input(syote_pyynto))
            if kokonaisluku <= 1:
                raise ValueError
            break
        except ValueError:
            print(virheviesti)
    return kokonaisluku


def tarkista_alkuluku(tarkistettava_luku):
    """
    Tarkistaa onko parametrina annettu luku alkuluku. Palauttaa False jos luku ei
    ole alkuluku; jos luku on alkuluku palautetaan True
    """
    for i in range(2, tarkistettava_luku):
        if tarkistettava_luku % i == 0:
            return False
    return True

luku = pyyda_syote(
    "Anna kokonaisluku, joka on suurempi kuin 1: ",
    "Pieleen meni"
)
tulos = tarkista_alkuluku(luku)
if tulos:
    print("Kyseessa on alkuluku")
else:
    print("Kyseessa ei ole alkuluku")
