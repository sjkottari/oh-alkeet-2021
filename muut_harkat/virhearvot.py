
def suodata_virhearvot(mittaustulokset, reuna):
    for tulos in mittaustulokset[:]:
        if tulos > reuna:
            mittaustulokset.remove(tulos)


mittaukset = [12.2, 54.2, 42345.2, 23534.1, 55.7, 8982.4]
suodata_virhearvot(mittaukset, 8000)
print(mittaukset)
