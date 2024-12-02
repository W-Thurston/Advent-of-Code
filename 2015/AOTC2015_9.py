from itertools import permutations

input_file = open("AOTC2015_9.txt")
data = []

for lines in input_file:
	data.append(lines.rstrip())
    
    
fullDistanceDict = {}
listOfLocations = []

for lines in data:
    listOfLines = lines.split(' ')
    
    fullDistanceDict[str(listOfLines[0]+" "+listOfLines[1]+" "+listOfLines[2])] = listOfLines[4]
    fullDistanceDict[str(listOfLines[2]+" "+listOfLines[1]+" "+listOfLines[0])] = listOfLines[4]
    
    if listOfLines[0] not in listOfLocations:
        listOfLocations.append(listOfLines[0])
        #print(listOfLines[0])
    elif listOfLines[2] not in listOfLocations:
        listOfLocations.append(listOfLines[2])
        #print(listOfLines[2])
    

perm = permutations(listOfLocations)
listPerms = list(perm)


finalDistance = {}

for i in listPerms:

    totalMiles = 0
    totalMiles += int(fullDistanceDict[str(i[0]+" to "+i[1])]) # 1
    totalMiles += int(fullDistanceDict[str(i[1]+" to "+i[2])]) # 2
    totalMiles += int(fullDistanceDict[str(i[2]+" to "+i[3])]) # 3
    totalMiles += int(fullDistanceDict[str(i[3]+" to "+i[4])]) # 4
    totalMiles += int(fullDistanceDict[str(i[4]+" to "+i[5])]) # 5
    totalMiles += int(fullDistanceDict[str(i[5]+" to "+i[6])]) # 6
    totalMiles += int(fullDistanceDict[str(i[6]+" to "+i[7])]) # 7
    
    finalDistance[str(i)] = totalMiles


key_max = max(finalDistance.keys(), key=(lambda k: finalDistance[k]))
key_min = min(finalDistance.keys(), key=(lambda k: finalDistance[k]))

## Part 1
print('Minimum Value: ',finalDistance[key_min],' For key: ',key_min)

## Part 2
print('Maximum Value: ',finalDistance[key_max],' For key: ',key_max)

