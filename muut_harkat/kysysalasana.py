
def kysy_salasana():
    salasana = ""
    while True:
        salasana = input("Kirjoita salasana: ")
        if len(salasana) >= 8:
            break
        else:
            print("Salasanan tulee olla vähintään 8 merkkiä pitkä")
    return salasana


print(kysy_salasana())
