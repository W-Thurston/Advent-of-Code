###### 
# DOES NOT WORK!!!!!
# Look at File AOTC2018_7_2.txt for breakdown
######



file = open("AOTC2018_7.txt")

data =[lines.strip() for lines in file]

###
seq_dict = {}
key_list = []
for line in data:
	key_list.append(line[5])
	key_list.append(line[-12])
	if line[-12] in seq_dict:
		seq_dict[line[-12]] += [line[5]]
	else:
		seq_dict[line[-12]] = [line[5]]

key_list = list(set(key_list))
###

###
queued_letters = []
for i in key_list:
	if i not in seq_dict:
		queued_letters.append(i)

queued_letters.sort()
###

workers_list = [[],[],[],[],[]]

final_seq = []

while len(final_seq) < len(key_list):
	print("Final: ", final_seq)
	print("Queue: ", queued_letters)
	# print("Worke: ", workers_list)
	# next_in_line = queued_letters.pop(0)
	# print("Next : ", next_in_line)

	for i in queued_letters:
		temp = [len(x) for x in workers_list]
		smallest_sublist = temp.index(min(temp))
		for x in range( ord(i)-4 ):
			workers_list[ smallest_sublist ].append(i)

	temp = []
	for x in queued_letters:
		print("Checking for:",x)
		for i in seq_dict:
			if x in seq_dict[i]:
				print("B Seq_dict: ",i,":", seq_dict[i])
				del seq_dict[i][seq_dict[i].index(x)]
				print("A Seq_dict: ",i,":", seq_dict[i])
			if seq_dict[i] == []:
				print(i,"being added to queue because: ",seq_dict[i])
				seq_dict[i] = [0]
				temp.append(i)
		final_seq.append(x)

	queued_letters = sorted(temp)
	print("#"*15)
	print()

# for i in workers_list:
# 	print(i)
print(final_seq)

import pandas as pd

a = pd.DataFrame(workers_list)
print(a.T.apply(pd.value_counts))


# print([len(x) for x in workers_list])
