def read_file(filename):
# List to store player information
player_list = []
index = 0

# Open file for reading.
infile = open(filename, "r")

# Read first line of file.
line = infile.readline()

# While not end of file reached i.e. empty string not returned from readline method.
while line != '':
# Read name in file
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

# Return the player list
return player_list

def find_player(player_list, name):

    index = 0
    for player in player_list:
        if player[0] == name:
            return index
        else:
            return -1
        index += 1

'''
def remove_player(player_list, name):


removed_list = []
player_index = find_player(player_list, name)

if player_index == -1:
print("Error - The player could not be found!")
else:
index = 0
while index < len(player_list):

if player_list[index][0] != name:
removed_list.append(player_list[index])

index += 1
print(f"Successfully removed {name} from the player list!")

return removed_list
'''

temp_list = read_file("test_file.txt")

print(temp_list)

# remove_player(temp_list, "Bruce Wayne")

#for player in temp_list:
 #   print(player)