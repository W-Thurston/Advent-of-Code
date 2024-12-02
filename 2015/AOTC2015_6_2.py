import re
import numpy as np

ifile = open("AOTC2015_6.txt",'r')
fileLines = []

for line in ifile:
    fileLines.append(line.rstrip())
    
ifile.close() 
    
theGrid = np.zeros((1000,1000))


instruct = ""
cords = ""
cord1 = ""
cord2 = ""    


def toggle(grid, startX, startY, endX, endY):
    for i in range(int(startX), int(endX)+1):
        for j in range(int(startY), int(endY)+1):            
            grid[i,j] += 2
                             
    return grid     
        
def turn_off(grid, startX, startY, endX, endY):
    for i in range(int(startX), int(endX)+1):
        for j in range(int(startY), int(endY)+1):
            if grid[i,j] > 0:
                grid[i,j] -= 1
            else:
                grid[i,j] = 0
            
    return grid
    
def turn_on(grid, startX, startY, endX, endY):
    for i in range(int(startX), int(endX)+1):
        for j in range(int(startY), int(endY)+1):
            grid[i,j] += 1
    
    return grid

    
# turnOnCount  = 0
# turnOffCount = 0
# toggleCount  = 0
    
    
for i in fileLines:
    oldI = i
    i = i.replace(" through "," ")
    fileLines[fileLines.index(oldI)] = i
    
    m = re.search('\d', i)
    instruct = i[:m.start()-1]
    cords = i[m.start():]
    
    cord1, cord2 = cords.split(" ")
    
    cord1_x = cord1[:cord1.find(',')]
    cord1_y = cord1[cord1.find(',')+1:]

    cord2_x = cord2[:cord2.find(',')]
    cord2_y = cord2[cord2.find(',')+1:]
    
    if instruct == "toggle":
        theGrid = toggle(theGrid, cord1_x, cord1_y, cord2_x, cord2_y)
        #toggleCount +=1
    elif instruct == "turn off":
        theGrid = turn_off(theGrid, cord1_x, cord1_y, cord2_x, cord2_y)
        #turnOffCount +=1
    elif instruct == "turn on":
        theGrid = turn_on(theGrid, cord1_x, cord1_y, cord2_x, cord2_y)
        #turnOnCount +=1
    else:
        print("THERE WAS AN ISSUE: "+ instruct+"}") 
        
print(sum(sum(theGrid)))

