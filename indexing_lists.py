# TODO Create an empty list to maintain the player names

roster = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'

add_player =  input("Would you like to add a player to the roster? (Yes/No):  ")
while add_player.lower() == 'yes':
    name = input("Please provide a player name:  ")
    roster.append(name)
    add_player = input("Would you like to add another player?  (Yes/No):  ")


# TODO print the number of players on the team
print("There are {} players on the team.".format(len(roster)))

# TODO Print the player number and the player name
# The player number should start at the number one
player_number = 1
for player in roster:
    print("Player {}: {}".format(player_number,player))
    player_number += 1

# TODO Select a goalkeeper from the above roster
goalie = input("Please select the goalie by selecting the player's number. 1 - {}:  ".format(len(roster)))

goalie = int(goalie)
# TODO Print the goal keeper's name
# Remember that lists use a zero based index -- we need to sub  from variable above
print("Excellent. The goalie is {}".format(roster[goalie - 1]))


