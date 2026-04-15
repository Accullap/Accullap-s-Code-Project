board = ["   "] * 9
currentplayer = " X "
winner = None
gamerunning = True


def printBoard():
    for i in range(0, 9, 3):
        print(f"{board[i]}|{board[i+1]}|{board[i+2]}")
        if i < 6:
            print("---+---+---")


def playerInput():
    while True:
        print()
        if currentplayer == " X ":
            inp = int(input(f"Enter a number 1-9 Player (X): "))
        else:
            inp = int(input(f"Enter a number 1-9 Player (O): "))
        print()
        if inp >= 1 and inp <= 9 and board[inp-1] == "   ":
            board[inp-1] = currentplayer
            break
        else:
            print("Oops! Try again!\n")
            printBoard()


def checkHorizontal():
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "   ") or \
       (board[3] == board[4] == board[5] and board[3] != "   ") or \
       (board[6] == board[7] == board[8] and board[6] != "   "):
        winner = currentplayer
        return True


def checkRow():
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "   ") or \
       (board[1] == board[4] == board[7] and board[1] != "   ") or \
       (board[2] == board[5] == board[8] and board[2] != "   "):
        winner = currentplayer
        return True


def checkDiagonal():
    global winner
    if (board[0] == board[4] == board[8] and board[0] != "   ") or \
       (board[2] == board[4] == board[6] and board[2] != "   "):
        winner = currentplayer
        return True


def checkTie():
    global gamerunning
    if "   " not in board:
        printBoard()
        print("Its a tie")
        gamerunning = False


def checkWin():
    if checkDiagonal() or checkHorizontal() or checkRow():
        print(f"The winner is {winner}\n")


def switchPlayer():
    global currentplayer
    if currentplayer == " X ":
        currentplayer = " O "
    else:
        currentplayer = " X "


while gamerunning:
    printBoard()
    if winner != None:
        break
    playerInput()
    checkWin()
    checkTie()
    switchPlayer()
