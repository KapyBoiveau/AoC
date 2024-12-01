import numpy as np

dirs = np.array([(0,1),(1,0),(0,-1),(-1,0)])
def around(pos):
    global toDoNext
    for dir in dirs:
        newDir = tuple(pos+dir)
        if map[newDir] in ('.'):
            toDoNext.add(newDir)

input = open('./2023/day21/input.txt', 'r').read().split('\n')
map = np.array([list(line) for line in input])
sPos = tuple([x[0] for x in np.where(map == 'S')])
map[sPos] = '.'

toDo = {sPos}
for _ in range(64):
    toDoNext = toDo.copy()
    for pos in toDo:
        around(pos)
    toDo = toDoNext.difference(toDo)

print(len(toDo))