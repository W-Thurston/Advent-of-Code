import re
print()
## Part 1 Example
# calibration_document = ['1abc2',
#                         'pqr3stu8vwx',
#                         'a1b2c3d4e5f',
#                         'treb7uchet']
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

calibration_document = ''
with open('input_text.txt', 'r') as file:
    calibration_document = file.readlines()

part_1_calibration_document = [''.join(re.findall(r'[0-9]', x.replace('\n',''))) for x in calibration_document]
part_1_calibration_document = [int(x[0]+x[-1]) for x in part_1_calibration_document]

part_1_calibration_value = sum(part_1_calibration_document)

print(f"Part 1 Calibration Value: {part_1_calibration_value}")
print()