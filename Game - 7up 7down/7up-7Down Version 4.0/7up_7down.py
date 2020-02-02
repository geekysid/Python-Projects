#
#  Project: &up-7down Version 2.0
#  Coder: Siddhant Shah
#  Desc: Addinf couple of features:
#         1. Keep playingt he game untill user wants to quit.
#         2. Mantaining and displaying scores after evrey match.
#

from random import randint
import os
import json
import getpass
import hashlib


class Dice:
    """Class to hold details of dice. 
        Attributes:
            _value (int): Indicates one of teh 6 faces of dice. can have value between 1-6
    """
    def __init__(self):
        self._value = int(randint(1, 6))
    
    # def dice_with_6_side():
    #     self._value = int(randint(1, 6))

    # def dice_with_12_side():
    #     self._value = int(randint(1, 12))


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
    def __init__(self, name, balance, wins, losses, nr, trans, password):
        self._name = name
        self._wins = wins
        self._losses = losses
        self._no_result = nr
        self._balance = balance
        self._game_detail = trans
        self.__password = password
    

    def update_game_detail(self, trans):
        self._game_detail.append(trans)
        self.update_data_file()


    def update_data_file(self):
        data = {
            "username": self._name,
            "password": self.__password,
            "balance": self._balance, 
            "trans": self._game_detail, 
            "wins": self._wins, 
            "losses": self._losses, 
            "nr": self._no_result
        }
        
        file_name = get_dir_path() + '/users/' + self._name + ".json"
        with open(file_name, 'w') as file:
            json.dump(data, file)


    def show_game_detail(self):
        print(f"\nPlayer Details\nName: {self._name}\nGames Played: {self._wins+self._losses+self._no_result}\nWins: {self._wins}\nLosses: {self._losses}\nMoney: ${self._balance}")
        print()
        print("Choice\tOdds\tStaked\tResult\tReturn\tBalance")
        print('='*50)
        for trans in self._game_detail:
            if trans[3] == 'WON':
                return_val = trans[1]*trans[2]
            elif trans[3] == 'LOST':
                return_val = trans[2]*(-1)
            print(f"{trans[0]}\t{trans[1]}x\t{trans[2]}\t{trans[3]}\t{return_val}\t{trans[4]}")


    def __str__(self):
        self.show_game_detail()
        return ""


def create_new_user():
    file_dir = get_dir_path() + '/users/'

    while True:
        username = input('Please enter username: ')

        if os.path.exists(file_dir + username + '.json'):
            print("Username already take by someone. Please choose another one.\n")
            continue
        else:
            break

    while True:
        password = getpass.getpass('Please enter Password: ')
        conf_pass = getpass.getpass('Please confirm your Password: ')

        if not password == conf_pass:
            print('Password didnot matched. Please try again.\n')
            continue
        else:
            password = hashlib.sha256(str(password).encode()).hexdigest()
            random_hash = hashlib.sha256(str(randint(1,100)).encode()).hexdigest()
            password = random_hash[:8] + password + random_hash[-8:]
            break

    data = {
        'username': username,
        'password': password,
        'balance': 100.0,
        'trans': [],
        'wins': 0,
        'losses': 0,
        'nr': 0
    }
    
    file_path = file_dir + username + '.json'

    try:
        with open(file_path, 'w') as new_file:
            new_file.write(json.dumps(data))
            create_flag = True

        if create_flag:
            print("\nYour accout has been created. We have also credited $100.00 in your account as good gesture. Let's see if you can keep it or loose to us")
            player = user_login()
        
        else:
            player = None
    
        return player
        
    except:
        print("ERROR")
    
    if create_flag:
        print("\nYour accout has been created. We have also credited $100.00 in your account as good gesture. Let's see if you can keep it or loose to us")
        player = user_login()
    else:
        player = None
    
    return player
    

def user_login():
    print()
    print("Please enter credentials to log into the game")
    print()
    while True:
        username = input("Username: ")
        
        file_path = get_dir_path() + '/users/' + username + '.json'
        
        if os.path.exists(file_path):
            with open (file_path) as filename:
                data = json.load(filename)
            break
        else:
            print('Username is not correct. Please try again.\n')
            continue

    while True:
        password = getpass.getpass("Password: ")

        if data['password'][8:-8] == hashlib.sha256(str(password).encode()).hexdigest():
            login_flag = True
            break
        else:
            print('Password is not correct. Please try again.\n')
            continue
    
    if login_flag:
        player = initialise_player(data)
        return player


