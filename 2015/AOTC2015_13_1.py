import re
import itertools

###############################################################################
###############################################################################

file = open('AOTC2015_13.txt', 'r')
data = []
for line in file:
    data.append(line.rstrip())
    
file.close()

###############################################################################
###############################################################################

nameDict = {}
nameList = []
patternDigit = "\d+"




for x in data:
    #print(x)
    increment = re.findall(patternDigit,x)
    m =  re.search(patternDigit,x)
    posOrNeg = x[:m.start()-1][-4:]
    actualNumber = 0
    
    if posOrNeg == "lose":
        actualNumber = -int(increment[0])
    else:
        actualNumber = int(increment[0])
    
    buildTuple = ()
    
    
    
    nameDict[x[:x.find(' ')]] = []
    if x[:x.find(' ')] == 'Alice':
        buildTuple = (x[x.rfind(' ')+1:-1],actualNumber)
        nameList.append(buildTuple)
        
        if len(nameList) == 7:
            nameDict['Alice'] = nameList
            nameList = []
            
    elif x[:x.find(' ')] == 'Bob':
        buildTuple = (x[x.rfind(' ')+1:-1],actualNumber)
        nameList.append(buildTuple)
        
        if len(nameList) == 7:
            nameDict['Bob'] = nameList
            nameList = []
            
    elif x[:x.find(' ')] == 'Carol':
        buildTuple = (x[x.rfind(' ')+1:-1],actualNumber)
        nameList.append(buildTuple)
        
        if len(nameList) == 7:
            nameDict['Carol'] = nameList
            nameList = []
            
    elif x[:x.find(' ')] == 'David':
        buildTuple = (x[x.rfind(' ')+1:-1],actualNumber)
        nameList.append(buildTuple)
        
        if len(nameList) == 7:
            nameDict['David'] = nameList
            nameList = []
            
    elif x[:x.find(' ')] == 'Eric':
        buildTuple = (x[x.rfind(' ')+1:-1],actualNumber)
        nameList.append(buildTuple)
        
        if len(nameList) == 7:
            nameDict['Eric'] = nameList
            nameList = []
            
    elif x[:x.find(' ')] == 'Frank':
        buildTuple = (x[x.rfind(' ')+1:-1],actualNumber)
        nameList.append(buildTuple)
        
        if len(nameList) == 7:
            nameDict['Frank'] = nameList    
            nameList = []
            
    elif x[:x.find(' ')] == 'George':
        buildTuple = (x[x.rfind(' ')+1:-1],actualNumber)
        nameList.append(buildTuple)
        
        if len(nameList) == 7:
            nameDict['George'] = nameList
            nameList = []
            
    elif x[:x.find(' ')] == 'Mallory':
        buildTuple = (x[x.rfind(' ')+1:-1],actualNumber)
        nameList.append(buildTuple)
        
        if len(nameList) == 7:
            nameDict['Mallory'] = nameList
            nameList = []
   
   
   
# for k,v in nameDict.items():
#     print(str(k)+": "+str(v))
    
    
newDict = {}

for k,v in nameDict.items():
    for i in range(0,7):
        #print(str(str(k)+" to "+str(v[i][0]))+" = "+ str(v[i][1]))
        newDict[str(str(k)+" to "+str(v[i][0]))] = int(v[i][1])
        
for k,v in newDict.items():
    if str(str(k[str(k).rfind(" ")+1:]) +" to "+ str(k[:str(k).find(" ")])) in newDict:
        oldValue = int(newDict[str(str(k[str(k).rfind(" ")+1:]) +" to "+ str(k[:str(k).find(" ")]))])
        newDict[k] = oldValue + int(v)
        
        
    print( str(k)+"= "+str(newDict[k]))

     
namesList = ['Alice',
'Bob',
'Carol',
'David',
'Eric',
'Frank',
'George',
'Mallory']

