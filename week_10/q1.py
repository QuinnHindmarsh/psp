import random

def display_details():
    print("""
    Author: Quinn
    Email Id: hinqc001
    This is my own work as defined by the
    University's Academic Misconduct Policy.""")

def get_choice():
    uchoice = 4
    while uchoice > 3 or uchoice < 1:
        uchoice = int(input('enter a number from 1 to 3 (1 = rock, 2 = paper, 3 = scissors)'))
        if uchoice > 3 or uchoice < 1:
            print('please enter a valid number from 1-3')

    return uchoice

play = 1
games = 0
while play == 1:
    games += 1
    choices = ['rock','paper','scissors']

    uchoice = get_choice()
    print('you chose ', choices[uchoice - 1])
    AIchoice = random.randint(1,3)

    print('the computer chose ',choices[AIchoice-1])

    if AIchoice == uchoice:
        print('draw')
    elif AIchoice == 1 and uchoice == 3 or AIchoice == 2 and uchoice == 1 or AIchoice == 3 and uchoice == 2:
        print('computer wins')
    else:
        print('player wins')

    play = int(input('enter 1 to play again, any other number to end'))

print(games,' played')

