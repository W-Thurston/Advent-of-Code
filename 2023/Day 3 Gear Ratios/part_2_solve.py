import re
from math import prod
print()

## Part 2 Example
# engine_schematic = [".467..114...",
#                     "....*.......",
#                     "...35..633..",
#                     ".......#....",
#                     ".617*.......",
#                     "......+.58..",
#                     "...592......",
#                     ".......755..",
#                     "....$.*.....",
#                     "..664..598.."]

# In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345.
# The second gear is in the lower right; its gear ratio is 451490. 
# (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) 
# Adding up all of the gear ratios produces 467835.

## Read in input text
with open('2023\Day 3 Gear Ratios\input_text.txt', 'r') as file:
    engine_schematic = [f'.{row}.' for row in file.read().split('\n')]

## Final variable to be returned
actual_gear_ratios = 0

## For each row in the input text
for row_num, row in enumerate(engine_schematic):

    ## Find each asterix (*) in the row
    for gear_pos in re.finditer(r'\*', row):
        possible_gears = []
        start_gear_pos = gear_pos.span()[0]
        end_gear_pos   = gear_pos.span()[1]

        ## If this is not the first row in the data
        ## Check the row above current line
        if row_num>0:

            ## Find each number in the above row
            for part_num in re.finditer(r'\d+', engine_schematic[row_num-1]):

                ## Create a range of indexes to search within to find the '*'
                part_num_span = [x for x in range(part_num.span()[0], part_num.span()[1]+1)]

                ## If the '*' is found within the above list of indexes, append that part_num to the "possible_gears" list
                if start_gear_pos in part_num_span:
                    possible_gears.append(int(part_num.group()))
                elif end_gear_pos in part_num_span:
                    possible_gears.append(int(part_num.group()))
        
        ## Find each number in the current row
        for part_num in re.finditer(r'\d+', row):

            ## Create a range of indexes to search within to find the '*'
            part_num_span = [x for x in range(part_num.span()[0], part_num.span()[1]+1)]
            
            ## If the '*' is found within the above list of indexes, append that part_num to the "possible_gears" list
            if start_gear_pos in part_num_span:
                possible_gears.append(int(part_num.group()))
            elif end_gear_pos in part_num_span:
                possible_gears.append(int(part_num.group()))

        ## If this is not the last row in the data
        ## Check the row below current line
        if row_num < len(engine_schematic):
            for part_num in re.finditer(r'\d+', engine_schematic[row_num+1]):

                ## Create a range of indexes to search within to find the '*'
                part_num_span = [x for x in range(part_num.span()[0], part_num.span()[1]+1)]

                ## If the '*' is found within the above list of indexes, append that part_num to the "possible_gears" list
                if start_gear_pos in part_num_span:
                    possible_gears.append(int(part_num.group()))
                elif end_gear_pos in part_num_span:
                    possible_gears.append(int(part_num.group()))
                    
        ## If the list of possible gears is only a length of 2, multiply those two values and add them to the actual_gear_ratio total
        if len(possible_gears) == 2:
            actual_gear_ratios += prod(possible_gears)


print(f"Answer: {actual_gear_ratios}") # Answer: 81709807
print()
