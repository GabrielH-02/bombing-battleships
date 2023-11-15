import random

HR_LINE = str('-' * 50)


def welcome_statement():
    print('\n Welcome to Bombing Battleships'.upper())
    print(HR_LINE)
    print(' How to Play:')
    print(HR_LINE)
    print('   1. Insert your name')
    print('   2. Select a singular number for the size of the grid')
    print('   3. Select and guess the row, and column to bomb')
    print('   4. Try and beat the computer')
    print('   Note: Consider the size of the grid since there are 4 ships \n')
    print(HR_LINE)
    print(' Key: \n')
    print('   @ = Your Ship')
    print('   X = Space')
    print('   * = Hit')
    print('   O = Missed\n')
    print(HR_LINE)


def get_player_name():
    player_name = input("What's your name: \n")
    return player_name


def print_board(board):
    for row in board:
        print(" ".join(row))


def get_grid_size():
    try:
        size = int(input("\nEnter the grid size: \n"))
        if size < 3:
            raise ValueError("Grid size must be 3 or greater.")
        return size
    except ValueError as e:
        print(f"Invalid input: {e}")
        return get_grid_size()


def player_guess(arg):
    try:
        guess_row = int(input(f"Guess Row: \n"))
        guess_col = int(input(f"Guess Col: \n"))
        if 0 <= guess_row <= arg and 0 <= guess_col <= arg:
            return guess_row, guess_col
        else:
            print("Please enter valid coordinates.")
            return player_guess(arg)
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return player_guess(arg)


def ran_row_col(num):
    return random.randint(0, num)


def play():
    # Calls the welcome statement
    welcome_statement()
    # Calls and defines player name input
    player_name = get_player_name()
    # Calls and defines grid size input
    size = get_grid_size()

    # defines size and define grid spaces 
    player_board = [["~"] * size for _ in range(size)]
    computer_board = [["~"] * size for _ in range(size)]

    # prints out player and computer boards
    print(f"\n{player_name}'s Board:\n")
    print_board(player_board)

    print(HR_LINE)

    print("\nComputer's Board:\n")
    print_board(computer_board)

    
    

play()
