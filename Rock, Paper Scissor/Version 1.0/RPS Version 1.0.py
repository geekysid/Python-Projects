# author: Siddhant Shah
# Desc: A very basic version of RPS. This is a very basic version of RPS with only functionality being used are use of
# variables, if-elif-else statements, taking user input, and printing result

import random

print("Welcome to the Rock, Paper, Scissors Game")
user_input = input("Please choose one of the 3 options, 'Rock', 'Paper' or 'Scissor': ")    # taking user input

print()

game_tuple = ('Rock', 'Paper', 'Scissor')       # tuple which holds all possible option of game
random_choice = game_tuple[random.randint(0, 2)]    # using randint function of class random to choose one of 3 items in tupple
print(f"You choose: {user_input}")
print(f"Computer choose: {random_choice}")

print()

# checking different conditions
if user_input == 'Rock':
    if random_choice == 'Rock':         # if both user and computer have selected 'Rock'
        print("IT A DRAW!!!")
    elif random_choice == 'Paper':      # if user have selected 'Rock' but computer has selected 'Paper'
        print("LOL!! YOU LOST")
    elif random_choice == 'Scissor':    # if user have selected 'Rock' but computer has selected 'Scissor'
        print("YAY!! YOU WIN")
elif user_input == 'Paper':
    if random_choice == 'Rock':         # if user have selected 'Paper' but computer has selected 'Rock'
        print("LOL!! YOU LOST")
    elif random_choice == 'Paper':      # if both user and computer have selected 'Paper'
        print("IT A DRAW!!!")
    elif random_choice == 'Scissor':    # if user have selected 'Paper' but computer has selected 'Scissor'
        print("YAY!! YOU WIN")
elif user_input == 'Scissor':
    if random_choice == 'Rock':         # if user have selected 'Scissor' but computer has selected 'Rock'
        print("YAY!! YOU WIN")
    elif random_choice == 'Paper':      # if user have selected 'Scissor' but computer has selected 'Paper'
        print("LOL!! YOU LOST")
    elif random_choice == 'Scissor':    # if both user and computer have selected 'Scissor'
        print("IT A DRAW!!!")
else:
    print("Please enter valid input")
