
def laskutoimitus(operaatio, operandi1, operandi2):
    if operaatio == '+':
        return operandi1 + operandi2
    elif operaatio == '-':
        return operandi1 - operandi2
    elif operaatio == '*':
        return operandi1 * operandi2
    elif operaatio == '/':
        if operandi2 == 0:
            print("Tällä ohjelmalla ei pääse äärettömyyteen")
        else:
            return operandi1 / operandi2

def kysy_luvut(op):
    try:
        luku1 = float(input("Anna luku 1: "))
        luku2 = float(input("Anna luku 2: "))
    except ValueError:
        print("Ei tämä ole mikään luku")
    else:
        print("Tulos: {}".format(laskutoimitus(op, luku1, luku2)))

def main():
    operaatio = input("Valitse operaatio (+, -, *, /): ")
    if operaatio != ('+' or '-' or '*' or '/'):
        print("Operaatiota ei ole olemassa")
    else:
        kysy_luvut(operaatio)

if __name__ == "__main__":
    main()
