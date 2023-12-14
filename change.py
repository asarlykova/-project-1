import random
a=input('User name:')

def create_random_ship():
    return random.randint(1, 7), random.randint(1, 7)


def play_again():
    try_again = input("Wanna play again? <Y>es or <N>o? >: ").lower()
    if try_again == "y":
        play_game()
    else:
        print("Goodbye!")
        return


print(a,", welcome to the Battleship game!"
      "\nYour main objective is to find and destroy all the hidden ships on map!\n")

print("""\nIntroductions:
\nYou have 10 ammo and there are 3 hidden ships on map.
In order to hit them, you have to enter specific numbers for that location. For example:
For the first row and first column, you have to write 1 and 1.
I wish you good fortune in wars to come!\n""")


def play_game():
    game_board = [["0", "1", "2", "3", "4", "5", "6", "7"],
              ["1", "O", "O", "O", "O", "O", "O", "O"],
              ["2", "O", "O", "O", "O", "O", "O", "O"],
              ["3", "O", "O", "O", "O", "O", "O", "O"],
              ["4", "O", "O", "O", "O", "O", "O", "O"],
              ["5", "O", "O", "O", "O", "O", "O", "O"],
              ["6", "O", "O", "O", "O", "O", "O", "O"],
              ["7", "O", "O", "O", "O", "O", "O", "O"]]

    for i in game_board:
        print(*i)

    ship1 = create_random_ship()
    ship2 = create_random_ship()
    ship3 = create_random_ship()
    ship4 = create_random_ship()
    ship5 = create_random_ship()
    ship6 = create_random_ship()
    ship7 = create_random_ship()
    ship8 = create_random_ship()
    ship9 = create_random_ship()
    ship10 = create_random_ship()
    ship11 = create_random_ship()
    ships_left = 11
    ammo = 20

    while ammo:
        try:
            row = int(input("Enter a row number between 1-7 >: "))
            column = int(input("Enter a column number between 1-7 >: "))
        except ValueError:
            print("Only enter number!")
            continue

        if row not in range(1,8) or column not in range(1, 8):
            print("\nThe numbers must be between 1-7!")
            continue

       

        if game_board[row][column] == "-" or game_board[row][column] == "X":
            print("\nYou have already shoot that place!\n")
            continue
        elif (row, column) == ship1 or (row, column) == ship2 or (row, column) == ship3:
            print("\nBoom! You hit! A ship has exploded! You were granted a new ammo!\n")
            game_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print("My my, i didn't know you were a sharpshooter! Congratz, you won!")
                play_again()
        else:
            print("\nYou missed!\n")
            game_board[row][column] = "-"
            ammo -= 1

        for i in game_board:
            print(*i)

        print(f"Ammo left: {ammo} | Ships left: {ships_left}")

    play_again()


if __name__ == "__main__":
    play_game()