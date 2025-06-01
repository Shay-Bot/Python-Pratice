import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_Slot_machine_spin(rows, cols, sybmols):
    all_symbols = []
    for symbol, symbol_count in sybmols.items():
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

def print_slot_machine(coloums):
    for row in range(len(coloums[0])):
        for i, coloum in enumerate(coloums):
            if i != len(coloums) - 1:
                print(coloum[row], end=" | ")
            else:
                print(coloum[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to Deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number")    

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the numbers of lines to bet on (1 - "+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines")
        else:
            print("Please enter a number")    

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to Bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET} ")
        else:
            print("Please enter a number")    

    return amount




def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You dont have enough amount, your current balance is {balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines}. Total bet is equal to: ${total_bet} ")

    slots = get_Slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()
