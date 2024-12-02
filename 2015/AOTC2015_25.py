import pandas as pd
import numpy as np



theGrid = pd.DataFrame(0, index=range(10000), columns=range(10000))


lastValue = 20151125
theGrid.iloc[0,0] = lastValue
#print(theGrid.iloc[2891,3075])

rowCounter = 1

while rowCounter < 5000:
    y = 0
    for x in range(rowCounter,-1,-1):
        theGrid.iloc[x,y] = (lastValue * 252533) % 33554393
        lastValue = theGrid.iloc[x,y]
        y += 1
        
    rowCounter += 1
    
    
print(theGrid.iloc[2981,3075])




