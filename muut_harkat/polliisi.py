try:
    matka = float(input("Anna auton kulkema matka (m): "))
    aika = float(input("Anna matkaan kulunut aika (s): "))
except ValueError:
    print("Vähemmän donitseja, enemmän puhtaita numeroita.")
else:
    nopeus = ( matka / aika ) * 3.6
    print("{:.2f} metriä {:.2f} sekunnissa kulkeneen auton nopeus on {:.2f} km/h."
          .format(matka, aika, nopeus))