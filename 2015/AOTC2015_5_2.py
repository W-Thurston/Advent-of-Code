import re

file = open('AOTC2015_5.txt', 'r')

text = []

for i in file:
    text.append(i.rstrip())

file.close()


pattern4 = re.compile(r"(..)(.*)\1")
pattern5 = re.compile(r"(.)(.)\1")
nice = {}
niceCount = 0
for x in text:

    print("\n")
    print(x)
    if re.search(pattern4, x) :
        nice[x] = "Nice"
        print(" Matches Pattern 4")

    else: 
        nice[x] = "Naughty"
        print("DOES NOT MATCH PATTERN 4")
        continue
    
    
    if re.search(pattern5, x) :
        nice[x] = "Nice"
        print(" Matches Pattern 5")

    else: 
        nice[x] = "Naughty"
        print("DOES NOT MATCH PATTERN 5")    
        continue

for k,v in nice.items():
    #print( str(k)+": "+str(v))
    if v == "Nice":
        niceCount += 1

print("\n" +"PART 2 - Total number of Nice strings: "+str(niceCount))
