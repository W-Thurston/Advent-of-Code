import re

file = open('AOTC2015_5.txt', 'r')

text = []

for i in file:
    text.append(i.rstrip())

file.close()

pattern1 = re.compile('[aeiou]')
pattern2 = re.compile(r"(.)\1")
pattern3 = ['ab', 'cd', 'pq', 'xy']


nice = {}
niceCount = 0
for x in text:
    #print("\n")
    #print(x)

    # Pattern 1
    if len(re.findall(pattern1, x)) >= 3 :
        nice[x] = "Nice"
        #print(" Matches Pattern 1")

    else:
       nice[x] = "Naughty"
       #print("DOES NOT MATCH PATTERN 1")
       continue


    # Pattern 2
    if re.search(pattern2, x) :
        nice[x] = "Nice"
        #print(" Matches Pattern 2")

    else:
        nice[x] = "Naughty"
        #print("DOES NOT MATCH PATTERN 2")
        continue


    # Pattern 3
    pattern3Count = 0
    for j in pattern3:
        if j not in x:
            pass
        else:
            pattern3Count += 1
            break;

    if pattern3Count == 0:
        nice[x] = "Nice"
        #print(" Matches Pattern 3")
    else:
        nice[x] = "Naughty"
        #print("DOES NOT MATCH PATTERN 3")
        continue


for k,v in nice.items():
    if v == "Nice":
        niceCount += 1

print("PART 1 - Total number of Nice strings: "+str(niceCount))



