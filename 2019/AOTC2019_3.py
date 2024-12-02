## Part 1 -- https://adventofcode.com/2019/day/3
def find_intersection(w_a, w_b):
    pos_a = [0,0]
    pos_b = [0,0]
    pos_a_list = []
    pos_b_list = []

    intersect_points = []

    ## Wire 1 pathing
    for w1 in w_a:
        number = int(w1[1:])
        direction = w1[0]
        if direction == "U":
            for x in range(0, number):
                pos_a[1] += 1
                pos_a_list.append(pos_a.copy())
        elif direction == "D":
            for x in range(0, number):
                pos_a[1] -= 1
                pos_a_list.append(pos_a.copy())
        elif direction == "R":
            for x in range(0, number):
                pos_a[0] += 1
                pos_a_list.append(pos_a.copy())
        elif direction == "L":
            for x in range(0, number):
                pos_a[0] -= 1
                pos_a_list.append(pos_a.copy())

    ## Wire 2 pathing
    for w2 in w_b:
        number = int(w2[1:])
        direction = w2[0]
        if direction == "U":
            for x in range(0,number):
                pos_b[1] += 1
                pos_b_list.append(pos_b.copy())
        elif direction == "D":
            for x in range(0, number):
                pos_b[1] -= 1
                pos_b_list.append(pos_b.copy())
        elif direction == "R":
            for x in range(0, number):
                pos_b[0] += 1
                pos_b_list.append(pos_b.copy())
        elif direction == "L":
            for x in range(0, number):
                pos_b[0] -= 1
                pos_b_list.append(pos_b.copy())

    ## Part 1
    # intersect_points = [[abs(v) for v in value] for value in pos_a_list if value in pos_b_list]
    # # print(intersect_points)
    # intersect_sums = sorted([abs(sum(value)) for value in intersect_points])
    # print(intersect_sums)

    ## Part 2
    intersect_points = [value for value in pos_a_list if value in pos_b_list]
    #print(intersect_points)

    intersect_dist = []
    for point in intersect_points:
        # print(f"{pos_a_list.index(point)+1} + {pos_b_list.index(point)+1}")
        intersect_dist.append(pos_a_list.index(point) + pos_b_list.index(point)+2)
    print(min(intersect_dist))



if __name__ == '__main__':
    with open("AOTC2019_3_input.txt", 'r') as file:
        wires = file.readlines()


    find_intersection(wires[0].split(","), wires[1].split(","))


