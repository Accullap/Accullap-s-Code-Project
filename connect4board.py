board = ["   "] * 42


def printBoard():
    for i in range(0, 42, 7):
        print(
            f"{board[i]}|{board[i+1]}|{board[i+2]}|{board[i+3]}|{board[i+4]}|{board[i+5]}|{board[i+6]}")
        if i < 35:
            print("---+---+---+---+---+---+---")


printBoard()
