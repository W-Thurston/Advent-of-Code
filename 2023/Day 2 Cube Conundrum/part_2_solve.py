import re
print()
## Part 2 Example
# list_of_games =   [ "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#                     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#                     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#                     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#                     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
# As you continue your walk, the Elf poses a second question: in each game you played, 
# what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
# 
# In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
# Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
# Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
# Game 4 required at least 14 red, 3 green, and 15 blue cubes.
# Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.


list_of_games = ''
with open("2023\Day 2 Cube Conundrum\input_text.txt", 'r') as file:
    list_of_games = file.read().splitlines()

list_of_games_cube_powers = []

for game in list_of_games:
    
    ## Pull out game ID
    game_id = int(game[game.index(' '):game.index(':')])

    ## Remove "Game X: " from string
    game = game[game.index(': ')+2:]

    ## Pull out the maximum number shown within each game for each cube color
    blue_cubes  = max([int(''.join(filter(str.isdigit, x))) for x in re.findall("\d+ blue",  game)])
    red_cubes   = max([int(''.join(filter(str.isdigit, x))) for x in re.findall("\d+ red",   game)])
    green_cubes = max([int(''.join(filter(str.isdigit, x))) for x in re.findall("\d+ green", game)])

    ## Append the "power" of the current set of cubes a list
    list_of_games_cube_powers.append(blue_cubes*red_cubes*green_cubes)

    # print(game)
    # print(f"Blue min : {blue_cubes}")
    # print(f"Red min  : {red_cubes}")
    # print(f"Green min: {green_cubes}")
    # print(f"Cube Power: {blue_cubes*red_cubes*green_cubes}")
    # print()

## Print out the summation of the game id's that were deemed to be possible
print(f"Answer: {sum(list_of_games_cube_powers)}")
print()
  
