print('What is your name?')
a = input()
from random import randint, choice

board_size = 7

def number_to_letter(number):
    return chr(ord('A') + number)

def print_board(board):
    print("  " + " ".join([number_to_letter(i) for i in range(board_size)]))
    for i, row in enumerate(board):
        print(str(i + 1) + " " + " ".join(row))

def place_ship(board, ship_size):
    while True:
        orientation = choice(['horizontal', 'vertical'])
        if orientation == 'horizontal':
            ship_row = randint(0, board_size - 1)
            ship_col = randint(0, board_size - ship_size)
            if all(board[ship_row][col] == 'O' for col in range(ship_col, ship_col + ship_size)):
                for col in range(ship_col, ship_col + ship_size):
                    board[ship_row][col] = 'S'
                break
        else:
            ship_row = randint(0, board_size - ship_size)
            ship_col = randint(0, board_size - 1)
            if all(board[row][ship_col] == 'O' for row in range(ship_row, ship_row + ship_size)):
                for row in range(ship_row, ship_row + ship_size):
                    board[row][ship_col] = 'S'
                break

board = []

for _ in range(board_size):
    board.append(['O'] * board_size)

print(a, ", let's play Battleship!")

place_ship(board, 3)  
place_ship(board, 2)  
place_ship(board, 2) 
place_ship(board, 1)  
place_ship(board, 1)
place_ship(board, 1)
place_ship(board, 1)

print_board(board)
