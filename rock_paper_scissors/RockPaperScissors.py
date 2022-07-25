'''
A game of Rock, Paper, Scissors
'''

import random
from time import sleep

def computer_play():
    '''
    A function that randomly generates the computers turn. It will return either
    rock, paper or scissors.
    '''
    computersTurn = random.randint(1,3)
    if computersTurn == 1:
        return 'rock'
    if computersTurn ==2:
        return 'paper'
    if computersTurn == 3:
        return 'scissors'

computer_play()

def players_turn():
    '''
    A function that asks the user if they want to play rock, paper or scissors.
    If the user inputs an invalid response they will keep receiving input prompts
    until a valid response is given.
    '''
    while True:
        players_choice = input('Do you want to play Rock, Paper or Scissors?').lower()
        if players_choice == 'rock' or players_choice == 'scissors' or players_choice\
        == 'paper':
            return players_choice
        else:
            print('Please choose rock, paper or scissors.')

players_turn()

def play_round(player_selection, computuer_selection):
    '''
    This functions plays one round of rock paper scissors between a user and
    the computer. It should be called with the players_turn function being passed
    param one and computer_play as param 2.
    
    :param player_selection: func - the players_turn function shold be passed.
    :param computer_play: func - the computer_play function should be passed.
    :result: str - it will state the winner of the round.
    
    If invalid params are passed an exception message will be shown to the user.
    '''
    if player_selection == 'rock' and computuer_selection == 'scissors':
        return 'You win, rock beats scissors.'
    if player_selection == 'rock' and computuer_selection == 'paper':
        return 'You lose, paper beats rock.'
    if player_selection == 'rock' and computuer_selection == 'rock':
        return 'It\'s a draw, you both picked rock.'
    if player_selection == 'paper' and computuer_selection == 'scissors':
        return 'You lose, scissors beats paper.'
    if player_selection == 'paper' and computuer_selection == 'rock':
        return 'You win, paper beats rock.'
    if player_selection == 'paper' and computuer_selection == 'paper':
        return 'It\'s a draw, you both picked paper.'
    if player_selection == 'scissors' and computuer_selection == 'scissors':
        return 'It\'s a draw, you both picked scissors.'
    if player_selection == 'scissors' and computuer_selection == 'paper':
        return 'You win, scissors beat paper.'
    if player_selection == 'scissors' and computuer_selection == 'rock':
        return 'You lose, rock beats scissors.'
    else:
        raise Exception('An invalid argument has been passed. Please read the\
            docstring and try again.')

play_round(players_turn(), computer_play())

def play_five_rounds():
    round = 0
    while round < 5:
        print(play_round(players_turn(), computer_play()))
        round += 1
        sleep(0.5)

play_five_rounds()
