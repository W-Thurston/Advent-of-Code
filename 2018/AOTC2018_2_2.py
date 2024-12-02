"""
--- Part Two ---
Confident that your list of box IDs is complete, you're ready to 
find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the 
same position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). 
However, the IDs fghij and fguij differ by exactly one character, the third (h and u). 
Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, 
this is found by removing the differing character from either ID, producing fgij.)
"""

file = open("AOTC2018_2.txt")

data = [x.strip() for x in file]


for x in data:
	length_ = len(x)
	for i in data:
		total = 0
		if len(i) == length_:
			for y in range(length_):
				if x[y] != i[y]:
					total += 1
		if total == 1:
			print("These are the matches:")
			print(x,' <-> ',i)
			
			print("This is the answer: ")
			print( ''.join([j for j in i if j in x]))
			print("-"*20)
			print()

# Your puzzle answer was jiwamotgsfrudclzbyzkhlrvp.