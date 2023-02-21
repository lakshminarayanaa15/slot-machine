import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
} #dictionary

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): #evry line has line wch means we're looping through evry row
        symbol = columns[0][line]
        for column in columns: # all the symbols in columns should be same
            symbol_to_check = column[line] # we're going to loop through evry column and check weather they are same
            if symbol is symbol_to_check: # if the symbols are not same we're going to break wch means check the next line
                break
            else:
                winnings += values[symbol] * bet # if they are same they have won the amount wch is multiple of how many times they hav won and how much amount they have bet on
                winning_lines.append(line + 1) # the winning_lines now represents that how much lines they have won

    return winnings, winning_lines       

def get_slot_machine_spin(rows, cols, symbols): #inside we will use the parameter, what we generate inside is what symbol should be there in each column based on the frequency of symbols that we have 
    all_symbols = []  
    for symbol, symbol_count in symbols.items(): # for loops helps to add howmany symbols we have  into the all symbols list, .items gives both the key and value associated
        for _ in range(symbol_count):
            all_symbols.append(symbol) # symbol reffers to A symbol_count reffers to 2 wch gets looped and added to the all_symbols

    columns = [] #this for loop is for that is going to do this for every column
    for _ in range(cols): #picks random value, generate column for every single column (if we have three column, we need to do evrythng inside three times)
        column = []  #column is an empty list
        current_symbols = all_symbols[:] #current symbols is copy of all symbols
        for _ in range(rows): #we loop through the number of value tat we need to generate wch is equal to no. of rows in slot machine
            value = random.choice(current_symbols) #picks random value from the current symbol list
            current_symbols.remove(value) # currnt sumbol removes the value so tat we dont pick it again
            column.append(value) # then the value is added to empty lis of column

        columns.append(column) #how many symbols are inside column is now added to columns
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])): #no. of rows reffer to the no. of symbols in the columns
        for i, column in enumerate(columns): #looping through all of the items inside of column
            if i != len(columns) - 1: #the lenght column -1 is the maximum index tat we have the acces to elemnt in the column, if length is 3 thn the max index is 2
                print(column[row], end=" | ") #if this is a not a end comment print |
            else:
                print(column[row], end="")

        print()
        
def deposit():
    while True:
        amount = input("what would you like to deposit ? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("enter the number of lines to bet on (1-"+ str(MAX_LINES)+") ! ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Line number must be within 1-3.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
     while True:
        amount = input("what would you like to bet on each line ? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")
            
     return amount

def spin(balance): # these stuff will say things based on the output
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet on that amount, your current balance is :{balance}")
        else:
            break           
    print(f"You are betting {bet} on {lines} lines. Total bet is equal to {total_bet} ")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet # says how much they hav won or lost

def main(): # these code will say the same on evry execution 
    balance = deposit() 
    while True:
        print(f"current balance is {balance}")
        answer = input("Press enter to play or q to quit.")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with {balance}")    
   

main()