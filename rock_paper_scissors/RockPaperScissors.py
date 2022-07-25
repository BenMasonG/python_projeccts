'''
A game of Rock, Paper, Scissors
'''

import random

def computerPlay():
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

computerPlay()

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
