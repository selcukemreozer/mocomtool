import os

def clear_terminal(): # clear the terminal
    if os.system == 'nt': # Windows
        os.system('cls')
        
    else: # Linux and Mac
        os.system('clear')
        
def position(column:int, row:int):
    # Move cursor to row {row}, column {column}
    print(f'\033[{row};{column}H', end='')
