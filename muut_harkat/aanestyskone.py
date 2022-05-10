verouudistus = {
    "jaa": 0,
    "ei": 0,
    "eos": 0,
    "virhe": 0
}
nalle_puh_presidentiksi = {
    "jaa": 12,
    "ei": 0,
    "eos": 5,
    "virhe": 4
}

def aanesta(sanakirja):
    valinta = input("""Anna äänesi, vaihtoehdot ovat:\njaa, ei, eos\n:""")
    
    valinta = valinta.lower().strip()
    
    if valinta in sanakirja:
        aani = sanakirja.get(valinta)
        aani = aani + 1
        sanakirja[valinta] = aani
    else:
        virhe = sanakirja.get("virhe")
        virhe = virhe + 1
        sanakirja["virhe"] = virhe
    
def nayta_tulokset(sanakirja):

    hash_merkki = "#"
    jaa = ""
    ei = ""
    eos = ""
    virhe = ""
    
    for x in range(sanakirja["jaa"]):
        jaa = jaa + hash_merkki
    
    for x in range(sanakirja["ei"]):
        ei = ei + hash_merkki
        
    for x in range(sanakirja["eos"]):
        eos = eos + hash_merkki
        
    for x in range(sanakirja["virhe"]):
        virhe = virhe + hash_merkki
        
    print("Jaa: {}".format(jaa))
    print("Ei: {}".format(ei))
    print("Eos: {}".format(eos))
    print("Virhe: {}".format(virhe))
    
print("Suoritetaanko verouudistus?")
aanesta(verouudistus)
nayta_tulokset(verouudistus)

print("Nalle Puh presidentiksi?")
aanesta(nalle_puh_presidentiksi)
nayta_tulokset(nalle_puh_presidentiksi)
