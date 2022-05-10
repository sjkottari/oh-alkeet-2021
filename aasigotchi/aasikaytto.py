
def nayta_tila(data):
    """
    Tulostaa aasin tilan.
    """
    print("Aasi on {ika} vuotta vanha ja rahaa on {raha} mk.\nKyllaisyys: {masu}\nOnnellisuus: {onni}\nJaksaminen: {jaksu}"
          .format(ika=data["IKÄ"], raha=data["RAHA"], masu=data["KYLLÄISYYS"], onni=data["ONNELLISUUS"], jaksu=data["JAKSAMINEN"]))
    if data["ELÄKE"] == True:
        print("Aasi on jaanyt elakkeelle.")


def pyyda_syote(data):
    if data["ELÄKE"] == True:
        print("Valinnat: q, a")
        while True:
            syote = input("Anna seuraava valinta: ")
            if syote.lower().strip() == 'q' or syote.lower().strip() == 'a':
                break
            print("Virheellinen syote!")
    else:
        print("Valinnat: q, r, k, t")
        while True:
            syote = input("Anna seuraava valinta: ")
            if syote.lower().strip() == 'q' or syote.lower().strip() == 'r' or syote.lower().strip() == 'k' or syote.lower().strip() == 't':
                break
            print("Virheellinen syote!")
    return syote
