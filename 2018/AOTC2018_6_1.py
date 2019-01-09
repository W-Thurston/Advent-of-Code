import numpy as np
import pandas as pd

file = open("AOTC2018_6.txt")

def split(s):
	x, y = s.split(", ")
	return (int(x), int(y))

data = [split(i.strip()) for i in file]

grid = pd.DataFrame(index=np.arange(350), columns = np.arange(350))

marker = ['A','B','C','D','E','F','G','H',
		  'I','J','K','L','M','N','O','P',
		  'Q','R','S','T','U','V','W','X',
		  'Y','Z',
		  'AA','BB','CC','DD','EE','FF',
		  'GG','HH','II','JJ','KK','LL',
		  'MM','NN','OO','PP','QQ','RR',
		  'SS','TT','UU','VV','WW','XX']

manhattan_dist = []

grid_x = grid.shape[0]
grid_y = grid.shape[1]


marker_dict = {}
safe_area = 0
# Part 1
for x in range(grid_x):
    for y in range(grid_y):
        manhattan_dist = [( abs(i[0] - x) + abs(i[1] - y)) for i in data]
        index_min_dist = manhattan_dist.index(min(manhattan_dist))
        #### Part 2 ####
        if sum(manhattan_dist) < 10000:
            safe_area += 1
        ################
        
        if manhattan_dist.count(min(manhattan_dist)) > 1:
            grid.iloc[x,y] = '.'
        else:
            grid.iloc[x,y] = marker[index_min_dist].lower()
            if marker[index_min_dist] in marker_dict:
                marker_dict[marker[index_min_dist]] += 1
            else:
                marker_dict[marker[index_min_dist]] = 1
        print("(",x,",",y,")")# is closest to", marker[index_min_dist])

        manhattan_dist = []


for i in range(len(data)):
    grid.iloc[data[i][0],data[i][1]] = marker[i]         