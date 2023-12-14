print('What is your name?')
a = input()
from random import randint

board_size = 7

# Helper function to convert number to corresponding letter for columns
def number_to_letter(number):
    return chr(ord('A') + number)

board = []

for _ in range(board_size):
    board.append(["O"] * board_size)

def print_board(board):
    print("  " + " ".join([number_to_letter(i) for i in range(board_size)]))
    for i, row in enumerate(board):
        print(str(i + 1) + " " + " ".join(row))

print(a, ", let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(12):
    print("\nTurn", turn)
    guess_row = int(input("Guess Row (1-" + str(board_size) + "):")) - 1
    guess_col = int(input("Guess Col (A-" + number_to_letter(board_size - 1) + "):", base=26)) % board_size

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "X"
        break
    else:
        if (guess_row < 0 or guess_row >= board_size) or (guess_col < 0 or guess_col >= board_size):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "-"

    if turn == 11:
        print("Game Over")
        print_board(board)
