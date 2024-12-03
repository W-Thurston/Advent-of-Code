import re


# Read in data contents
with open('input_text.txt') as file:
    corrupted_memory = file.readlines()

# Join together the list of strings
corrupted_memory = "".join(corrupted_memory).replace("\n", "")

instructions_list = re.sub(r"don't\(\).*?(do\(\)|$)", "", corrupted_memory)

for d in (corrupted_memory, instructions_list):
    muls = re.findall(r"(?<=mul\()\d{1,3},\d{1,3}(?=\))", d)
    print(sum(eval(m.replace(",", "*")) for m in muls))