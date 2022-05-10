
huone = [['N', ' ', ' ', ' ', ' '],
         ['N', 'N', 'N', 'N', ' '],
         ['N', ' ', 'N', ' ', ' '],
         ['N', 'N', 'N', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ']]


def laske_ninjat(x, y, kentta):
    """
    Laskee annetussa huoneessa yhden ruudun ympärillä olevat ninjat ja palauttaa
    niiden lukumäärän. Funktio toimii sillä oletuksella, että valitussa ruudussa ei
    ole ninjaa - jos on, sekin lasketaan mukaan.
    """
    ninjat = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if -1 < i < len(kentta) and -1 < j < len(kentta[0]):
                #print(i, j)
                if kentta[i][j] == 'N':
                    ninjat = ninjat + 1

    return ninjat


def main():
    """
    Ohjelman paaohjelma
    """
    ninja_lkm = laske_ninjat(1, 2, huone)
    print("Loytyi {} ninjaa".format(ninja_lkm))


main()
