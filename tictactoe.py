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


show()
