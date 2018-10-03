file = open('txt.txt', 'r')
text = file.read()

santas_position = [0,0]
rsantas_position = [0,0]
position_recorder = {"[0, 0]":2}

count = 0

for i in text:
    
    if count % 2 == 0:
        if i == "^":
            santas_position[0] += 1
        elif i == "v":
            santas_position[0] -= 1  
        elif i == ">":
            santas_position[1] += 1
        elif i == "<":
            santas_position[1] -= 1
    else:
        if i == "^":
            rsantas_position[0] += 1
        elif i == "v":
            rsantas_position[0] -= 1  
        elif i == ">":
            rsantas_position[1] += 1
        elif i == "<":
            rsantas_position[1] -= 1
        
    if str(santas_position) in position_recorder.keys():
        position_recorder[str(santas_position)] += 1
    else:
        position_recorder[str(santas_position)] = 1
    
    if str(rsantas_position) in position_recorder.keys():
        position_recorder[str(rsantas_position)] += 1
    else:
        position_recorder[str(rsantas_position)] = 1    
        
    count += 1     
        
    #print("Santas Current Position:     "+ str(santas_position))
    #print("Robots Current Position:     "+ str(rsantas_position))
    #print(position_recorder , len(position_recorder))
    #print("\n")
            
#print(position_recorder)
print(len(position_recorder))


