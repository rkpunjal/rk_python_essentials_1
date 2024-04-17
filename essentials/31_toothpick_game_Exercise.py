
import os

input_continue = "yes"

while input_continue.lower() == "yes":

    player1 = input(f"Enter Player 1 name : ")
    player2 = input(f"Enter Player 2 name : ")

    str_player_count = ""
    player_count = 0
    current_player = player1

    current_sticks = 13

    while current_sticks >= 0:

        print("| " * current_sticks)
        print(f"There are {current_sticks} sticks left")

        # input for current
        while not str_player_count.isdigit():
            str_player_count = input(f"How many sticks do you choose '{current_player}'? 1,2 or 3 : ")
            if str_player_count.isdigit():
                player_count = int(str_player_count)
                if player_count >=1 and player_count<=3:
                    break
                else:
                    str_player_count = ""
                    player1_count = 0

        current_sticks -= player_count

        # check win status
        if current_sticks <= 0:
            print(f"You win '{current_player}' !")
            break

        str_player_count = ""
        player_count = 0

        # alternate player
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

    print(" ---- Game Over ---- ")

    current_sticks = 13
    str_player_count = ""
    player_count = 0


    # input for quit
    input_continue = input("Play again? ('yes' to continue) : ").lower()

    if input_continue == "yes":
        os.system('cls')


print("******* EXIT **********")
