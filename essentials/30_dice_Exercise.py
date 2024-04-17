
# Dice exercise
# --------------------

import random

str_dice_count = ""
dice_count = 0
str_side_count = ""
side_count = 0

input_quit = ""

while not str_dice_count.isdigit():
    str_dice_count = input("How many dice are we rolling (between 1 to 9) ? ")
    if str_dice_count.isdigit():
        dice_count = int(str_dice_count)
        if dice_count > 0 and dice_count <= 9:
            break
        else:
            str_dice_count = ""
            dice_count = 0
    print("Enter a valid number between 1 to 9")

# input for number of sides in each dice
while not str_side_count.isdigit():
    str_side_count = input("How many sides in each dice (between 1 to 20) ? ")
    if str_side_count.isdigit():
        side_count = int(str_side_count)
        if side_count > 0 and side_count <= 20:
            break
        else:
            str_side_count = ""
            side_count = 0
    print("Enter a valid number between 1 to 20")

while input_quit.lower() != "q":
    # input for number of dice

    # generate output
    str_output = "|"
    for n in range (dice_count):
        str_output = str_output + str(random.randint(1, side_count))
        str_output = str_output + "|"
    print(str_output)

    # input for quit
    input_quit = input("Roll again? ('q' to quit) : ")


print("------ End of Program -----")

