import re

iFile = open("AOTC2015_12.txt",'r')
data = ''

for lines in iFile:
    data = lines.rstrip()
    
### Part 1
pattern1 = re.compile(r"[+-]?\d+")

numbers = re.findall(pattern1, data)

sum = 0
for i in numbers:
    sum += int(i)

print("Part 1: "+str(sum))

### Part 2
