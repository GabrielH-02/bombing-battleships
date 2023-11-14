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


def play():
    welcome_statement()
    player_name = get_player_name()
    size = get_grid_size()

    player_board = [["~"] * size for _ in range(size)]
    computer_board = [["~"] * size for _ in range(size)]

    print(f"\n{player_name}'s Board:\n")
    print_board(player_board)
    print(HR_LINE)
    print("\nComputer's Board:\n")
    print_board(computer_board)


play()
