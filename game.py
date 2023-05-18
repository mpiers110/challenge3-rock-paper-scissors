import tkinter as tk
from tkinter import *
import customtkinter
from random import randint

#using lowercase options
choices = ['rock','paper','scissors']
ch = 'y'


def opt_rock():
    global pc
    pc = "rock"
    make_move(pc)
def opt_paper():
    global pc
    pc = "paper"
    make_move(pc)
def opt_scissors():
    global pc
    pc = "scissors"
    make_move(pc)



#function with parameter to get result on every choice
def get_result(plr_ch):
    comp_choice = choices[randint(0,2)]
    comp_choice_message = "\nComputer chose:"+str(comp_choice)+"\n"
    message_label.configure(text = comp_choice_message)

    #basic game rules
    if plr_ch == comp_choice:
        result = ["tie", '{} is same as {}! No score change!'.format(plr_ch.upper(), comp_choice.upper())]       
    elif comp_choice == 'scissors' and plr_ch == 'rock':
        result = ['win', "ROCK crushes SCISSORS! You win!"]
        
    elif comp_choice == 'paper' and plr_ch == 'scissors': 
        result = ['win', "SCISSORS cut PAPER! You win!"]
        
    elif comp_choice == 'rock' and plr_ch == 'paper': 
        result = ['win', "PAPER covers ROCK! You win!"]
        
    #if it does not match any of the win criteria then add 1 to loss and 
    #display loss message 
    else: 
        result = ['lose', "You lose! Computer wins! Score -1"]
    return result

#function to update the scores
def update_score(result):
    global wins, loss, tie
    if result == 'win':
        wins += 1
    elif result == 'lose':
        loss += 1
    else:
        tie += 1


def make_move(pc):
    res = get_result(pc)
    round_result.append(res[0])
    update_score(res[0])
    tot_score = wins - loss
    message_label.configure(text = res[1])
    score_label.configure(text="Score : "+str(tot_score))

#function to run the game till user defined rounds
def game():
    tot_score = 0
    global round_result
    message_label.configure(text = "Choose one option from below")
    rock_button.place(x=50, y=85)
    paper_button.place(x=100, y=85)
    scissors_button.place(x=155, y=85)
    start_button.grid(row=2, column=0, columnspan=2, padx=25, pady= 100)
    start_button.configure(text="Reset Game")

    #at the end of all rounds we return total score    
    return tot_score


def start():
    ts = game()
    score_label.configure(text="Score : "+str(ts))


first_message = "\nWelcome to Rock, Paper, Scissors Game.\nRules are simple\nWinning Rules are as follows:\nRock vs Paper -> Paper wins Rock Losses\nRock vs Scissors -> Rock wins Scissors Losses\nPaper vs Scissors -> Scissors wins Paper Losses\n\nFor each win you get 1 point \nIf you lose -1 point\nAnd if its a tie 0 point\n'''"




def start_game():
    global ch, round_result
    message_label.configure(text = "Click Start when you are ready to play")
    score_label.place(x=120, y=50)
    score_label.configure(text="Score : 0")
    start_button.configure(command = start, text="Start")





#Main Window properties
window = Tk()
window.title("Rock, Paper, Scissors Game")
window.geometry("450x330")
window.configure(bg="#262626")
window.resizable(False, False)
#font definition
main_font = customtkinter.CTkFont(family="Helvetica", size=12)

#Creates a frame to hold the widgets
frame = tk.Frame(window, background='#262626')
frame.pack()

#Creates a button to start game
start_button = customtkinter.CTkButton(
    master= frame,
    command= start_game,
    text= "Start Game",
    font= main_font,
    text_color= "#79ae61",
    hover= True,
    hover_color= "white",
    height=40,
    width= 120,
    border_width=2,
    corner_radius=20,
    border_color= "#79ae61", 
    bg_color="#262626",
    fg_color= "#262626")
start_button.grid(row=2, column=0, columnspan=2, padx=25, pady= 40)

#Creates label for repository info
info_label = customtkinter.CTkLabel(
                                master=window,
                                text="https://github.com/mpiers110/challenge3-rock-paper-scissors",
                                text_color= "black",
                                width=120,
                                height=25,
                                fg_color=("white", "gray75"),
                                bg_color="#262626",
                                corner_radius=8)
info_label.place(x=15, y=290)

#Creates labels for first_message
message_label = customtkinter.CTkLabel(
                                master=frame,
                                text=first_message,
                                text_color= "black",
                                width=120,
                                height=25,
                                fg_color=("white", "gray75"),
                                bg_color="#262626",
                                corner_radius=8)
message_label.grid(row=0, column=0, padx=15, pady=10)

rounds_label = customtkinter.CTkLabel(
                                master=frame,
                                text="Rounds",
                                text_color= "black",
                                width=70,
                                height=25,
                                fg_color=("white", "gray75"),
                                bg_color="#262626",
                                corner_radius=8)

score_label = customtkinter.CTkLabel(
                                master=frame,
                                text="Score",
                                text_color= "black",
                                width=90,
                                height=25,
                                fg_color=("white", "gray75"),
                                bg_color="#262626",
                                corner_radius=8)



rock_button = customtkinter.CTkButton(
    master= window,
    command= opt_rock,
    text= "Rock",
    font= main_font,
    text_color= "#79ae61",
    hover= True,
    hover_color= "white",
    height=10,
    width= 20,
    border_width=2,
    corner_radius=20,
    border_color= "#79ae61", 
    bg_color="#262626",
    fg_color= "#262626")

paper_button = customtkinter.CTkButton(
    master= window,
    command= opt_paper,
    text= "Paper",
    font= main_font,
    text_color= "#79ae61",
    hover= True,
    hover_color= "white",
    height=10,
    width= 20,
    border_width=2,
    corner_radius=20,
    border_color= "#79ae61", 
    bg_color="#262626",
    fg_color= "#262626")

scissors_button = customtkinter.CTkButton(
    master= window,
    command= opt_scissors,
    text= "Scissors",
    font= main_font,
    text_color= "#79ae61",
    hover= True,
    hover_color= "white",
    height=10,
    width= 20,
    border_width=2,
    corner_radius=20,
    border_color= "#79ae61", 
    bg_color="#262626",
    fg_color= "#262626")

while(ch == 'y' or ch == 'Y'):
    wins = 0
    loss = 0
    tie = 0
    round_result = []
    window.mainloop()
