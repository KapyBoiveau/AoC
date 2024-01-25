import itertools as iter
import numpy as np

input = open('./2023/day11/input.txt', 'r').readlines()
universe = [list(line.strip().replace('.','0').replace('#','1')) for line in input]
uni = np.array(universe)

# get empty rows and columns numbers
eCols = [i for i,x in enumerate(np.sum(uni,axis=0)) if x == 0]
eRows = [i for i,x in enumerate(np.sum(uni,axis=1)) if x == 0]

# get galaxies pos
galaxies = [tuple(x) for x in np.asarray(np.where(uni == 1)).T]

# get every duo of galaxies
duos = iter.combinations(galaxies, 2)

total = 0
for duo in duos:
    x1, x2 = min((duo[0][1], duo[1][1])), max((duo[0][1], duo[1][1]))
    y1, y2 = min((duo[0][0], duo[1][0])), max((duo[0][0], duo[1][0]))

# get the number of empty rows and columns between the duo
    n = len([0 for x in eCols if x > x1 and x < x2])
    n += len([0 for y in eRows if y > y1 and y < y2])
    
# add this number to the distance separating the duo
    total += x2 - x1 + y2 - y1 + (1000000-1)*n
    
print(total)