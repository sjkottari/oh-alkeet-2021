
def valitse_lukumaara(inventaario):
    return inventaario[1]

inventaario = [("aasi", 12), ("muumimuki", 1), ("varsikirves", 4)]

inventaario.sort(key=valitse_lukumaara, reverse=True)

print(inventaario)
