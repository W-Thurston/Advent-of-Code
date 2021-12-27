import math

with open('Day 1 The Tyranny of the Rocket Equation_1.txt','r') as file:
	input_text = file.read()
	
input_text = input_text.split('\n')

## SOLUTION 1
# final_fuel_count = 0
# for i in input_text[:-1]:
	# final_fuel_count += (math.floor(int(i)/3))-2
	
#print(final_fuel_count)


## SOLUTION 2
def find_fuel_needed(i, final_fuel_count):
	fuel = (math.floor(int(i)/3))-2
	
	
	if fuel <=0:
		#print(final_fuel_count, fuel)
		return final_fuel_count 
	else:
		final_fuel_count += fuel
		final_fuel_count = find_fuel_needed(fuel, final_fuel_count)
	return final_fuel_count 
	
	
final_fuel_count = 0
for i in input_text[:-1]:
	final_fuel_count += find_fuel_needed(i, 0)
	
print(final_fuel_count)