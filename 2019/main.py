## Part 1

def intcode_computer(l):
    position = 0

    l[1] = 12
    l[2] = 2


    while position < len(l):
        # print(f"Sequence: {l[position:position+4]}")

        if l[position] == 1:
            t = l[l[position+1]] + l[l[position+2]]
            # print(f"{l[l[position+1]]} + {l[l[position+2]]} = {t}")
            # print(f'{l[l[position + 3]]} now is {t}')
            l[l[position + 3]] = t
        elif l[position] == 2:
            t = l[l[position + 1]] * l[l[position + 2]]
            # print(f"{l[l[position + 1]]} * {l[l[position + 2]]} = {t}")
            # print(f'{l[l[position + 3]]} now is {t}')
            l[l[position + 3]] = t
        elif l[position] == 3:
            l[l[position+1]] = input("Value: ")
        elif l[position] == 4:
            print(l[position+1])
        elif l[position] == 99:
            break
        else:
            print("Uh Oh")
            break

        position += 4

    print(f"l[0]: {l[0]}")



if __name__ == '__main__':
    with open("AOTC2019_2_input.txt", 'r') as file:
        line = file.readlines()

    input = [int(x) for x in line[0].split(",")]
    intcode_computer(input)


