import re

file = open("AOTC2015_7.txt",'r')
data = []

for line in file:
    data.append(line.rstrip())
    
file.close()


theDict = {}

for i in data:
    value, key = i.split(" -> ")
    theDict[key] = value


bitwiseDict = {"AND":"&", "OR":"|", "RSHIFT":">>", "LSHIFT":"<<", "NOT":"~"}    

for key, value in theDict.items():
    aList = value.split(' ')
    for i,v in enumerate(aList):
        if v in bitwiseDict.keys():
            aList[i] = bitwiseDict[v]
    aString = ' '.join(aList)
    theDict[key]= aString
    

##############################################################################


def solved_solution(d):
    aList = []
    for key, value in d.items():
        try:
            int(value)
            is_dig = True
        except ValueError:
            is_dig = False
        if is_dig:
            aList.append(key)
             
    return aList
         

def assign_values(aDict): 
    listOfSolved = solved_solution(aDict)
    print(listOfSolved)
    print("The following have matches in the list above:")
    digitList = []
    
    
    for key,value in aDict.items():
        for i in listOfSolved:

            match = re.search(r"\b" + i + r"\b", value)
            #print("Trying to match: "+ i)
            #print("TO: "+key+": "+value)
            if match:
                print("There is a match with the solved index:  "+i+"' in: key:"+key+", value:"+value)
                
                boolList = []
                for char in value.replace(match.group(0), aDict[match.group(0)]):
                    boolList.append(char.isalpha())
                if not any(boolList):
                    aDict[key] = str(eval(value.replace(match.group(0), aDict[match.group(0)])))
                    print("The new value for key "+key+" is: "+str(eval(aDict[key])))
                    print()
                else:
                    aDict[key] = value.replace(match.group(0), aDict[match.group(0)])
                    print("The new value for key "+key+" is: "+aDict[key])
                    print()
                if key =='i':
                    print("WHY IS THIS NOT ")
    
    for v in aDict.values():
        digitList.append(v.isalpha())
            
    if all(digitList):
        print("All True")
        print()
        # print(digitList)
        return aDict
    else:
        print("Not quite yet!")
        print()
        #assign_values(aDict)
    return aDict


 
while not (theDict['a'].isdigit()):
    theDict = assign_values(theDict)


print(theDict['a']) 
