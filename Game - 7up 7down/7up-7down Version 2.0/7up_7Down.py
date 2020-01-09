#
#  Project: &up-7down Version 2.0
#  Coder: Siddhant Shah
#  Desc: Addinf couple of features:
#         1. Keep playingt he game untill user wants to quit.
#         2. Mantaining and displaying scores after evrey match.
#

from random import randint

class Dice:
    """Class to hold details of dice. 
        Attributes:
            _value (int): Indicates one of teh 6 faces of dice. can have value between 1-6
    """
    def __init__(self):
        self._value = int(randint(1, 6))


class Player:
    """Class to hold details of Player. 
        Attributes:
            _name (str): name of the player
            _wins (int): number of games user has won
            _wins (int): number of games user has lost
            _wins (int): number of games with no results
    """
    def __init__(self, name):
        self._name = name
        self._wins = 0
        self._losses = 0
        self._no_result = 0


def dice_total():
    """functions that creates coupleof instances of dice and returns a dictionary."""
    dice1 = Dice()
    dice2 = Dice()

    dice_value = {'dice1': dice1._value,
                    'dice2': dice2._value, 
                    'sum': dice1._value + dice2._value
                }
    return dice_value


def user_input_int(prompt, maxValue):
    """functions that creates coupleof instances of dice and returns a dictionary.
        Args:
            prompt (str): holds text that will be displayed when user is asked for input
            maxValue (int): indicates max value in int that a user is allowed to give 
    """

    while True:
        user_choice = input(prompt)     # asking for user input
        if user_choice.isnumeric():     # making sure user has provided an int else we re-run the loop
            if 1 <= int(user_choice) <= maxValue:   # making sure user has provided a desired value else we re-run the loop
                return int(user_choice)     # returning user input
            else:   
                print("This is not a valid option. Please try again later.")
        else:
            print("This is not a valid option. Please try again later.")


def game_7Up7Down(player):
    """function that actually hold code for playing 7up 7down. Instantiatles 2 dice, ask user to select one of 
        possible 3 outcomes and then decides if user has won ot lost.
        Args: 
            player (Player): object of class Player
    """
    print()
    print("**** 7 UP 7 DOWN ****")
    print("So you think you can win? I am gonna rob you like anything... HAHAHA...\n"\
        "Let's Begin")
    print()
    
    while True:

        dice_dict = dice_total()    # calling function that instaiate 2 object of classs dice and returns a dictionary

        dice_sum = dice_dict['sum']     # fetching sum of two dices stored as a vlue in a dictionary against key 'sum'

        prompt_int = "Press 1 if you think sum of two dice will be more then 7\n"\
                    "Press 2 if you think sum of two dice will be less then 7\n"\
                    "Press 3 if you think sum of two dice will be equal to 7 \n"\
                    "Press 4 to quit this game: "

        guessed_number = user_input_int(prompt_int, 4)  # fetching user's one of possible 3 choice.
        
        if guessed_number == 4:
            print("Thanks for playing 7 Ups 7 Down. looking forward to see you again")
            break
        
        if guessed_number == '1' and dice1+dice2 > 7:   # if user selects more then 7 and sum of 2 dice is also more the 7
            print("You WON")
            result = "WON"
        elif guessed_number == '2' and dice1+dice2 < 7:  # if user selects less then 7 and sum of 2 dice is also less the 7
            print("You WON")
            result = "WON"
        elif guessed_number == '3' and dice1+dice2 == 7:    # if user selects sum of 2 dice is equal to 7 and result is also 7
            print("You WON")
            result = "WON"
        else:                                           # for everyother condition
            print("You LOST")
            result = "LOST"
        
        # calling functionto displayt outcome.
        game_result_display(player, result, dice_dict)


def game_result_display(player, game_result, dict_dice):
    """
        Args:
            player (Player): Holds object of class player
            game_result (str): holds 'WON' if player has won or 'LOST' if player has lost
            dict_dice (dictionary): dictionary have value of dice1 and dice2 and their sum.
    """

    # calling fucntion score_update() to update player's attributes depending of result og the game.
    if game_result == 'WON':
        print("You WON.")
        score_update(player, True)
    elif game_result == 'LOST':
        print("You LOST.")
        score_update(player, False)

    # fetching values from dictionary
    dice1 = dict_dice['dice1']
    dice2 = dict_dice['dice2']
    dice_sum = dict_dice['sum']

    print(f"Dice1: {dice1}, Dice2: {dice2}.; Total = {dice_sum}")    
    print()
    print(f"Score Update: Player: {player._name}, Wins: {player._wins}, Losses: {player._losses}")
    print()
    

def choice_of_game(player):
    """function that ask user to chooce one of many games and call the game function depending on user's input.
        Args:
            player (Player): object of class Player who is playing the game.
    """
    game_choice_prompt = "Press 1 if you want to play 7 Up and 7 Down\n"\
                        "Press 2 if you want to play Even or Odd\n"\
                        "Press 3 if you want to play 7 Up and 7 Down Version 2.0\n"
    game_choice_maxChoice = 3

    game_selected = str(user_input_int(game_choice_prompt, game_choice_maxChoice))
    
    if game_selected == '1':
        game_7Up7Down(player)
    else:
        print("Opps.. We are still working on this game. Please try again.")


def score_update(player, result):
    """function to update the player attributes.
        Args:
            player (Player): object of class Player whose attributes are to be updated
            result (boolean): Truw if player won or False if player lost
    """
    if result:
        player._wins += 1   # increasing player's _wins attribute by 1 if player won
    else:
        player._losses += 1  # increasing player's _losses attribute by 1 if player lost


print()
print("WELCOME TO GUESSING GAME")
print("========================= let's see how good you really are....")
print()
print("The game is designed and coded by SIDDHANT SHAH.")

print()

name = input("Please enter your name: ")
player = Player(name)   # instantiating Player object with name taken from user.

print()

# running game till user asks to quit
while True:
    user_input = input("Press 1 if your are ready to loose or anyother key to quit: ")
    if user_input == '1':
        print()
        choice_of_game(player)

    else:
        print("You're such a looser.. Next time have some guts before coming back...")
        break


print()




