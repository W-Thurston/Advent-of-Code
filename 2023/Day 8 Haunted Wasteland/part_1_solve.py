import math
import re
from itertools import cycle
print()


## Part 1 Example
# ## 2
# maps = ["RL",
#         "",
#         "AAA = (BBB, CCC)",
#         "BBB = (DDD, EEE)",
#         "CCC = (ZZZ, GGG)",
#         "DDD = (DDD, DDD)",
#         "EEE = (EEE, EEE)",
#         "GGG = (GGG, GGG)",
#         "ZZZ = (ZZZ, ZZZ)"]

# ## 6
# maps = ["LLR",
#         "",
#         "AAA = (BBB, BBB)",
#         "BBB = (AAA, ZZZ)",
#         "ZZZ = (ZZZ, ZZZ)"]


pattern = r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)"
with open('2023/Day 8 Haunted Wasteland/input_text.txt', 'r') as file:
    maps = file.read().splitlines()

navigation = maps[0]
maps = maps[2:]

maps_dict = {}
for line in maps:
    k, *v = re.fullmatch(pattern, line.rstrip()).groups()
    maps_dict[k] = v

def count_steps(pattern, node):
    for count, lr_index in enumerate(cycle(map("LR".index, navigation)), start=1):
        node = maps_dict[node][lr_index]
        if re.fullmatch(pattern, node):
            return count
        

num_steps = count_steps("ZZZ", "AAA")
print(f"Answer: {num_steps}")
print()

