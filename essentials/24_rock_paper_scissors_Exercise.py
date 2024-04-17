
# rock beats scissors
# scissors beats paper
# paper beats rock

# One player use input and other player is random

# Your Move :
# Computer move is :
# Result : You win / Computer wins

import sys
import random

rock_ascii_art = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper_ascii_art = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors_ascii_art = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print("-----------------------------------------------------------")
print("Welcome to Rock-Scissors-Paper game with Computer")
print("-----------------------------------------------------------")

your_move = input("Enter your move : ").lower()

if your_move != "rock" and your_move != "scissors" and your_move != "paper":
    print("Invalid entry! Start again !")
    sys.exit();


# print ascii art
if your_move == "rock":
    print(rock_ascii_art)
elif your_move == "scissors":
    print(scissors_ascii_art)
else:
    print(paper_ascii_art)


computer_move_number = random.randint(1,3)
computer_move = "un-calculated"

if computer_move_number == 1:
    computer_move = "rock"
elif computer_move_number == 2:
    computer_move = "scissors"
elif computer_move_number == 3:
    computer_move = "paper"

print(f"Computer's move : {computer_move}")

# print ascii art
if computer_move == "rock":
    print(rock_ascii_art)
elif computer_move == "scissors":
    print(scissors_ascii_art)
else:
    print(paper_ascii_art)


winner = "un-calculated"

if your_move == computer_move:
   winner = "tie"
elif (your_move == "rock" and computer_move == "scissors") or (your_move == "scissors" and computer_move == "paper") or (your_move == "paper" and computer_move == "rock"):
   winner = "you"
else:
   winner = "computer"


if winner == "you":
    print("Congratulations, You Win!")
elif winner == "computer":
    print("Computer Won! No worries, try again!")
else:
    print("It's a Tie")

