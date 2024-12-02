import re
print()

## Part 1 Example
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

#In this schematic, two numbers are not part numbers because they are not adjacent to a symbol:
# 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; 
# their sum is 4361.

with open('2023\Day 3 Gear Ratios\input_text.txt', 'r') as file:
    engine_schematic = [f'.{row}.' for row in file.read().split('\n')]

actual_part_numbers = []

for row_num, row in enumerate(engine_schematic):

    for part_num in re.finditer(r'\d+', row):
        start_part_num = part_num.span()[0]
        end_part_num   = part_num.span()[1]

        symbols = ['-', '$', '&', '%', '=', '@', '/', '*', '#', '+']
        
        actual_part_flag = False

        ## Check current row for symbols
        ## If the character in the same row before the number is a symbol
        if row[start_part_num-1] in symbols:
            actual_part_flag = True

        ## If the character in the same row after the number is a symbol
        if row[end_part_num] in symbols:
            actual_part_flag = True

        if not actual_part_flag:
            ## Check row above
            ## Skip checking the row above; we're on the first row
            if row_num != 0:
                
                ## For each index from 1 before the part num to 1 after the part num for the row above
                for i in range(start_part_num-1, end_part_num+1):
                    if engine_schematic[row_num-1][i] in symbols:
                        actual_part_flag = True
            
        if not actual_part_flag:
            ## Check row below
            ## Skip checking the row above; we're on the first row
            if row_num != len(engine_schematic)-1:

                ## For each index from 1 before the part num to 1 after the part num for the row below
                for i in range(start_part_num-1, end_part_num+1):
                    if engine_schematic[row_num+1][i] in symbols:
                        actual_part_flag = True

        if actual_part_flag:
            actual_part_numbers.append(int(part_num.group()))

print(f"Answer: {sum(actual_part_numbers)}") # Answer: 538046
print()
