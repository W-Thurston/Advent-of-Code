# Read in input text
with open('input_text.txt', 'r') as file:
    location_lists = file.readlines()

# split each line into respective lists based on indexes
list_a = sorted([int(x[:5]) for x in location_lists])
list_b = sorted([int(x[8:-1]) for x in location_lists])

# take the absolute value of element-wise difference between the two lists
result = sum([abs(a_i - b_i) for a_i, b_i in zip(list_a, list_b)])

# return result -- 1506483
print(result)
