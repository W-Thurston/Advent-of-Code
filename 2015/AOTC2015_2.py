file = open('txt.txt', 'r')

dimensions = []

for i in file:
    dimensions.append(i.rstrip())
    
#print (dimensions)

# l x w x h
paper_Area = 0
ribbon_total = 0

for i in dimensions:
    lwh = []
    rlwh = []
    l = int(i[:i.find("x")])
    w  = int(i[(i.find("x"))+1: i.rfind("x")])
    h = int(i[i.rfind("x")+1:])
    
    paper_Area += (2*l*w + 2*w*h + 2*h*l)
    
    lwh.append(l*w)
    lwh.append(w*h)
    lwh.append(h*l)
    min_lwh = min(lwh)

    paper_Area += min_lwh


    bow_length = l*w*h
    
    rlwh.append(l)
    rlwh.append(w)
    rlwh.append(h)
    rlwh.remove(max(rlwh))
    
    ribbon_length = rlwh[0]+rlwh[0]+rlwh[1]+rlwh[1]
    ribbon_total += bow_length + ribbon_length
    
    

print(ribbon_total)    
print(paper_Area)