import numpy as np
import matplotlib as plt

# moodle aufgaben Tut 2

list = [1,2,3,4,5,6]

def summe(list):
    return np.sum(list)

resultat = summe(list)

# print(resultat)

# calculator

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
        print("Ungültiges Zeichen, nur +, -, *, / erlaubt")
        symbol = input("Neues Symbol: ")


# Moodle task 3 rectangle area

