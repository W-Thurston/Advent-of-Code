def main():
    with open('input_text.txt') as file:
        map = file.readlines()

    map = [list(x.strip()) for x in map]

    curr_position = ()
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '^':
                curr_position = (i, j)

    def moveForward(direction, curr_i, curr_j):
        if direction == 'UP':
            for x in range(1,curr_i+1):
                if map[curr_i-x][curr_j] == '#':
                    break
                map[curr_i-x][curr_j] = 'X'
                if curr_i-x == len(map)-1:
                    return (None, None)
            new_position = (curr_i-x+1, curr_j)

        elif direction == 'DOWN':
            for x in range(1,len(map)-curr_i):
                if map[curr_i+x][curr_j] == '#':
                    break
                map[curr_i+x][curr_j] = 'X'
                if curr_i+x == len(map)-1:
                    return (None, None)
            new_position = (curr_i+x-1, curr_j)
            

        elif direction == 'RIGHT':
            for x in range(1,len(map[curr_i])-curr_j):
                if map[curr_i][curr_j+x] == '#':
                    break
                map[curr_i][curr_j+x] = 'X'
                if curr_j+x == len(map[curr_i])-1:
                    return (None, None)
            new_position = (curr_i, curr_j+x-1)

        elif direction == 'LEFT':
            for x in range(1,curr_j+1):
                if map[curr_i][curr_j-x] == '#':
                    break
                map[curr_i][curr_j-x] = 'X'
                if curr_j-x == 0:
                    return (None, None)
            new_position = (curr_i, curr_j-x+1)
            
        return new_position
    
    direction = 'UP'
    while (curr_position != (None, None)):
        curr_position = moveForward(direction, curr_position[0], curr_position[1])

        if direction == 'UP':
            direction = 'RIGHT'
        elif direction == 'DOWN':
            direction = 'LEFT'
        elif direction == 'RIGHT':
            direction = 'DOWN'
        elif direction == 'LEFT':
            direction = 'UP'

    total = 0
    for x in map:
        total += x.count('X')
        total += x.count('^')

    print(f"Part 1: {total}")


if __name__ == '__main__':
    main()