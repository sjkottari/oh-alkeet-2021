
def muotoile_heksaluvuksi(luku, hex_pituus):
    hex_pituus = int(hex_pituus / 4)
    hex_luku = str(hex(luku))
    return hex_luku.removeprefix('0x').zfill(hex_pituus)

try:
    luku = int(input("Anna kokonaisluku: "))
    hex_pituus = int(input("Anna heksaluvun pituus (bittien lukumäärä): "))
except ValueError:
    print("Kokonaisluku kiitos")
else:
    print(muotoile_heksaluvuksi(luku, hex_pituus))