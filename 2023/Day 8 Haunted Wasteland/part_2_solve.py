import math
import re
from itertools import cycle
print()

## Part 2 Example
## 6
# maps = ["LR",
#         "",
#         "11A = (11B, XXX)",
#         "11B = (XXX, 11Z)",
#         "11Z = (11B, XXX)",
#         "22A = (22B, XXX)",
#         "22B = (22C, 22C)",
#         "22C = (22Z, 22Z)",
#         "22Z = (22B, 22B)",
#         "XXX = (XXX, XXX)"]

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
        
starting_nodes = filter(lambda node: re.fullmatch("[A-Z]{2}A", node), maps_dict.keys())
num_steps = math.lcm(*(count_steps("[A-Z]{2}Z", node) for node in starting_nodes))
print(f"Answer: {num_steps}")
print()
