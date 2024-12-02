from math import prod
print()

## Part 1 Example
# records =   ["Time:      7  15   30",
#              "Distance:  9  40  200"]

with open('2023/Day 6 Wait For It/input_text.txt', 'r') as file:
    records = file.read().splitlines()


times = records[0][5:].split()
times = [int(x) for x in times]
distances = records[1][9:].split()
distances = [int(x) for x in distances]

defeat_the_record_counter = 0
defeated_record_holder = []

for idx, time in enumerate(times):
    defeat_the_record_counter = 0
    for holding_time in range(time):
        remaining_time = time-holding_time
        travel_distance = remaining_time * holding_time
        # print(f"{holding_time} mm/s for {remaining_time} seconds traveling a distance of {travel_distance} millimeters; The record is {distances[idx]}")

        if travel_distance > distances[idx]:
            defeat_the_record_counter += 1

    defeated_record_holder.append(defeat_the_record_counter)

    # print(f"We can defeat the record in {defeat_the_record_counter} ways for a timer of {time}")
    # print()

print(f"Answer: {prod(defeated_record_holder)}")
print()