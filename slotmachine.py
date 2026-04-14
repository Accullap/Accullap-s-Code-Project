import random

X = 3   # correlation: global value X makes MAX_LINES and ROWS equal for simplified changing in the size of the Slotmachine and Text

MAX_LINES = X   # correlation in text with ROWS
MIN_LINES = 1
MAX_BET = 100
MIN_BET = 1

ROWS = X # correlation in text with MAX_LINES
COLS = 3

symbol_count = {
    "A": 3,
    "B": 6,
    "C": 9,
    "D": 12
}

symbol_value = {
    "A": 16,
    "B": 8,
    "C": 4,
    "D": 2,
}


def checkwinnings(columns, lines, bet, values):
    return


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = "|")
            else:
                print(column[row], end = "")

        print()


def deposit():
    while True:
        amount = input("What amount would you like to deposit? €")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a number!")

    return amount


def get_number_of_lines():
     while True:
        lines = input("Enter the number of lines you want to bet on: 1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number!")

     return lines

    
def get_bet():
     while True:
        amount = input("What would you like to bet on each line? €")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be between" f"{MIN_BET}€ - {MAX_BET}€")
        else:
            print("Please enter a number!")

     return amount
    

def spin(balance):
    return


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:

        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You dont have that much money. Your current balance is " f"{balance}€")
        else:
            break

    print("You are betting " f"{bet}€ on {lines} lines. Total bet: {total_bet}€")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    





main()