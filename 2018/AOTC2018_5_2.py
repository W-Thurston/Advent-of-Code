file = open("AOTC2018_5.txt")

data = ["0"]
data_dict = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for j in file:
	for x in alphabet:
		for i in j:
			if i == x or i == x.upper():
				continue

			if i.isupper():
				if data[-1] == i.lower():
					del data[-1]
				else:
					data.append(i)
			else:
				if data[-1] == i.upper():
					del data[-1]
				else:
					data.append(i)
		data_dict[x] = len(data)-1
		data = ["0"]
		
print(data_dict)

#### ^^^^^ Part 2 ^^^^^ ####

