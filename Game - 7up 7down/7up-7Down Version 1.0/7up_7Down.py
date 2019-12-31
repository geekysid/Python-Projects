#
#  Project: &up-7down Version 1.0
#  Coder: Siddhant Shah
#  Desc: BASIC 7UP AND 7DOWN
#

from random import randint

print()
print("WELCOME TO GUESSING GAME")
print("========================= let's see how good you really are....")
print()
print("The game is designed and coded by SIDDHANT SHAH.")

print()

name = input("Please enter your name: ")

print()

print()
print("**** 7 UP 7 DOWN ****")
print("So you think you can win? I am gonna rob you like anything... HAHAHA...\n"\
    "Let's Begin")
print()

dice1 = int(randint(1, 6))  # using randint functiom to randmly generate dice value
dice2 = int(randint(1, 6))  # using randint functiom to randmly generate dice value

prompt_int = "Press 1 if you think sum of two dice will be more then 7\n"\
            "Press 2 if you think sum of two dice will be less then 7\n"\
            "Press 3 if you think sum of two dice will be equal to 7 \n"\
            "Press 4 to quit this game: "

guessed_number = input(prompt_int)  # asking user to select one of possible 3 outcomes

# if user selects more then 7 and sum of 2 dice is also more the 7
if guessed_number == '1' and dice1+dice2 > 7:
    print("You WON")
    
# if user selects less then 7 and sum of 2 dice is also less the 7
elif guessed_number == '2' and dice1+dice2 < 7:
    print("You WON")

# if user selects sum of 2 dice is equal to 7 and result is also 7
elif guessed_number == '3' and dice1+dice2 == 7:
    print("You WON")

# for everyother condition
else:
    print("You LOST")

print(f"Dice1: {dice1}, Dice2: {dice2}; Total = {dice1+dice2}")    




