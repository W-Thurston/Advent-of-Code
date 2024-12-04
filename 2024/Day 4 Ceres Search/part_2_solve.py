
with open('input_text.txt') as file:
    word_search = file.readlines()

word_search = [list(x.strip()) for x in word_search]
# for x in word_search:
#     print(x)

def searchDirection(curr_i, curr_j, curr_val):
    # Edge case check -- XMAS won't fit outside these bounds
    edge = 1
    if ((curr_i-1 < 0 and curr_i < edge) or 
       (curr_i+1 > 0 and len(word_search)-curr_i-1 < edge) or 
       (curr_j-1 < 0 and curr_j < edge) or 
       (curr_j+1 > 0 and len(word_search[0])-curr_j-1 < edge)):
        return False
    
    #print(f"[{curr_i},{curr_j}]: {curr_val}")
    if curr_val == 'A':  
        top_left     = word_search[curr_i-1][curr_j-1]
        top_right    = word_search[curr_i-1][curr_j+1]
        bottom_left  = word_search[curr_i+1][curr_j-1]
        bottom_right = word_search[curr_i+1][curr_j+1]

        if (((top_left == 'S' and bottom_right == 'M') and
            ((top_right == 'S' and bottom_left == 'M') or 
             (top_right == 'M' and bottom_left == 'S'))) or
           ((top_left == 'M' and bottom_right == 'S') and
            ((top_right == 'S' and bottom_left == 'M') or 
             (top_right == 'M' and bottom_left == 'S')))):
            return True
    return False
    
total = 0
for i in range(len(word_search)):
    for j in range(len(word_search[i])):
        total += searchDirection(i, j, word_search[i][j])

print(f"Part 2: {total}")