def initialise_player(player_dict):
    name = player_dict['username']
    wins = player_dict['wins']
    losses = player_dict['losses']
    nr = player_dict['nr']
    balance = player_dict['balance']
    trans = player_dict['trans']
    password = player_dict['password']
    return Player(name=name, wins=wins, losses=losses, nr=nr, balance=balance, trans=trans, password=password)


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
    """functions that accepts and validated for int type user input and returns it back.
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
        user_stake = input("Please enter the amount you want to stake for your stock: $")   # asking for user input
        print()
        
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
                        f"\nYou Choice: "

            guessed_number = user_input_int(prompt_int, 3)  # fetching user's one of possible 3 choice.

            if guessed_number == 1:
                user_choice = "7 Up"
                game_odd = 2
            elif guessed_number == 2:
                user_choice = "7 Down"
                game_odd = 2
            elif guessed_number == 3:
                user_choice = "7"
                game_odd = 3
            else:
                user_choice = ""
                game_odd = 0

            if guessed_number == 1 and dice_sum > 7:   # if user selects more then 7 and sum of 2 dice is also more the 7
                result = "WON"
            elif guessed_number == 2 and dice_sum < 7:  # if user selects less then 7 and sum of 2 dice is also less the 7
                result = "WON"
            elif guessed_number == 3 and dice_sum == 7:    # if user selects sum of 2 dice is equal to 7 and result is also 7
                result = "WON"
            else:   # for everyother condition
                result = "LOST"
            
            if result == 'WON':
                money_return = money_stake * game_odd
            elif result == 'LOST':
                money_return = money_stake * (-1)
            else:
                money_return = money_stake

            print()
            
            trans_dict = game_result(player, result, dice_dict, money_return)
            print()
            print(f"You choose {user_choice} and sum of 2 dice was {dice_sum}.\n"\
                f"You invested ${money_stake} at {game_odd}x odd. You {result.title()} = ${money_return} ")


            trans_dict['odd'] = game_odd
            trans_dict['choice'] = user_choice
            score_display(player, dice_dict)
            trans = [user_choice, game_odd, money_stake, result, player._balance]
            player.update_game_detail(trans)

            print()
            next_game_option = user_input_int("Press 1 to continue playing or 2 to quit: ", 2)
            if next_game_option == 1:
                continue
            else:
                print("\nThankyou for loosing to us. We will look forward to steal more money from you.\nBelow are your details")

                print(player)
                return True

        else:
            print("Hey Buddy.. Your balance is 0. We dont play we beggars.. Bubye....")

            player.show_game_detail()
            print()
            return Trus


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
    print(f"Score Update: Player: {player._name}, Wins: {player._wins}, Losses: {player._losses}, Balance = ${player._balance}")
    print()


def get_dir_path():
    return os.path.dirname(os.path.realpath(__file__))


print()
print("""WELCOME TO GUESSING GAME2
========================= let's see how good you really are....
The game is designed and coded by SIDDHANT SHAH.

**** 7 UP 7 DOWN ****
So you think you can win? I am gonna rob you like anything... HAHAHA...

Let's Begin""")

print()

userLogin = user_input_int("Press 1 to login or 2 to create a new account: ", 2)

if userLogin == 1:
    player = user_login()
else:
    player = create_new_user()

if player:
    print(player)
    print()
    # running game till user asks to quit
    while True:
        if(player._balance > 0):
            user_input = input("Press 1 if your are ready to loose or anyother key to quit: ")
            if user_input == '1':
                quit_flag = game_7Up7Down(player)
                # choice_of_game(player)
                if quit_flag:
                    break
            else:
                print("You're such a looser.. Next time have some guts before coming back...")
                break
        else:
            print("You account balance is 0.")
            print("We are working on our loan system and it should be up in coming days.")
            print("Till then, you can ceate new account and start lossing money again.")
            break
else:
    print('There was some problem. Please try after some time.')

print()





