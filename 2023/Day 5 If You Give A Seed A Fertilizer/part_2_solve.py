import tqdm
print()

## Part 2 Example

# almanac = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

# almanac = almanac.split('\n')

#################


with open('2023/Day 5 If You Give A Seed A Fertilizer/input_text.txt') as file:
    almanac = file.read().splitlines()

seed_to_soil = {}
soil_to_fertilizer = {}
fertilizer_to_water = {}
water_to_light = {}
light_to_temperature = {}
temperature_to_humidity = {}
humidity_to_location = {}

seeds_rng = [int(x) for x in almanac[0][almanac[0].index(': ')+2:].split(' ')]
seed_ranges = []
for x in range(0,len(seeds_rng),2):
    seed_ranges.append(range(seeds_rng[x], seeds_rng[x+1], 1))
print(seed_ranges)

for s in tqdm.tqdm(seed_ranges, desc="Seed Ranges", position=0):
    seeds = [x for x in s]
    for seed_idx, seed in enumerate(tqdm.tqdm(seeds, desc="Seed Values", position=1, leave=False)): 
        # print(f"Seed: {seed}")
        for idx, row in enumerate(almanac):
            if idx<2:
                continue
            if 'seed-to-soil map:' in row:
                seed_checked_flag = False
                for line in almanac[idx+1:almanac.index('', idx+1)]:
                    if seed_checked_flag:
                        break
                    line = [int(x) for x in line.split(' ')]
                    if line[1] <= seeds[seed_idx]< line[1]+line[2]:
                        # print(f"seed-to-soil: {seeds[seed_idx]} -> {line[0] + (seeds[seed_idx]-line[1])}")
                        seeds[seed_idx] = line[0] + (seeds[seed_idx]-line[1])
                        seed_checked_flag = True

            elif 'soil-to-fertilizer map:' in row:
                seed_checked_flag = False
                for line in almanac[idx+1:almanac.index('', idx+1)]:
                    if seed_checked_flag:
                        break
                    line = [int(x) for x in line.split(' ')]
                    if line[1] <= seeds[seed_idx]< line[1]+line[2]:
                        # print(f"soil-to-fertilizer: {seeds[seed_idx]} -> {line[0] + (seeds[seed_idx]-line[1])}")
                        seeds[seed_idx] = line[0] + (seeds[seed_idx]-line[1])
                        seed_checked_flag = True

            elif 'fertilizer-to-water map:' in row:
                seed_checked_flag = False
                for line in almanac[idx+1:almanac.index('', idx+1)]:
                    if seed_checked_flag:
                        break
                    line = [int(x) for x in line.split(' ')]
                    if line[1] <= seeds[seed_idx]< line[1]+line[2]:
                        # print(f"fertilizer-to-water map: {seeds[seed_idx]} -> {line[0] + (seeds[seed_idx]-line[1])}")
                        seeds[seed_idx] = line[0] + (seeds[seed_idx]-line[1])
                        seed_checked_flag = True

            elif 'water-to-light map:' in row:
                seed_checked_flag = False
                for line in almanac[idx+1:almanac.index('', idx+1)]:
                    if seed_checked_flag:
                        break
                    line = [int(x) for x in line.split(' ')]
                    if line[1] <= seeds[seed_idx]< line[1]+line[2]:
                        # print(f"water-to-light: {seeds[seed_idx]} -> {line[0] + (seeds[seed_idx]-line[1])}")
                        seeds[seed_idx] = line[0] + (seeds[seed_idx]-line[1])
                        seed_checked_flag = True

            elif 'light-to-temperature map:' in row:
                seed_checked_flag = False
                for line in almanac[idx+1:almanac.index('', idx+1)]:
                    if seed_checked_flag:
                        break
                    line = [int(x) for x in line.split(' ')]
                    if line[1] <= seeds[seed_idx]< line[1]+line[2]:
                        # print(f"light-to-temperature: {seeds[seed_idx]} -> {line[0] + (seeds[seed_idx]-line[1])}")
                        seeds[seed_idx] = line[0] + (seeds[seed_idx]-line[1])
                        seed_checked_flag = True

            elif 'temperature-to-humidity map:' in row:
                seed_checked_flag = False
                for line in almanac[idx+1:almanac.index('', idx+1)]:
                    if seed_checked_flag:
                        break
                    line = [int(x) for x in line.split(' ')]
                    if line[1] <= seeds[seed_idx]< line[1]+line[2]:
                        # print(f"temperature-to-humidity: {seeds[seed_idx]} -> {line[0] + (seeds[seed_idx]-line[1])}")
                        seeds[seed_idx] = line[0] + (seeds[seed_idx]-line[1])
                        seed_checked_flag = True

            elif 'humidity-to-location map:' in row:
                seed_checked_flag = False
                for line in almanac[idx+1:]:
                    if seed_checked_flag:
                        break
                    line = [int(x) for x in line.split(' ')]
                    if line[1] <= seeds[seed_idx]< line[1]+line[2]:
                        # print(f"humidity-to-location: {seeds[seed_idx]} -> {line[0] + (seeds[seed_idx]-line[1])}")
                        seeds[seed_idx] = line[0] + (seeds[seed_idx]-line[1])
                        seed_checked_flag = True

# print(f"Seeds: {seeds}")
# print(seed_tracker)
print(f"Answer: {min(seeds)}") # 251346198
print()