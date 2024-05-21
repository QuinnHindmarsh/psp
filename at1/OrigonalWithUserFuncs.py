#
# File:  hinqc001_battle_p1.py
# Author: Quinn Hindmarsh
# Email Id: hinqc001@mymail.unisa.edu.au
# Description: Assignment 1 – text based adventure game Dragon Battleground
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

#assumptions
"""
all assumptions i have made while creating the project are listed here

the task states rolling 3 1s,3s or 5s means zero damage will be dealt. i have assumed if 4 or 5 1s,0s or 5s are rolled it will also be zero damage
similaraly ill also assume rolling 4/5 2s,4s or 6s will triple the damage like 3 of a kind would

i assume in 1 round both the player and the dragon attack e.g. if there are 5 rounds each attacks 5 times
"""

from dice import display_dice #used to display dice
import random #used to roll dice



#player/dragon hp and player_stats are global so they can be used in all functions without them being put in paramaters
global dragon_hp
global player_hp
player_stats = [0,0,0] #keeps track of player stats. 0 = wins, 1 = drawn, 2 = dragons killed
dragon_hp = 100
player_hp = 100




def roll_dice(): #rolls 5 dice and returns a list with the results
    rolls = []#stores each dice roll
    for itteration in range(0,5,1):
        rolls.append(random.randint(1,6))

    return rolls

def count_rolls(rolls): #accepts a list of rolls and determines how many of each number where rolled
    roll_frequency = [0,0,0,0,0,0,0]#all elements but element0 corripsond to the amount of times that number was rolled. eg if roll_frequency[2] == 3 then 3 2s where rolled
    for item in rolls:
        roll_frequency[item] += 1


    #finds the appropraite damage multiplier to use
    damage_multiplier = 1
    if roll_frequency[1] == 3 or roll_frequency[3] == 3 or roll_frequency[5] == 3:
        damage_multiplier = 0
    else:
        max = 0
        for itteration in range(len(roll_frequency)):
            if roll_frequency[itteration] > max:
                max = roll_frequency[itteration]

        if max >= 3:
            damage_multiplier = 3
        elif max == 2:
            damage_multiplier = 2

    return damage_multiplier * sum(rolls)

def player():#manages the player turn
    global dragon_hp
    player_roll = []#player rolls stored in this
    player_roll = roll_dice()#sets the player rolls to 5 random numbers between 1-6
    damage = count_rolls(player_roll)# holds player_roll * damage_multiplier
    print(damage,'damage dealt to the dragon')
    dragon_hp = dragon_hp - damage

    if dragon_hp <= 0:
        print('the dragon has died')
        end = True
    else:
        print('dragon is on ',dragon_hp,'health')

def dragon():#manages dragon turn
    global player_hp
    dragon_roll = []
    dragon_roll = roll_dice()
    damage = count_rolls(dragon_roll)
    player_hp -= damage
    print(damage, 'damage dealt to the player')
    if player_hp <= 0:
        print('the dragon has died')
        end = True
    else:
        print('player is on ',player_hp,'health')

def main(rounds):
    global dragon_hp
    global player_hp
    global player_stats


    end = False
    while rounds != 0 and end != True:
        player()
        dragon()
        rounds -= 1

    if player_hp < dragon_hp:
        player_stats[0] += 1
        print('player looses')
    elif dragon_hp < player_hp:
        player_stats[1] += 1
        print('dragon looses')
    else:
        player_stats[2] += 1
        print('draw')

    play()

def play():
    global player_stats
    play = 'j'
    rounds = 0
    while play.lower() != 'y' and play.lower != 'n':
        play = str(input('would you like to play dragons battlground? (y/n)'))
        if play.lower() == 'y':
            while rounds > 5 or rounds < 1:
                rounds = int(input('how many rounds would you like to play 1-5'))

            main(rounds)


        elif play.lower() == 'n':
            print('ok have a good day')
            print('wins -', player_stats[0])
            print('losses  ', player_stats[1])
            print('draws -', player_stats[2])






play()




