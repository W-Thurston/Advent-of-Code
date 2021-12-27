with open('Day 2 1202 Program Alarm_1.txt','r') as file:
	input_text = file.read()

# input_text = [int(x) for x in input_text.split(',')]
# input_text[1] = 12
# input_text[2] = 2

# intcode_iter = iter(range(len(input_text)))

# for i in intcode_iter:
	
	# if input_text[i] == 1:
		# print("Addition: {} + {}".format(input_text[input_text[i+1]],input_text[input_text[i+2]]))
		# input_text[input_text[i+3]] = input_text[input_text[i+1]]+input_text[input_text[i+2]]
		# next(intcode_iter)
		# next(intcode_iter)
		# next(intcode_iter)
	
	# elif input_text[i] == 2:
		# print("Multiply: {} + {}".format(input_text[input_text[i+1]],input_text[input_text[i+2]]))
		# input_text[input_text[i+3]] = input_text[input_text[i+1]]*input_text[input_text[i+2]]
		# next(intcode_iter)
		# next(intcode_iter)
		# next(intcode_iter)
		
	# elif input_text[i] == 99:
		# print("HALT")
		# break
	# else: 
		# print("Not an opcode")
	
	
# print(input_text[0])

## Part Two
for noun in range(100):
	for verb in range(100):
		input_tex = [int(x) for x in input_text.split(',')]
		input_tex[1] = noun
		input_tex[2] = verb

		intcode_iter = iter(range(len(input_tex)))

		for i in intcode_iter:
			
			if input_tex[i] == 1:
				#print("Addition: {} + {}".format(input_tex[input_tex[i+1]],input_tex[input_tex[i+2]]))
				input_tex[input_tex[i+3]] = input_tex[input_tex[i+1]]+input_tex[input_tex[i+2]]
				next(intcode_iter)
				next(intcode_iter)
				next(intcode_iter)
			
			elif input_tex[i] == 2:
				#print("Multiply: {} + {}".format(input_tex[input_tex[i+1]],input_tex[input_tex[i+2]]))
				input_tex[input_tex[i+3]] = input_tex[input_tex[i+1]]*input_tex[input_tex[i+2]]
				next(intcode_iter)
				next(intcode_iter)
				next(intcode_iter)
				
			elif input_tex[i] == 99:
				#print("HALT")
				break
			
			
		if input_tex[0] == 19690720:
			print("#"*100)
			print("#"*100)
			print("#"*100)
			print("#"*100)
			print(100*noun+verb)
			break
			break
