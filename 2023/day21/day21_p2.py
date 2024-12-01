import numpy as np
import math

dirs = np.array([(0,1),(1,0),(0,-1),(-1,0)])
def around(pos):
    global toDoNext
    for dir in dirs:
        newDir = tuple(pos+dir)
        if map[newDir] in ('.'):
            toDoNext.add(newDir)

input = open('./2023/day21/input.txt', 'r').read().split('\n')
map = np.array([list(line) for line in input])
nbRocks = len(np.where(map == '#')[0])
shape = map.shape

steps = 50
steps = steps - math.trunc(shape[0]/2)
full = int(steps / shape[0])
full1, full2 = math.ceil(full / 2), math.floor(full/2)
#savoir si c'est map1 == full1 (et map2 == full2) ou l'inverse
steps -= shape[0] * full

sPos = tuple([x[0] for x in np.where(map == 'S')])
sPosBonusList = [(sPos[0], 0), (sPos[0], shape[1]-1), (0,sPos[1]), (shape[0]-1, sPos[1])]
bonus = sum([move(p, steps-1) for p in sPosBonusList])

map[sPos] = '.' # useless ?
map1, map2 = map.flatten()[::2], map.flatten()[1::2]
nbR1, nbR2 = list(map1).count('#'), list(map2).count('#')
nbO1, nbO2 = len(map1) - nbR1, len(map2) - nbR2


def move(sPos, n):
    if n < 0:
        return 0
    
    toDo = {sPos}
    for _ in range(n):
        toDoNext = toDo.copy()
        for pos in toDo:
            around(pos)
        toDo = toDoNext.difference(toDo)

    return len(toDo)

'''
for pos in toDo:
    map[pos] = 'O'
for l in map:
    print(''.join(l))
'''