import numpy as np

file = open('./2024/day06/input.txt', 'r').read()
lab = np.array([list(x) for x in file.split('\n')])
lab = np.pad(lab, 1, constant_values='~')

def move(pos_dir):
    pos, d = pos_dir
    if d % 2 == 0: # up or down
        nextPos = (pos[0] + (1 if d == 2 else -1), pos[1])
    else: # left or right
        nextPos = (pos[0], pos[1] + (1 if d == 1 else -1))

    if lab[nextPos[0], nextPos[1]] == '#':
        return (pos, (d + 1) % 4)
    return (nextPos, d)

# tuple (pos, dir) dir = 0 : up, 1 : right, 2 : down, 3 : left
pos = (tuple(np.argwhere(lab == '^')[0].tolist()), 0)

allPos = set()
while(lab[pos[0]] != '~'): # while not swimming
    pos = move(pos)
    allPos.add(pos[0])

print(len(allPos))