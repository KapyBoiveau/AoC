import numpy as np
import re

lines = open('./2024/day04/input.txt', 'r').read().split('\n')
x = np.array([list(l) for l in lines])

def getPos(m, i, reverse = False):
    if reverse:
        return (m, len(x) - m + i - 1) if i < 0 else (m + i, len(x) - m - 1) # oof
    else:
        return (m, m - i) if i < 0 else (m + i, m)

posA1, posA2 = set(), set() # a set for each diag orientation
for i in range(-len(x)+1, len(x)): # for each diag "number" (start point)
    for goal in ['MAS', 'SAM']: # finditer doesn't work with overlapping matches

        for m in re.finditer(goal, ''.join(np.diag(x, i))): # find every goal
            posA1.add(getPos(m.span()[0]+1, i)) # getPos of A in goal

        for m in re.finditer(goal, ''.join(np.diag(np.flipud(x), i))): 
            posA2.add(getPos(m.span()[0]+1, i, True)) 

print(len(posA1.intersection(posA2)))