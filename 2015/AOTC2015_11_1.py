import itertools

p1 = "vzbxkghb"

# Original: vzbxxyzz
# had to add 1 to the end making the "-yzz" become "-zaa" to force the next iteration
p2 = "vzbxxzaa"
#iString = "abcdffaa"
# wacaabcc

asciiList = []
for i in p1:
    asciiList.append(ord(i))
    
#print(asciiList)
    
def check_password(l):
    flagList = [False, True, False]
    
    # Flag 1 - one increasing straight of at least three letters
    for i in range(0,len(l)):
        if (i+2) <= (len(l)-1):
            if l[i]+1 == l[i+1]:
                if l[i]+2 == l[i+2]:
                    flagList[0] = True
                    
    # Flag 2 - may not contain the letters i (105), o (111), or l (108)
    for i in [105,111,108]:
        if i in l:
            flagList[1] = False
            break
    
    # Flag 3 - at least two different, non-overlapping pairs of letters, like aa, bb, or zz
    count = 0
    for k,g in itertools.groupby(l):
        if len(list(g)) == 2:
            count += 1
    if count == 2:
        flagList[2] = True
                
    #print(all(flagList))
    return all(flagList)
    
def reverse_find(l, value):
    for i in range(len(l)-1,0,-1):
        if l[i] == value:
            return i
    
    
while check_password(asciiList) is False:
    
    if asciiList[-1] != ord('z'):
        asciiList[-1] += 1
    else:
        asciiList[-1] = ord('a')
        if asciiList[-2] != ord('z'):
            asciiList[-2] += 1
        else:
            asciiList[-2] = ord('a')
            if asciiList[-3] != ord('z'):
                asciiList[-3] += 1
            else:
                asciiList[-3] = ord('a')
                if asciiList[-4] != ord('z'):
                    asciiList[-4] += 1
                else:
                    asciiList[-4] = ord('a')
                    if asciiList[-5] != ord('z'):
                        asciiList[-5] += 1
                    else:
                        asciiList[-5] = ord('a')
                        if asciiList[-6] != ord('z'):
                            asciiList[-6] += 1
                        else:
                            asciiList[-6] = ord('a')
                            if asciiList[-7] != ord('z'):
                                asciiList[-7] += 1
                            else:
                                asciiList[-7] = ord('a')
                                if asciiList[-8] != ord('z'):
                                    asciiList[-8] += 1
                                else:
                                    asciiList[-8] = ord('a')
    print(asciiList)
    
    
    
check_password(asciiList)
aList = []
for i in asciiList:
    aList.append(chr(i))

print(''.join(aList))
