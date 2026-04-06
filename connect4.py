board = ["   "] * 42
currentplayer = " X "
winner = None
gamerunning = True


def printBoard():
    for i in range(0, 42, 7):
        print(
            f"{board[i]}|{board[i+1]}|{board[i+2]}|{board[i+3]}|{board[i+4]}|{board[i+5]}|{board[i+6]}")
        if i < 35:
            print("---+---+---+---+---+---+---")


# def playerInput():
#     while True:
#         print()
#         if currentplayer == " X ":
#             inp = int(input(f"Enter a number 1-9 Player (X): "))
#         else:
#             inp = int(input(f"Enter a number 1-9 Player (O): "))
#         print()
#         if inp >= 1 and inp <= 9 and board[inp-1] == "   ":
#             board[inp-1] = currentplayer
#             break
#         else:
#             print("Oops! Try again!\n")
#             printBoard()

def checkHorizontal():
    global winner
    # Check column 1 - 6 every 4 lines is every pssibility to win for first column.
    if (board[0] == board[1] == board[2] == board[3] and board[0] != "   ") or \
        (board[1] == board[2] == board[3] == board[4] and board[1] != "   ") or \
        (board[2] == board[3] == board[4] == board[5] and board[2] != "   ") or \
        (board[3] == board[4] == board[5] == board[6] and board[3] != "   ") or \
        (board[7] == board[8] == board[9] == board[10] and board[7] != "   ") or \
        (board[8] == board[9] == board[10] == board[11] and board[8] != "   ") or \
        (board[9] == board[10] == board[11] == board[12] and board[9] != "   ") or \
        (board[10] == board[11] == board[12] == board[13] and board[10] != "   ") or \
        (board[14] == board[15] == board[16] == board[17] and board[14] != "   ") or \
        (board[15] == board[16] == board[17] == board[18] and board[15] != "   ") or \
        (board[16] == board[17] == board[18] == board[19] and board[16] != "   ") or \
        (board[17] == board[18] == board[19] == board[20] and board[17] != "   ") or \
        (board[21] == board[22] == board[23] == board[24] and board[21] != "   ") or \
        (board[22] == board[23] == board[24] == board[25] and board[22] != "   ") or \
        (board[23] == board[24] == board[25] == board[26] and board[23] != "   ") or \
        (board[24] == board[25] == board[26] == board[27] and board[24] != "   ") or \
        (board[28] == board[29] == board[30] == board[31] and board[28] != "   ") or \
        (board[29] == board[30] == board[31] == board[32] and board[29] != "   ") or \
        (board[30] == board[31] == board[32] == board[33] and board[30] != "   ") or \
        (board[31] == board[32] == board[33] == board[34] and board[31] != "   ") or \
        (board[35] == board[36] == board[37] == board[38] and board[35] != "   ") or \
        (board[36] == board[37] == board[38] == board[39] and board[36] != "   ") or \
        (board[37] == board[38] == board[39] == board[40] and board[37] != "   ") or \
            (board[38] == board[39] == board[40] == board[41] and board[38] != "   "):
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

# def checkTie():
#     global gamerunning
#     if "   " not in board:
#         printBoard()
#         print("Its a tie")
#         gamerunning = False

# def checkWin():
#     if checkDiagonal() or checkHorizontal() or checkRow():
#         print(f"The winner is {winner}\n")

# def switchPlayer():
#     global currentplayer
#     if currentplayer == " X ":
#         currentplayer = " O "
#     else:
#         currentplayer = " X "

# while gamerunning:
#     printBoard()
#     if winner != None:
#         break
#     playerInput()
#     checkWin()
#     checkTie()
#     switchPlayer()
