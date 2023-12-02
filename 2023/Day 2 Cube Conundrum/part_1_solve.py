import re
print()
## Part 1 Example
# list_of_games =   [ "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#                     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#                     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#                     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#                     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
# The Elf would first like to know which games would have been possible if the bag contained
#  only 12 red cubes, 13 green cubes, and 14 blue cubes?
# 
# In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. 
# However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, 
# game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the 
# games that would have been possible, you get 8.


list_of_games = ''
with open("2023\Day 2 Cube Conundrum\input_text.txt", 'r') as file:
    list_of_games = file.read().splitlines()

list_of_possible_games = []

num_red_cubes   = 12
num_green_cubes = 13
num_blue_cubes  = 14

for game in list_of_games:
    
    ## Game is possible flag
    possible_game_flag = True

    ## Pull out game ID
    game_id = int(game[game.index(' '):game.index(':')])

    ## Remove "Game X: " from string
    game = game[game.index(': ')+2:]

    ## Split games into rounds based on ';'
    game = game.split(';')

    ## For each round in a game
    for round in game:

        ## find all 'XX color' combinations
        nums = re.findall(r"\d+ blue|\d+ red|\d+ green", round)

        ## For each number + color combination
        for cube_set in nums:

            ## If blue is in the str
            if 'blue' in cube_set:

                ## remove the ' ' and 'blue' from the str
                cube_set = cube_set.replace(' blue', '')

                ## if the int() that is left is larger than the number of that colored cubes in the game, set game flag to false
                if int(cube_set) > num_blue_cubes:
                    possible_game_flag = False

            ## If red is in the str
            elif 'red' in cube_set:

                ## remove the ' ' and 'red' from the str
                cube_set = cube_set.replace(' red', '')

                ## if the int() that is left is larger than the number of that colored cubes in the game, set game flag to false
                if int(cube_set) > num_red_cubes:
                    possible_game_flag = False

            ## If green is in the str
            elif 'green' in cube_set:

                ## remove the ' ' and 'red' from the str
                cube_set = cube_set.replace(' green', '')

                ## if the int() that is left is larger than the number of that colored cubes in the game, set game flag to false
                if int(cube_set) > num_green_cubes:
                    possible_game_flag = False

        ## START DEBUG ##
        # print(f"{nums} || {possible_game_flag}")
    # print(f"Game {game_id}: {game} || {possible_game_flag}")
    # print(possible_game_flag)
    # print()
    ## END DEBUG ##

    ## If the game was found possible, append the game id to a list
    if possible_game_flag:
        list_of_possible_games.append(game_id)

# print(list_of_possible_games)

## Print out the summation of the game id's that were deemed to be possible
print(f"Answer: {sum(list_of_possible_games)}")
print()
  
