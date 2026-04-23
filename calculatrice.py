zahl1 = float(input("Erste Zahl: "))
symbol = input("Symbol (+, -, *, /): ")
zahl2 = float(input("Zweite Zahl: "))

while True:
    if symbol == "/" and zahl2 == 0:
        print("Division durch 0 nicht möglich")
        zahl2 = float(input("Neue zweite Zahl: "))

    elif symbol == "+":
        print(zahl1 + zahl2)
        break

    elif symbol == "-":
        print(zahl1 - zahl2)
        break

    elif symbol == "*":
        print(zahl1 * zahl2)
        break

    elif symbol == "/":
        print(zahl1 / zahl2)
        break

    else:
        print("Ungültiges Zeichen! Nur +, -, *, / erlaubt!")
        symbol = input("Neues Symbol: ")
