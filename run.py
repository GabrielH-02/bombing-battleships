import random

# Horizontal Line Large
HR_L = '-' * 70
# Horizontal Line Small
HR_L_S = '-' * 35
# Board Space (empty)
B_S = "~"
# Board - Player Ship
B_P_S = "@"
# Board - Computer Ship
B_C_S = "0"
# Board - Player hits computer's ship
B_P_H = "*"
# Board - Computer hits player's ship
B_C_H = "X"
# Board - Missed hit
B_M = "O"


def welcome_statement():
    print('\n Welcome to Bombing Blasting Battleships'.upper())
    print(HR_L)
    print(' How to Play:')
    print(HR_L)
    print('   1. Insert your name')
    print('   2. Select a singular number for the size of the grid')
    print('   3. Select and guess the row, and column to bomb')
    print('   4. Try and beat the computer')
    print('   Note: The game has only ten rounds!')
    print('   Note: Consider the size of the grid since there are 4 ships!')
    print('   Note: The grid coordinates begin in the top left corner,(0, 0)')
    print(HR_L)
    print(f' Key: \n')
    print(f'   {B_P_S} = Your Ship')
    print(f'   {B_S} = Space')
    print(f'   {B_P_H} = Hit')
    print(f'   {B_C_H} = Hit By Computer')
    print(f'   {B_M} = Missed\n')
    print(HR_L)


def get_player_name():
    player_name = input("What's your name: \n").capitalize()
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


def player_guess(num_spaces, max_invalid_attempts):
    invalid_attempts = 0

    while invalid_attempts < max_invalid_attempts:
        try:
            guess_row = int(input(f"\nGuess Row (0 - {num_spaces - 1}): \n"))
            guess_col = int(input(f"\nGuess Col (0 - {num_spaces - 1}): \n"))

            if 0 <= guess_row < num_spaces and 0 <= guess_col < num_spaces:
                return guess_row, guess_col
            else:
                print("Please enter valid coordinates.")
                invalid_attempts += 1
        except ValueError:
            print("Invalid input. Please enter numbers.")
            invalid_attempts += 1

    print(HR_L)
    print("\nToo many invalid attempts. Game over!\n".upper())
    print(HR_L)
    exit()


def rand_num(num):
    return random.randint(0, (num - 1))


def place_player_ships(board):
    for _ in range(4):
        ship_row = rand_num(len(board) - 1)
        ship_col = rand_num(len(board) - 1)
        while board[ship_row][ship_col] == B_P_S:
            ship_row = rand_num(len(board) - 1)
            ship_col = rand_num(len(board) - 1)
        board[ship_row][ship_col] = B_P_S


def place_comp_ships(board):
    for _ in range(4):
        ship_row = rand_num(len(board) - 1)
        ship_col = rand_num(len(board) - 1)
        while board[ship_row][ship_col] == B_C_S:
            ship_row = rand_num(len(board) - 1)
            ship_col = rand_num(len(board) - 1)
        board[ship_row][ship_col] = B_C_S


def main():
    # Calls the welcome statement
    welcome_statement()
    # Calls and defines player name input
    player_name = get_player_name()
    # Calls and defines grid size input
    size = get_grid_size()

    # defines size and define grid spaces
    player_board = [[B_S] * size for _ in range(size)]
    computer_board = [[B_S] * size for _ in range(size)]

    # defines the player and computer score
    player_score = 0
    computer_score = 0

    # places the ships for the player
    place_player_ships(player_board)

    # places the ships for the comp
    place_comp_ships(computer_board)

    # prints out player and computer boards
    print(f"\n{player_name}'s Board:\n")
    print_board(player_board)

    print(HR_L)

    print("\nComputer's Board:\n")
    print_board(computer_board)

    # loop of the game

    rounds = 10

    for turn in range(rounds):

        # prints the title of the round
        print("\n Round", turn + 1)
        print(HR_L)

        # prints the players turn
        print(f"\n{player_name}'s Go:")

        # runs the player_guess function
        player_guess_row, player_guess_col = player_guess(size, 3)

        # If the player hits a computer's ship changes 0 to *
        if computer_board[player_guess_row][player_guess_col] == B_C_S:
            print(HR_L_S)
            print("Congratulations! You sunk the computer's battleship!")
            print(HR_L_S)
            player_score += 1
            computer_board[player_guess_row][player_guess_col] = B_P_H
        else:
            # If player renters value they already inputed
            if computer_board[player_guess_row][player_guess_col] == B_M:
                print(HR_L_S)
                print("You already guessed that. Try again.")
                print(HR_L_S)
            else:
                # If player misses it replaces ~ to O
                print(HR_L_S)
                print("You missed!")
                print(HR_L_S)
                computer_board[player_guess_row][player_guess_col] = B_M

        # prints the players board
        print(f"\n{player_name}'s Board:")
        print_board(player_board)

        print("\nComputer Board:")
        print_board(computer_board)

        print("\nComputer's Go:")
        computer_guess_row = rand_num(size)
        computer_guess_col = rand_num(size)

        # If the computer hits the player's ship it changes @ to X
        if player_board[computer_guess_row][computer_guess_col] == B_P_S:
            print(HR_L_S)
            print("Oh no! The computer sunk your battleship!")
            print(HR_L_S)
            computer_score += 1
            player_board[computer_guess_row][computer_guess_col] = B_C_H
        else:
            # If the guess the same inputed value
            if player_board[computer_guess_row][computer_guess_col] == B_M:
                print(HR_L_S)
                print("Computer already guessed that. It's your lucky day.")
                print(HR_L_S)
            else:
                # If computer misses it replaces ~ to O
                print(HR_L_S)
                print("Computer missed!")
                print(HR_L_S)
                player_board[computer_guess_row][computer_guess_col] = B_M

        print(f"\n{player_name}'s Board:")
        print_board(player_board)

    # prints the game of the game
    # displays the amount of points
    print(HR_L)
    print("\nGame Over!\n".upper())
    print(HR_L)
    print(f"\n{player_name} Scored: {player_score} points\n")
    print(f"Computer Scored: {computer_score} points\n")

    # determines who wins the game based on points
    if player_score > computer_score:
        print(HR_L)
        print(f"\nCongratulations, {player_name}! is the winner!\n".upper())
        print(HR_L)
    elif player_score < computer_score:
        print(HR_L)
        print("\nSorry, the computer wins. Better luck next time!\n")
        print(HR_L)
    else:
        print(HR_L)
        print("\nIt's a tie! Both sides played well.\n")
        print(HR_L)


main()
