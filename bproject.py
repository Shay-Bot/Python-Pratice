MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

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
        amount = input("What would you like to Bet? $")
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

main()