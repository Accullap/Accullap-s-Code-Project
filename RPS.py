import random

game = {1: "Rock", 2: "Paper", 3: "Scissors"}       # connects numbers to words
choices = {"Rock": 1, "Paper": 2, "Scissors": 3}    # connects words to numbers


def userinput():
    while True: # loop until userinput == Rock/Paper/Scissors and 1 succesfull Game played
            try: # try --> run this code | except --> if it crashes do this instead
                print(" ")
                num = choices[input("Choose between Rock, Paper and Scissors: \n").capitalize()]
                print(" ")
                botnumber = random.randint(1,3)
                if num == 1:
                    if botnumber == 1:
                        print("Bot chooses Rock too")
                        print("")
                        print("--> Draw\n")
                    else:
                        if botnumber == 2:
                            print("Bot's " + game[botnumber] + " beats your " + game[num]) # in this case game[botnumber] is game[2] which is Paper | game[num] is game[1] which is Rock
                            print(" ")
                        else:
                            print("Your " + game[num] + " beats Bot's " + game[botnumber]) # in this case game[num] is game[1] which is Rock | game[botnumber] is game[3] which is Scissors
                            print(" ")

                elif num == 2:
                    if botnumber == 1:
                        print("Your " + game[num] + " beats Bot's " + game[botnumber]) # in this case game[num] is game[2] which is Paper | game[botnumber] is game[1] which is Rock
                        print(" ")
                    else:
                        if botnumber == 2:
                            print("Bot chooses Paper too")
                            print(" ")
                            print("--> Draw\n")
                        else:
                            print("Bot's " + game[botnumber] + " beats your " + game[num]) # in this case game[botnumber] is game[3] which is Scissors | game[num] is game[2] which is Paper
                            print(" ")
                elif num == 3:
                    if botnumber == 1:
                        print("Bot's " + game[botnumber] + " beats your " + game[num]) # in this case game[botnumber] is game[1] which is Rock | game[num] is game[3] which is Scissors
                        print(" ")
                    else:
                        if botnumber == 2:
                            print("Your " + game[num] + " beats Bot's " + game[botnumber]) # in this case game[num] is game[3] which is Scissors | game[botnumber] is game[2] which is Paper
                            print(" ")
                        else:
                            print("Bot chooses Scissors too")
                            print(" ")
                            print("--> Draw\n")
                break   # makes code stop if one Game played succesfull
            except: # try --> run this code | except --> if it crashes do this instead and ask again
                    print(" ")
                    print("please write one of the following: Rock, Paper or Scissors")

userinput()


