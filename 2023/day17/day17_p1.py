import numpy as np
import sys

directions = np.array([(0,1),(1,0),(0,-1),(-1,0)])
def around(pos, d):
    result = []
    for dir in directions:
        if tuple(d+dir) != (0,0): # not opposite dir
            newPos = pos + dir
            if 0 <= newPos[0] < len(map) and 0 <= newPos[1] < len(map[0]):
                result.append(tuple(newPos))
    return result

input = open('./2023/day17/input.txt', 'r').read().split('\n')
map = np.array([list(line) for line in input], dtype=int)
goal = tuple(map.shape - np.array([1,1]))
visitSet = set()

# row 1 : current pos + dir + inertia, row 2 : heat (row 3 : path taken / for visualisation)
paths = np.array([[((0,0), (0,1), 0)], [0]], dtype=object)

while True:
    x = np.argmin(paths[1])
    (pos, dir, speed), heat = paths[0,x], paths[1,x]

    newPos, newHeats = [], []
    for p in around(pos, dir):
        d = tuple(np.array(p)-pos) # new dir
        s = speed + 1 if dir == d else 1
        if s <= 3:
            if (p, d, s) not in visitSet:
                newPos.append((p, d, s))
                newHeats.append(map[p] + heat)
                visitSet.add((p, d, s))
                
    for i in range(len(newPos)):
        if newPos[i][0] == goal:
            print(newHeats[i])
            exit()
    
    paths = np.delete(paths, x, 1)
    paths = np.concatenate((paths, np.array([newPos, newHeats], dtype=object)), axis=1)