import random

# Constants for Game Parameters
NUM_ROWS = 7
NUM_COLUMNS = 7
NUM_SHIPS = 11
STARTING_AMMO = 30

def create_random_ship():
    return random.randint(1, NUM_ROWS), random.randint(1, NUM_COLUMNS)

def play_again():
    try_again = input("Wanna play again? <Y>es or <N>o? >: ").lower()
    if try_again == "y":
        play_game()
    else:
        print("Goodbye!")
        return

def print_board(board):
    for row in board:
        print(*row)

def is_valid_coordinate(row, col):
    return 1 <= row <= NUM_ROWS and 1 <= col <= NUM_COLUMNS

def play_game():
    game_board = [["0", "1", "2", "3", "4", "5", "6", "7"],
                  ["1", "O", "O", "O", "O", "O", "O", "O"],
                  ["2", "O", "O", "O", "O", "O", "O", "O"],
                  ["3", "O", "O", "O", "O", "O", "O", "O"],
                  ["4", "O", "O", "O", "O", "O", "O", "O"],
                  ["5", "O", "O", "O", "O", "O", "O", "O"],
                  ["6", "O", "O", "O", "O", "O", "O", "O"],
                  ["7", "O", "O", "O", "O", "O", "O", "O"]]

    print(a, ", welcome to the Battleship game!"
          "\nYour main objective is to find and destroy all the hidden ships on the map!\n")

    print("""\nIntroductions:
    \nYou have 30 ammo and there are 11 hidden ships on the map.
    In order to hit them, you have to enter specific numbers for that location. For example:
    For the first row and first column, you have to write 1 and 1.
    I wish you good fortune in wars to come!\n""")

    ships = [create_random_ship() for _ in range(NUM_SHIPS)]
    ships_left = NUM_SHIPS
    ammo = STARTING_AMMO

    while ammo:
        try:
            row = int(input(f"Enter a row number between 1-{NUM_ROWS} >: "))
            column = int(input(f"Enter a column number between 1-{NUM_COLUMNS} >: "))
        except ValueError:
            print("Only enter numbers!")
            continue

        if not is_valid_coordinate(row, column):
            print(f"\nThe numbers must be between 1-{NUM_ROWS} and 1-{NUM_COLUMNS}!")
            continue

        if game_board[row][column] == "-" or game_board[row][column] == "X":
            print("\nYou have already shot that place!\n")
            continue
        elif (row, column) in ships:
            print("\nBoom! You hit! A ship has exploded! You were granted new ammo!\n")
            game_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print("My my, I didn't know you were a sharpshooter! Congrats, you won!")
                play_again()
        else:
            print("\nYou missed!\n")
            game_board[row][column] = "-"
            ammo -= 1

        print_board(game_board)
        print(f"Ammo left: {ammo} | Ships left: {ships_left}")

    play_again()

if __name__ == "__main__":
    a = input('User name:')
    play_game()
