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


def playerInput():
    while True:
        print()
        if currentplayer == " X ":
            inp = int(input("Enter a number 1-7 Player (X): "))
        else:
            inp = int(input("Enter a number 1-7 Player (O): "))

        if inp >= 1 and inp <= 7:

            # now comes inp == 1
            if inp == 1 and board[35] == "   ":
                board[35] = currentplayer
                break
            elif inp == 1 and all(board[i] != "   " for i in [35]) and board[28] == "   ":
                board[28] = currentplayer
                break
            elif inp == 1 and all(board[i] != "   " for i in [35, 28]) and board[21] == "   ":
                board[21] = currentplayer
                break
            elif inp == 1 and all(board[i] != "   " for i in [35, 28, 21]) and board[14] == "   ":
                board[14] = currentplayer
                break
            elif inp == 1 and all(board[i] != "   " for i in [35, 28, 21, 14]) and board[7] == "   ":
                board[7] = currentplayer
                break
            elif inp == 1 and all(board[i] != "   " for i in [35, 28, 21, 14, 7]) and board[0] == "   ":
                board[0] = currentplayer
                break
            else:
                print("Oops! Try again!")

# now comes inp == 2:
            if inp == 2 and board[36] == "   ":
                board[36] = currentplayer
                break
            elif inp == 2 and all(board[i] != "   " for i in [36]) and board[29] == "   ":
                board[29] = currentplayer
                break
            elif inp == 2 and all(board[i] != "   " for i in [36, 29]) and board[22] == "   ":
                board[22] = currentplayer
                break
            elif inp == 2 and all(board[i] != "   " for i in [36, 29, 22]) and board[15] == "   ":
                board[15] = currentplayer
                break
            elif inp == 2 and all(board[i] != "   " for i in [36, 29, 22, 15]) and board[8] == "   ":
                board[8] = currentplayer
                break
            elif inp == 2 and all(board[i] != "   " for i in [36, 29, 22, 15, 8]) and board[1] == "   ":
                board[1] = currentplayer
                break
            else:
                print("Oops! Try again!")

# now comes inp == 3:
            if inp == 1 and board[35] == "   ":
                board[35] = currentplayer
                break
            elif inp == 1 and all(board[i] != "   " for i in [35]) and board[28] == "   ":
                board[28] = currentplayer
                break
            elif inp == 1 and all(board[i] != "   " for i in [35, 28]) and board[21] == "   ":
                board[21] = currentplayer
                break
            elif inp == 1 and all(board[i] != "   " for i in [35, 28, 21]) and board[14] == "   ":
                board[14] = currentplayer
                break
            elif inp == 1 and all(board[i] != "   " for i in [35, 28, 21, 14]) and board[7] == "   ":
                board[7] = currentplayer
                break
            elif inp == 1 and all(board[i] != "   " for i in [35, 28, 21, 14, 7]) and board[0] == "   ":
                board[0] = currentplayer
                break
            else:
                print("Oops! Try again!")


# input needs to be 1-7 for every row, needs to take accout gravity, e.g. input 1 needs spot is then 35 and if input is 1 again then != 35but 28
# def playerInput():
#     while True:
#         print()
#         if currentplayer == " X ":
#             inp = int(input(f"Enter a number 1-7 Player (X): "))
#         else:
#             inp = int(input(f"Enter a number 1-7 Player (O): "))
#         print()
#         if inp >= 1 and inp <= 7 and board[inp-1] == "   ":
#             board[inp-1] = currentplayer
#             break
#         else:
#             print("Oops! Try again!\n")
#             printBoard()


