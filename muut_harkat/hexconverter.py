heksa = ""
luku = 4451
while luku > 0:
    luku, bitti = divmod(luku, 16)           # Lasketaan osamäärä ja jakojäännös
    heksa = str(bitti) + heksa              # Huom: muista liittää uusi numero luvu *alkuun*
    
print(heksa)
