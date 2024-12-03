import re


# Read in data contents
with open('input_text.txt') as file:
    corrupted_memory = file.readlines()

instruction_list = re.findall('mul\(\d{1,3},\d{1,3}\)', ''.join(corrupted_memory))

total = 0
for instruction in instruction_list:
    start = instruction.find('(')
    middle = instruction.find(',')
    end = instruction.find(')')

    total += int(instruction[start+1:middle]) * int(instruction[middle+1:end])


print(f"Part 1 Total: {total}")