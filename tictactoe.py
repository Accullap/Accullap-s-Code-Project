import random

board = ["   "] * 9


def show():
    for i in range(0, 9, 3):
        print(f"{board[i]}|{board[i+1]}|{board[i+2]}")
        if i < 6:
            print("---+---+---")


def check(player):
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8),
            (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]


play_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def play():
    while True:
        try:
            number = int(input("Give me a number: "))
            if number < 10:
                if number <= 3:
                    x = 0
                elif number > 3 and number <= 6:
                    x = 1
                else:
                    x = 2

                y = (number - 1) % 3

                print(f"number vertical: {x}")
                print(f"number horizontal: {y}")
            else:
                print("only numbers from 1-9")
        except:
            print("only numbers allowed")


play()
