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

final_seq = []

while len(final_seq) < len(key_list):
	print("Final: ", final_seq)
	print("Queue: ", queued_letters)
	next_in_line = queued_letters.pop(0)
	print("Next : ", next_in_line)

	for i in seq_dict:
		if next_in_line in seq_dict[i]:
			print("B Seq_dict: ",i,":", seq_dict[i])
			del seq_dict[i][seq_dict[i].index(next_in_line)]
			print("A Seq_dict: ",i,":", seq_dict[i])
		if seq_dict[i] == []:
			print(i,"being added to queue because: ",seq_dict[i])
			seq_dict[i] = [0]
			queued_letters.append(i)
			queued_letters.sort()
	final_seq.append(next_in_line)
	print("#"*15)
	print()

print(''.join(final_seq))
