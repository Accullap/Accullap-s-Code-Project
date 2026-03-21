import random

def userinput():
    randomnum = random.randint(1,100)
    while True:
        print(" ")
        num = int(input("Guess the Number from 1-100:\n"))
        if num == randomnum:
            print(" ")
            print("God Job!\n")
            break
        elif num > randomnum:
            print("Hint: Lower")
        else: 
            print("Hint: Higher")

userinput()