#
# File:  assign2_hinqc001.py
# Author: Quinn Hindmarsh
# Email ID: hinqc001@mymail.unisa.edu.au
# Description: assesment task 2 for PSP - blackjack
# This is my own work as defined by the University's
# Academic Misconduct policy.
#
print('File      : assign2_hinqc001.py')
print('Author    : Quinn Hindmarsh')
print('Stud ID   : 110445614')
print('Email ID  : hinqc001')
print("This is my own work as defined by the University's Academic Misconduct Policy.\n")

"""                assumptions                """
#any assumptions I made during the development of the code are listed here

import blackjack
 
'''     TO-DO'''
#fix display player (stage 2)


"""                Functions                """

# takes file name and reads contents into list. records stats for each plater.
#the code encapsulated in this function is not mine and was provided for me
def read_file(filename):

    player_list = []
    index = 0
    
    infile = open(filename, "r")

    # Read first line of file.
    line = infile.readline()

    # While not end of file reached i.e. empty string not returned from readline method.
    while line != '':

        # Read name
        name = line.strip('\n')

        # Read in next line
        line = infile.readline()
        
        # Split line into games played, no won, no lost, etc
        info_list = line.split()
        games_played = int(info_list[0])
        no_won = int(info_list[1])
        no_lost = int(info_list[2])
        no_drawn = int(info_list[3])
        chips = int(info_list[4])
        total_score = int(info_list[5])
        
        # Create new player list with player info
        new_player = [name, games_played, no_won, no_lost, no_drawn, chips, total_score]
        
        # Add new player to player_list list
        player_list.append(new_player)
        
        # Read next line of file.
        line = infile.readline()
    
    return player_list

#writes the contents of player list in the same format as it was inputed.
def write_to_file(filename, player_list): #opens file where player data is saved
    print('writing to file')
    with open(filename, 'w') as output:
        for player in player_list:#loops through all players
            output.write(player[0] + '\n')#writes player name, so it is on a line by itself
            output.write(f'{player[1]} {player[2]} {player[3]} {player[4]} {player[5]} {player[6]}\n')#writes the rest of the stats with 1 sp[ace between each on the same line

    output.close()



#takes list of platers and outputs the contents properly formated ( as per the "screen format" specification)
def display_players(player_list):
    print('===========================================================')
    print('-                     Player Summary                      -')
    print('===========================================================')
    print('-                             P  W  L  D   Chips   Score  -')
    print('-----------------------------------------------------------')
    for player in player_list:
        print(f"{player[0]:<29} {player[1]:<2} {player[2]:<2} {player[3]:<2} {player[4]:<3} {player[5]:<10} {player[6]} ")

        print('-----------------------------------------------------------')
    print('===========================================================')
    print()



#takes plater name and list of players and returns the index of that player (returns -1 if not found)
def find_player(player_list, name):
    length = len(player_list)
    for i in range(length):
        if player_list[i][0] == name:
            return i
    return -1

#updates the plater chip balance. promts user for for the amount of chips they would like to buy (1-100)and updates balance
#validates the number of chips, displays a message indicating it has been done and an error message if the player is not found
def buy_player_chips(player_list, name):
    index = find_player(player_list, name)
    if index == -1:
        print('Sorry that player does not exist\n')
        return -1

    print(f'{name} currently has {player_list[index][5]} chips\n')
    done = False
    while not done:
        chips = int(input('How many chips would you like to buy?'))
        if chips < 1 or chips > 100:
            print('You may only buy between 1 and 100 chips at a time\n')
        else:
            player_list[index][5] += chips
            print(f"Succsessfully updated {name}'s chip balance to {player_list[index][5]}\n")
            done = True


#displays the plater with the highest chip vbalance. if two players have the same the one with the lower games is displayed. +
#displays error message if no players are found or if all players have a balance of 0
def display_highest_chip_holder(player_list,silent = False):
    length = len(player_list)
    max_val = 0
    max_index = 0
    for x in range(length):
        if player_list[x][5] > max_val:
            max_val = player_list[x][5]
            max_index = x
        elif player_list[x][5] == max_val:
            if player_list[x][1] < player_list[max_index][1]:
                max_val = player[5]

    if silent == False:#if silent is true the function is being called by another function and should not display text
        if max_val == 0:
            print('Error - no players or all players have 0 chips')
        else:
            print(f'the player with the most chips is {player_list[max_index][0]} with {max_val} chips')

    return max_index


