"""
--- Part Two ---
Amidst the chaos, you notice that exactly one claim doesn't overlap by 
even a single square inch of fabric with any other claim. If you can somehow 
draw attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are made.

What is the ID of the only claim that doesn't overlap?
"""


import numpy as np
import re

grid = np.zeros((1000,1000))


file = open("AOTC2018_3.txt")

data = [x.strip() for x in file]


get_coordinates = re.compile("\d*,\d*")
get_size		= re.compile("\d*x\d*")


for i in range(len(data)):
	m_coord = re.search(get_coordinates, data[i])
	m_size  = re.search(get_size, data[i])
	if m_coord and m_size:
		# print(m_coord.group(0))
		# print(m_size.group(0))

		x_coord = int(str(m_coord.group(0))[:str(m_coord.group(0)).find(",")])
		y_coord = int(str(m_coord.group(0))[str(m_coord.group(0)).find(",")+1:])
		# print(x_coord)
		# print(y_coord)

		x_size  = int(str(m_size.group(0))[:str(m_size.group(0)).find("x")])
		y_size  = int(str(m_size.group(0))[str(m_size.group(0)).find("x")+1:])
		# print(x_size)
		# print(y_size)

		grid[x_coord:x_coord+x_size, y_coord:y_coord+y_size] += 1

		

for i in range(len(data)):
	m_coord = re.search(get_coordinates, data[i])
	m_size  = re.search(get_size, data[i])
	if m_coord and m_size:
		x_coord = int(str(m_coord.group(0))[:str(m_coord.group(0)).find(",")])
		y_coord = int(str(m_coord.group(0))[str(m_coord.group(0)).find(",")+1:])
		

		x_size  = int(str(m_size.group(0))[:str(m_size.group(0)).find("x")])
		y_size  = int(str(m_size.group(0))[str(m_size.group(0)).find("x")+1:])

		if int(sum(sum(grid[x_coord:x_coord+x_size, y_coord:y_coord+y_size]))) == (x_size*y_size):
			print(data[i])


# Your puzzle answer was 650.