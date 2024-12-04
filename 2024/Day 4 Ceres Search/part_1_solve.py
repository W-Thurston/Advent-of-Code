
with open('input_text.txt') as file:
    word_search = file.readlines()

word_search = [list(x.strip()) for x in word_search]
for x in word_search:
    print(x)

def searchDirection(curr_i, curr_j, next_i, next_j, curr_val):
    # Edge case check -- XMAS won't fit outside these bounds
    edge = 3
    if ((next_i < 0 and curr_i < edge) or 
       (next_i > 0 and len(word_search)-curr_i-1 < edge) or 
       (next_j < 0 and curr_j < edge) or 
       (next_j > 0 and len(word_search[0])-curr_j-1 < edge)):
        return False
    
    # print(f"[{curr_i},{curr_j}]->[{next_i},{next_j}]: {curr_val}->{next_val}", end=', ')
    word_so_far = []
    if curr_val == 'X':  
        for x in range(1,4):
            word_so_far.append(curr_val)
            next_val = word_search[curr_i+(next_i*x)][curr_j+(next_j*x)]
            if (word_so_far == ['X', 'M']) or (word_so_far == ['X', 'M', 'A']) or (word_so_far == ['X', 'M', 'A', 'S']):
                print(f"{curr_val}->{next_val}", end=', ')
            else:
                print(f"{curr_val}->{next_val}")
            if curr_val == 'X':
                if next_val == 'M':
                    print(f"[{curr_i},{curr_j}]->[{curr_i+(next_i*x)},{curr_j+(next_j*x)}]: {curr_val}->{next_val} ({word_so_far})", end=', ')
                    curr_val = next_val
                    continue
                else:
                    print(f"[{curr_i},{curr_j}]->[{curr_i+(next_i*x)},{curr_j+(next_j*x)}]: {curr_val}->{next_val} ({word_so_far}) ~BREAK~")
                    print()
                    break
            elif curr_val == 'M':
                if next_val == 'A':
                    print(f"[{curr_i},{curr_j}]->[{curr_i+(next_i*x)},{curr_j+(next_j*x)}]: {curr_val}->{next_val} ({word_so_far})", end=', ')
                    curr_val = next_val
                    continue
                else:
                    print(f"[{curr_i},{curr_j}]->[{curr_i+(next_i*x)},{curr_j+(next_j*x)}]: {curr_val}->{next_val} ({word_so_far}) ~BREAK~")
                    print()
                    break
            elif curr_val == 'A':
                if next_val == 'S':
                    print(f"[{curr_i},{curr_j}]->[{curr_i+(next_i*x)},{curr_j+(next_j*x)}]: {curr_val}->{next_val} ({word_so_far+['S']})")
                    return True
                else:
                    print(f"[{curr_i},{curr_j}]->[{curr_i+(next_i*x)},{curr_j+(next_j*x)}]: {curr_val}->{next_val} ({word_so_far}) ~BREAK~")
                    print()
                    break
            else:
                print(f"[{curr_i},{curr_j}]->[{curr_i+(next_i*x)},{curr_j+(next_j*x)}]: {curr_val}->{next_val} ({word_so_far}) ~BREAK~")
                print()
                break
    return False
    
total = 0
for i in range(len(word_search)):
    for j in range(len(word_search[i])):
        for x in range(-1,2):
            for y in range(-1,2):
                if x == 0 and y==0:
                    continue
                total += searchDirection(i, j, x, y, word_search[i][j])

print(f"Part 1: {total}")