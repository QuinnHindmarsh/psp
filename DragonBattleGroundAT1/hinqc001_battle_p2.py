#
# File:  hinqc001_battle_p1.py
# Author: Quinn Hindmarsh
# Email Id: hinqc001
# Description: Assignment 1 – text based adventure game Dragon Battleground
# This is my own work as defined by the University's
# Academic Misconduct policy.
#

def display_details():
    print("File     : hinqc001_battle_p1.py")
    print("Author   : Quinn Hindmarsh")
    print("Email ID : hinqc001")
    print("This is my own work as defined by the\nUniversity's Academic Misconduct Policy.\n")
display_details()



#assumptions
"""
all assumptions i have made while creating the project are listed here

i assume if both the dragon and player die it is a draw regardless of which one is further into the negatives with hp
"""

from dice import display_dice #used to display dice
import random #used to roll dice

end = False #flag used to end game when chararhter dies
player_stats = [0,0,0,0] #keeps track of player stats. 0 = wins, 1 = loss, 2 = draw, 3 = dragon killed

dragon_hp = 100#the amount of hp the dragon has, starts at 100
player_hp = 100#the amount of hp the player has starts at 100


play = 'j'#used to allow the player to play as many games as they want 'j' is just a placeholder
rounds = 0#tracks the amount of rounds that has been player

def roll_dice():#returns a single dice roll
    return random.randint(1,6)

def roll_damage():#calls roll_dice() to generate a full hand
    hand = []
    for itteration in range(0,5,1):
        hand.append(roll_dice())
    return hand


def calculate_damage(hand):#works out the total damage, multiplier included
    roll_frequency = [0, 0, 0, 0, 0, 0,0]  # all elements but element0 corripsond to the amount of times that number was rolled. eg if roll_frequency[2] == 3 then 3 2s where rolled
    for item in hand:
        roll_frequency[item] += 1

    # finds the appropraite damage multiplier to use
    damage_multiplier = 1
    if roll_frequency[1] == 3 or roll_frequency[3] == 3 or roll_frequency[5] == 3:
        damage_multiplier = 0
        print('-- swing and miss - no damage inflicted!')
    else:
        max = 0#used to find the highest number of duplicates
        for itteration in range(len(roll_frequency)):
            if roll_frequency[itteration] > max:
                max = roll_frequency[itteration]

        if max == 3:
            damage_multiplier = 3
            print('-- Critical hit - triple the damage!')
        elif max == 2:
            damage_multiplier = 2
            print('-- Hit - double the damage!')

    sum_damage = 0#holds the sum of the dice rolled before multipliers
    for i in hand:
        sum_damage += i

    return damage_multiplier * sum_damage#returns total danage after multiplier

while play != 'n': #loops until player quits

    if player_stats[0] == 0 and player_stats[1] == 0 and player_stats[2] == 0: #if its there first time playing say this
        play = str(input('Would you like to play Dragon Battleground [y|n]? '))

    else:#if they have already done 1+ round say this
        play = str(input('Play again [y|n]? '))

    if play == 'n':
        #peints stats
        if player_stats[0] != 0 or player_stats[1] != 0 or player_stats[2] != 0:
            print('\n\nGame Summary')
            print('============')
            print('you played {} games'.format(str(player_stats[0]+player_stats[1]+player_stats[2])))
            print('  |--> Games won: ',player_stats[0])
            print('  |--> Games lost: ', player_stats[1])
            print('  |--> Games drawn: ', player_stats[2])
            print('  |--> Dragons killed: ', player_stats[3],end='\n')
            print('\nThanks for playing!')
        else:
            print('\n\nNo worries... you live to battle another day... :)')#prints this is game hasnt been played

    elif play != 'y' and play != 'n':#data validation
        print("Please enter either 'y' or 'n'.\n")


    elif play == 'y': #plays game

        while rounds > 5 or rounds < 1:#gets round num
            rounds = int(input('\nPlease enter number of battle rounds: '))

            if rounds < 1 or rounds > 5:#data validation
                print('Must be between 1-5 inclusive.')
        print('\n')
        print('-- Battle -- Player versus Dragon:', rounds, 'rounds --\n\n')

        count = 1 #keeps track of current round
        while rounds != 0 and end != True:#loops until all rounds have been played or a charather is dead

            print('Round:', count)



            """                                                     ***PLAYERS TURN***                                                     """
            input()  # pauses untill user enters any key - makes it easier to follow game
            player_roll = roll_damage()

            print('Player rolled: ')
            display_dice(player_roll)
            print()


            player_damage = calculate_damage(player_roll)#total damage player will do after multiplier


            print('-- Player has dealt', player_damage, 'damage')
            dragon_hp = dragon_hp - player_damage

            if dragon_hp <= 0:#if dragon is dead
                end = True



            """                                                     ***DRAGONS TURN***                                                     """
            input()#pauses untill user enters any key - makes it easier to follow game
            dragon_roll = roll_damage()

            dragon_damage = calculate_damage(dragon_roll)

            player_hp -= dragon_damage
            print('-- Dragon has dealt', dragon_damage, 'damage\n')
            if player_hp <= 0:
                end = True


            print('> Player - Damage taken:',dragon_damage,'- Current health:', player_hp)
            print('> dragon - Damage taken:',player_damage,'- Current health:', dragon_hp,'\n\n')

            rounds -= 1
            count += 1

        print('\n\n-- End of battle --\n')
        if player_hp <= 0:
            print('-- Player has died!  :(\n')
        if dragon_hp <= 0:#its importantant this isnt a elif as both the dragon and player can die simultaniously
            print('-- Dragon has died!  :(\n')
            player_stats[3] += 1

        if dragon_hp == player_hp or (dragon_hp <= 0 and player_hp <= 0): #if both dragon and player dies its a draw
            player_stats[2] += 1
            print('** Draw! **')
        elif player_hp > dragon_hp:
            player_stats[0] += 1
            print('** Player wins! **')
        elif player_hp < dragon_hp:
            player_stats[1] += 1
            print('** Dragon wins! **')

        print('\n')