file = open("AOTC2018_5.txt")

data = ["0"]

for j in file:
	for i in j:

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
		
print(len(data)-1) 

#### ^^^^^ Part 1 ^^^^^ ####

