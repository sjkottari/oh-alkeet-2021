
def nayta_tulokset(tiedosto):
    tulokset = []
    with open(tiedosto) as kohde:
        for i, rivi in enumerate(kohde.readlines()):
            tulokset.append(rivi)
            pelaaja1, pelaaja2, pisteet1, pisteet2 = tulokset[i].split(",")
            print("{pelaaja1} {pisteet1} - {pisteet2} {pelaaja2}".format(
                                                                pelaaja1=pelaaja1.strip(),
                                                                pisteet1=pisteet1.strip(),
                                                                pisteet2=pisteet2.strip(),
                                                                pelaaja2=pelaaja2.strip()
            ))


nayta_tulokset("hemulicup.csv")