#adds player name to list. if player name already exists error is displayed.
#uses find_player() to check if name already exists first
#chip balanace starts at 100, all other stats start at 0
def add_player(player_list, name):
    find_player(player_list, name)
    if find_player(player_list, name) != -1:
        print('Sorry that player already exists\n')
        return -1
    player_list.append([name, 0, 0, 0, 0, 100, 0])
    print('{} has been added succsesfully'.format(name))

#removes player from list and displays text indicating this has been done
#if player isnt found an error message is returned
#calls find_player()
def remove_player(player_list, name, silent = False):#silent is used to stop the function from displaying text when called by another function

    index = find_player(player_list, name)
    if index == -1:
        if silent == False:
            print('Sorry that player does not exist\n')
        return -1
    else:
        updated_list = [] #i am not allowed to use in built functions to remove this player. so a new list is created with all players but the one to be removed
        length = len(player_list)
        for i in range(length):
            if i != index:
                updated_list.append(player_list[i])
        if silent == False:
            print('{player} has been succsesfully removed'.format(player = name))
        return updated_list


#allows the player to play BlackJack agasint a computer untill they enter n to 'Play again [Y|N]?
#stats are updated after everyround -  +3 points for player win, +1 point for player draw and 0 points awarded for playe loss
#calls blackjack.play_one_game()
def play_blackjack_games(player_list, player_pos):
    play = 'y'
    while play.lower() == 'y':
        player_list[player_pos][1] += 1#adds one to games played
        result, chips = blackjack.play_one_game(player_list[player_pos][5])

        player_list[player_pos][5] = chips#updates chip balance
        player_list[player_pos][6] += result#updates score

        if result == 3:
            player_list[player_pos][2] += 1
        elif result == 1:
            player_list[player_pos][4] += 1
        else:
            player_list[player_pos][3] += 1



        play = input('Play again [Y|N]?')
        if play.lower() != 'y' and play.lower() != 'n':
            print('Invalid input, please enter Y or N')
            play = input('Play again [Y|N]?')


#returrns a copy of player list in desecnding order of chip balance
#when two players have the same balance the one with the lower amount of games played appears first
def sort_by_chips (player_list):
    temp_list = []
    new_sorted_list = []
    for item in player_list:
        temp_list.append(item)

    while len(temp_list) > 0:
        index = display_highest_chip_holder(temp_list, True)
        new_sorted_list.append(temp_list[index])
        temp_list = remove_player(temp_list, temp_list[index][0], True)

    return new_sorted_list





"""                Functions other then the required 10                """




"""                lists                """
player_list = []


"""                main code                """

player_list = read_file("players.txt")


done = False
while not done:
    #done = True
    u_input = str(input('\nplease enter choice \n[list, buy, search, high, add, remove, play, chips, quit]: ')).lower()

    if u_input == 'list':
        print()
        display_players(player_list)

    elif u_input == 'buy':
        player = str(input('please enter player name: '))
        buy_player_chips(player_list, player)


    elif u_input == 'search':
        index = find_player(player_list, input('please enter player name: '))

        if index == -1:
            print('Sorry that player does not exist\n')
        else:
           print('Player name:', player_list[index][0], '\nGames Played:', player_list[index][1], '\nGames won:', player_list[index][2], '\nGames lost:', player_list[index][3], '\nGames drawn:', player_list[index][4], '\nChips:', player_list[index][5], '\nScore:', player_list[index][6])

    elif u_input == 'high':
        display_highest_chip_holder(player_list)

    elif u_input == 'add':
        add_player(player_list, input('please enter player name: '))

    elif u_input == 'remove':
        temp = remove_player(player_list, input('please enter player name: '))
        if temp != -1:
            player_list = temp



    elif u_input == 'play':
        player_name = input('please enter player name: ')
        index = find_player(player_list, player_name)
        if index == -1:
            print(f'{player_name} is not found in player list.\n')
        else:
            play_blackjack_games(player_list, index)

    elif u_input == 'chips':
        desc_list = []
        desc_list = sort_by_chips(player_list)
        display_players(desc_list)

    elif u_input == 'quit':
        done = True
        print("\n\n-- Program terminating --\n")
        write_to_file("players.txt", player_list)

    else:
        print('\n Not a valid command - please try again\n')
        #done = False










