# Read in input text
with open('input_text.txt', 'r') as file:
    location_lists = file.readlines()

# split each line into respective lists based on indexes
list_a = sorted([int(x[:5]) for x in location_lists])
list_b = sorted([int(x[8:-1]) for x in location_lists])

# calculate similarity score
similarity_score = 0
for number in list_a:
    similarity_score += number * list_b.count(number)

# return result -- 23126924
print(similarity_score)