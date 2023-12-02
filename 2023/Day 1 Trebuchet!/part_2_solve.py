import regex as re

## Part 2 Example
# calibration_document = ['two1nine',
#                         'eightwothree',
#                         'abcone2threexyz',
#                         'xtwone3four',
#                         '4nineeightseven2',
#                         'zoneight234',
#                         '7pqrstsixteen']
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

calibration_document = ''
with open('input_text.txt', 'r') as file:
    calibration_document = file.readlines()


word_to_num_dict = {'one'  : '1',
                    'two'  : '2',
                    'three': '3',
                    'four' : '4',
                    'five' : '5',
                    'six'  : '6',
                    'seven': '7',
                    'eight': '8',
                    'nine' : '9'}

part_2_calibration_value = 0
for line in calibration_document:
    nums = re.findall(r"one|two|three|four|five|six|seven|eight|nine|\d", line, overlapped=True)
    
    for idx, n in enumerate(nums):
        if n.isdigit():
            nums[idx] = n
        else:    
            nums[idx] = word_to_num_dict[n]
    
    nums = nums[0] + nums[-1]

    part_2_calibration_value += int(nums)

print()
print(f"Part 2 Calibration Value: {part_2_calibration_value}")
print()