"""
--- Part Two ---

Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.

Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:

    Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
    If you only have one number left, stop; this is the rating value for which you are searching.
    Otherwise, repeat the process, considering the next bit to the right.

The bit criteria depends on which type of rating value you want to find:

    To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
    To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.

For example, to determine the oxygen generator rating value using the same example diagnostic report from above:

    Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
    Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
    In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
    In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
    In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
    As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.

Then, to determine the CO2 scrubber rating value from the same example above:

    Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
    Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
    In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
    As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.

Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.

Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)

Input: Day_3_Binary_Diagnostic.txt
Answer: 2845944

"""

with open('Day_3_Binary_Diagnostic.txt', 'r') as f:
    file = f.readlines()

file = [lines.strip() for lines in file]


o2_generator_rating_list = [file,[],[],[],[],[],[],[],[],[],[],[],[]]
co2_scrubber_rating_list = [file,[],[],[],[],[],[],[],[],[],[],[],[]]
o2_generator_str = ''
co2_scrubber_str = ''

o2_generator_rating = ''
co2_scrubber_rating = ''


for bit_position in range(len(file[0])):
    counter_list = [0,0]
    for line in o2_generator_rating_list[bit_position]:
        ## Count 0's or 1's in current bit_position
        counter_list[int(line[bit_position])] += 1
        
    if counter_list[1] >= counter_list[0]:
        o2_generator_str += '1'
    else:
        o2_generator_str += '0'

    # print(f"O2 Generator counter: {len(o2_generator_rating_list[bit_position])}")
    # print(f"Counter_list: {counter_list}")
    # print(f"O2_str : {o2_generator_str}")
    

    counter_list = [0,0]
    for line in co2_scrubber_rating_list[bit_position]:
        ## Count 0's or 1's in current bit_position
        counter_list[int(line[bit_position])] += 1
        
    if counter_list[1] >= counter_list[0]:
        co2_scrubber_str += '0'
    else:
        co2_scrubber_str += '1'

    # print()
    # print(f"Co2_scrubber counter: {len(co2_scrubber_rating_list[bit_position])}")
    # print(f"Counter_list: {counter_list}")
    # print(f"Co2_str: {co2_scrubber_str}")


    o2_generator_rating_list[bit_position+1] = [x for x in file if x.startswith(o2_generator_str)]
    co2_scrubber_rating_list[bit_position+1] = [x for x in file if x.startswith(co2_scrubber_str)]


    if len(o2_generator_rating_list[bit_position+1]) == 1:
        o2_generator_rating = o2_generator_rating_list[bit_position+1][0]

    if len(co2_scrubber_rating_list[bit_position+1]) == 1:
        co2_scrubber_rating = co2_scrubber_rating_list[bit_position+1][0]

    if (len(co2_scrubber_rating_list[bit_position+1]) == 1) & (len(o2_generator_rating_list[bit_position+1]) == 1):
        print(f"{o2_generator_rating}")
        print(f"{co2_scrubber_rating}")
        break
    
    # print("-"*10)

print("-"*10)
print(f"O2 Generator Rating Binary: {o2_generator_rating}")
print(f"CO2 Scrubber Rating Binary: {co2_scrubber_rating}")
print("-"*10)
print(f"O2 Generator Rating Decimal: {int(o2_generator_rating,2)}")
print(f"CO2 Scrubber Rating Decimal: {int(co2_scrubber_rating,2)}")
print("-"*10)
print(f"Life Support Rating: {int(o2_generator_rating,2)*int(co2_scrubber_rating,2)}")
print("-"*10)