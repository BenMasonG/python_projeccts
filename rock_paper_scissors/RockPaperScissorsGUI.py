import random
import tkinter as tk
from time import sleep

score_count = []

def computer_play():
    '''
    A function that randomly generates the computers turn. It will return either
    rock, paper or scissors.
    '''
    picks = ['rock', 'paper', 'scissors']
    return random.choice(picks)

def players_turn():
    players_choice = frm_entry.get().lower()
    if players_choice == 'rock' or players_choice == 'scissors' or players_choice\
        == 'paper':
            lbl_player_choice['text'] = players_choice
            return players_choice
    else:
        lbl_player_choice['text'] = 'Please choose rock, paper or scissors.'


window = tk.Tk()
window.columnconfigure(0, minsize=300)
window.rowconfigure([0, 1, 2, 3, 4], minsize=50)

btn_start = tk.Button(text='Start Game') #, command=play_five_rounds)
frm_entry = tk.Entry()
btn_enter_choice = tk.Button(text='input choice', command=players_turn)
lbl_player_choice = tk.Label()
lbl_result = tk.Label()

btn_start.grid(row=0, column=0, sticky='nsew')
frm_entry.grid(row=1, column=0)
btn_enter_choice.grid(row=2, column=0)
lbl_player_choice.grid(row=3, column=0)
lbl_result.grid(row=4, column=0)

window.mainloop()
