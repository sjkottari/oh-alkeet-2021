
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
            break
        except ValueError:
            print(virheviesti)
    return kokonaisluku


luku = pyyda_syote(
    "Anna kokonaisluku: ",
    "Et antanut kokonaislukua"
)
print("Annoit kokonaisluvun {}! Nohevaa toimintaa!".format(luku))
hemulit = pyyda_syote(
    "Montako hemulia mahtuu muumitaloon? ",
    "Tämä ei ollut kelvollinen hemulien lukumäärä!"
)
print("Muumitaloon mahtuu {} hemulia".format(hemulit))
