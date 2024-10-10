import random


MAX_Num = 3
MAX_BET = 100
MIN_BET = 1


ROWS = 3
COLS = 3


symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_slotmachine_spin(rows, cols, symbols):
    #gennerate what slots in each col
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #.items referencing the values
        for _ in range(symbol_count):
            all_symbols.append(symbol) #looping thru symbol count and throwing it into the list
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #split 
        for _ in range(rows): # go thru what slots are in our slot machine whixch is based on what w efchoose
            value = random.choice(current_symbols)#random from the list which we added in that list 
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)   


    return columns     

def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()      #print new line char each time  

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol == symbol_to_check:
                break

        else: 
            winnings += values[symbol] * bet
            winnings_lines.append(lines)

    return winnings, winnings_lines    




def deposit():
    while True:
        amount = input("How much to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount needs to be above 0")
        else:
            print("Try again")
    return amount

def get_number():
    while True:
        row = input(
            "Give an amount of rows to bet on (1- " + str(MAX_Num) + ")? ")
        if row.isdigit():
            row = int(row)
            if 1 <= row <= MAX_Num:
                break
            else:
                print("Amount must be between 1-3")
        else:
            print("Enter a number") 
    return row  

def get_bet():
    while True:
        amount = input("How much to bet? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Try again")
    return amount


def spin(balance):
    row = get_number()
    while True:
        bet = get_bet()
        total = bet * row

        if total > balance:
            print(f"You dont have enough money to bet that, you have #{balance}")
        else:
            break
    print(f"You betted ${bet} on {row} rows, Total bet is : ${total}")
    #print(balance, row)
#
    slots = get_slotmachine_spin(ROWS, COLS, symbol_count)
    print_slots(slots)
    winnings, winning_lines = check_winnings(slots, row, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on", *winning_lines) #*pass every line from winning_lines list to this print function, 
    ##so 1 and 2, it will be passed
    return winning_lines - total

    
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer= input("Press enter to spin or Q to quit")
        if answer == "Q":
            break
        balance += spin()


        print("You finished with ${balance}")

main()



        
        
                