def checkHorizontal():
    global winner
    # Check column 1 - 6 every 4 lines is every p0ssibility to win for first column.
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
    # Check row 1 - 7 every 3 lines is every possibility to win for first row.
    if (board[0] == board[7] == board[14] == board[21] and board[0] != "   ") or \
        (board[7] == board[14] == board[21] == board[28] and board[7] != "   ") or \
        (board[14] == board[21] == board[28] == board[35] and board[14] != "   ") or \
        (board[1] == board[8] == board[15] == board[22] and board[1] != "   ") or \
        (board[8] == board[15] == board[22] == board[29] and board[8] != "   ") or \
        (board[15] == board[22] == board[29] == board[36] and board[15] != "   ") or \
        (board[2] == board[9] == board[16] == board[23] and board[2] != "   ") or \
        (board[9] == board[16] == board[23] == board[30] and board[9] != "   ") or \
        (board[16] == board[23] == board[30] == board[37] and board[16] != "   ") or \
        (board[3] == board[10] == board[17] == board[24] and board[3] != "   ") or \
        (board[10] == board[17] == board[24] == board[31] and board[10] != "   ") or \
        (board[17] == board[24] == board[31] == board[38] and board[17] != "   ") or \
        (board[4] == board[11] == board[18] == board[25] and board[4] != "   ") or \
        (board[11] == board[18] == board[25] == board[32] and board[11] != "   ") or \
        (board[18] == board[25] == board[32] == board[39] and board[18] != "   ") or \
        (board[5] == board[12] == board[19] == board[26] and board[5] != "   ") or \
        (board[12] == board[19] == board[26] == board[33] and board[12] != "   ") or \
        (board[19] == board[26] == board[33] == board[40] and board[19] != "   ") or \
        (board[6] == board[13] == board[20] == board[27] and board[6] != "   ") or \
        (board[13] == board[20] == board[27] == board[34] and board[13] != "   ") or \
            (board[20] == board[27] == board[34] == board[41] and board[20] != "   "):
        winner = currentplayer
        return True


def checkDiagonal():
    global winner
    # Check diagonal first 12 lines -> top left to bottem right then last 12 lines -> top right to bottom left
    if (board[0] == board[8] == board[16] == board[24] and board[0] != "   ") or \
        (board[1] == board[9] == board[17] == board[25] and board[1] != "   ") or \
        (board[2] == board[10] == board[18] == board[26] and board[2] != "   ") or \
        (board[3] == board[11] == board[19] == board[27] and board[3] != "   ") or \
        (board[7] == board[15] == board[23] == board[31] and board[7] != "   ") or \
        (board[8] == board[16] == board[24] == board[32] and board[8] != "   ") or \
        (board[9] == board[17] == board[25] == board[33] and board[9] != "   ") or \
        (board[10] == board[18] == board[26] == board[34] and board[10] != "   ") or \
        (board[14] == board[22] == board[30] == board[38] and board[14] != "   ") or \
        (board[15] == board[23] == board[31] == board[39] and board[15] != "   ") or \
        (board[16] == board[24] == board[32] == board[40] and board[16] != "   ") or \
        (board[17] == board[25] == board[33] == board[41] and board[17] != "   ") or \
        (board[3] == board[9] == board[15] == board[21] and board[3] != "   ") or \
        (board[4] == board[10] == board[16] == board[22] and board[4] != "   ") or \
        (board[5] == board[11] == board[17] == board[23] and board[5] != "   ") or \
        (board[6] == board[12] == board[18] == board[24] and board[6] != "   ") or \
        (board[10] == board[16] == board[22] == board[28] and board[10] != "   ") or \
        (board[11] == board[17] == board[23] == board[29] and board[11] != "   ") or \
        (board[12] == board[18] == board[24] == board[30] and board[12] != "   ") or \
        (board[13] == board[19] == board[25] == board[31] and board[13] != "   ") or \
        (board[17] == board[23] == board[29] == board[35] and board[17] != "   ") or \
        (board[18] == board[24] == board[30] == board[36] and board[18] != "   ") or \
        (board[19] == board[25] == board[31] == board[37] and board[19] != "   ") or \
            (board[20] == board[26] == board[32] == board[38] and board[20] != "   "):
        winner = currentplayer
        return True


# still need to add if no possibility to win but "   " still in board -> gamerunning = False
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
