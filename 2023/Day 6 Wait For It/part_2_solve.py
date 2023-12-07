from math import prod
from tqdm import tqdm
print()

## Part 2 Example
# records =   ["Time:      7  15   30",
#              "Distance:  9  40  200"]

with open('2023/Day 6 Wait For It/input_text.txt', 'r') as file:
    records = file.read().splitlines()


time = int(''.join(records[0][5:].split()))
distance = int(''.join(records[1][9:].split()))


defeat_the_record_counter = 0
defeated_record_holder = []


defeat_the_record_counter = 0
for holding_time in tqdm(range(time)):
    remaining_time = time-holding_time
    travel_distance = remaining_time * holding_time
    # print(f"{holding_time} mm/s for {remaining_time} seconds traveling a distance of {distance} millimeters; The record is {distances}")

    if travel_distance > distance:
        defeat_the_record_counter += 1

defeated_record_holder.append(defeat_the_record_counter)

# print(f"We can defeat the record in {defeat_the_record_counter} ways for a timer of {time}")
# print()

print(f"Answer: {prod(defeated_record_holder)}")
print()