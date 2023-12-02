
with open('Calorie_Counting_1.txt', 'r') as f:
    calories = f.readlines()

cal_inventory = [[]]

counter = 0

for i in calories:
    if i =='\n':
        cal_inventory.append([])
        counter += 1
    else:
        cal_inventory[counter].append(eval(i))
        

max_cal = [sum(x) for x in cal_inventory]

print(max(max_cal))