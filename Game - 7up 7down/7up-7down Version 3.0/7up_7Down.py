#
#  Project: &up-7down Version 3.0
#  Coder: Siddhant Shah
#  Desc: Adding few of features:
#       1. Added odds for each events (7up, 7down, 7)
#       2. Gifting user $100 once game start and allowing them to put money on the their calls.
#       3. Maintaining their money vallet and making sure they cannot bet more then they have.
#       4. Quiting game once user has lost all money.
#       5. User can quit the game whenever he wants but doing so all his money will be gone as we are not saving anything in any kind of database

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
            _losses (int): number of games user has lost
            _no_result (int): number of games with no results
            _balance (float): money payer has left
            _game_detail ([()]): list of tuple where tuple will look like ('result', choice, odds, stake, amount, balance)

    """
    def __init__(self, name, balance):
        self._name = name
        self._wins = 0
        self._losses = 0
        self._no_result = 0
        self._balance = balance
        self._game_detail = []


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


def stake(player):
    """functions that ask user to stake the money on his choice.
        Args:
            player (Player): object of class Player
    """

    while True:
        user_stake = input("Please enter the amount you want to stake for your stock: ")     # asking for user input
        if user_stake.isnumeric():     # making sure user has provided an int else we re-run the loop
            if 0 < float(user_stake) <= player._balance:   # making sure user has provided a desired value else we re-run the loop
                return float(user_stake)     # returning user input
            else:   
                print("You can't stake more then you have. Your max contribution can be {}.".format(player._balance))
        else:
            print("This is not a valid option. Please try again later.")


def game_7Up7Down(player):
    """function that actually hold code for playing 7up 7down. Instantiatles 2 dice, ask user to select one of 
        possible 3 outcomes and then decides if user has won ot lost.
        Args: 
            player (Player): object of class Player
    """
    
    print()
    
    while True:
        if player._balance > 0:
            dice_dict = dice_total()    # calling function that instaiate 2 object of classs dice and returns a dictionary
            dice_sum = dice_dict['sum']     # fetching sum of two dices stored as a vlue in a dictionary against key 'sum'
            money_stake = stake(player)
            game_odd = 0
            user_choice = ""

            prompt_int = f"Press 1 if you think sum of two dice will be more then 7 (return = 2x, you get {money_stake*2})\n"\
                        f"Press 2 if you think sum of two dice will be less then 7 (return = 2x, you get {money_stake*2})\n"\
                        f"Press 3 if you think sum of two dice will be equal to 7 (return = 3x, you get {money_stake*3})\n"\
                        f"Press 4 to quit this game: "

            guessed_number = user_input_int(prompt_int, 4)  # fetching user's one of possible 3 choice.

            if guessed_number == 1:
                user_choice = "7 Up"
            elif guessed_number == 2:
                user_choice = "7 Down"
            elif guessed_number == 3:
                user_choice = "7"
            else:
                user_choice = ""

            if guessed_number == 4:
                print("Thanks for playing 7 Ups 7 Down. looking forward to see you again")
                break
            if guessed_number == 1 and dice_sum > 7:   # if user selects more then 7 and sum of 2 dice is also more the 7
                game_odd = 2
                result = "WON"
            elif guessed_number == 2 and dice_sum < 7:  # if user selects less then 7 and sum of 2 dice is also less the 7
                game_odd = 2
                result = "WON"
            elif guessed_number == 3 and dice_sum == 7:    # if user selects sum of 2 dice is equal to 7 and result is also 7
                game_odd = 3
                result = "WON"
            else:   # for everyother condition
                game_odd = -1
                result = "LOST"
            
            money_return = money_stake * game_odd
            print()
            
            trans_dict = game_result(player, result, dice_dict, money_return)
            print()
            print(f"You choose {user_choice} and sum of 2 dice was {dice_sum}.\nYou invested {money_stake} at {game_odd}x odd. So return = {money_return} ")


            trans_dict['odd'] = game_odd
            trans_dict['choice'] = user_choice
            score_display(player, dice_dict)
        else:
            print("Hey Buddy.. Your balance is 0. We dont play we beggars.. Bubye....")
            break


def game_result(player, game_result, dict_dice, money_return):
    """
        Args:
            player (Player): Holds object of class player
            game_result (str): holds 'WON' if player has won or 'LOST' if player has lost
            dict_dice (dictionary): dictionary have value of dice1 and dice2 and their sum.
            money_return (float): net value of monetary outcome of the game.
    """

    # calling fucntion score_update() to update player's attributes depending of result og the game.
    if game_result == 'WON':
        print("You WON.")
        player._wins += 1
        player._balance += money_return
        return {'result':'WON', "return":money_return, "dice_sum": dict_dice['sum'], "balance": player._balance}
        
    elif game_result == 'LOST':
        print("You LOST.")
        print(f"Dice1: {dict_dice['dice1']}, Dice2: {dict_dice['dice2']}.; Total = {dict_dice['sum']}") 
        player._losses += 1
        player._balance += money_return
        return {'result':'LOST', "return":money_return, "dice_sum": dict_dice['sum'], "balance": player._balance}

def choice_of_game(player):
    """function that ask user to chooce one of many games and call the game function depending on user's input.
        Args:
            player (Player): object of class Player who is playing the game.
    """
    game_choice_prompt = "Press 1 if you want to play 7 Up and 7 Down\n"\
                        "Press 2 if you want to play Even or Odd\n"\
                        "Press 3 if you want to play 7 Up and 7 Down\n"
    game_choice_maxChoice = 3

    game_selected = str(user_input_int(game_choice_prompt, game_choice_maxChoice))
    
    if game_selected == '1':
        game_7Up7Down(player)
    else:
        print("Opps.. We are still working on this game. Please try again.")

def score_display(player, dict_dice):
    """function to display the result.
        Args:
            player (Player): object of class Player whose attributes are to be updated
            dict_dice (dictionary): dictionary have value of dice1 and dice2 and their sum.
    """


    
    print()
    print(f"Score Update: Player: {player._name}, Wins: {player._wins}, Losses: {player._losses}, Balance = {player._balance}")
    print()


print()
print("WELCOME TO GUESSING GAME")
print("========================= let's see how good you really are....")
print()
print("The game is designed and coded by SIDDHANT SHAH.")
print()
print("**** 7 UP 7 DOWN ****")
print("So you think you can win? I am gonna rob you like anything... HAHAHA...\n"\
    "Let's Begin")

print()

name = input("Please enter your name: ")
player = Player(name, 100.0)   # instantiating Player object with name taken from user.

print()

# running game till user asks to quit
while True:
    if(player._balance > 0):
        user_input = input("Press 1 if your are ready to loose or anyother key to quit: ")
        if user_input == '1':
            print()
            game_7Up7Down(player)
            # choice_of_game(player)

        else:
            print("You're such a looser.. Next time have some guts before coming back...")
            break
    else:
        break

print()




