import numpy as np

file = open('./2024/day06/input.txt', 'r').read()
lab = np.array([list(x) for x in file.split('\n')])
lab = np.pad(lab, 1, constant_values='~')
# tuple (pos, dir) dir = 0 : up, 1 : right, 2 : down, 3 : left
pos = (tuple(np.argwhere(lab == '^')[0].tolist()), 0)
lab[pos[0]] = '.' # start

def move(pos_dir):
    pos, d = pos_dir
    if d % 2 == 0: # up or down
        nextPos = (pos[0] + (1 if d == 2 else -1), pos[1])
    else: # left or right
        nextPos = (pos[0], pos[1] + (1 if d == 1 else -1))

    if lab[nextPos] == '#': # if next pos is a wall
        return move((pos, (d + 1) % 4)) # rotate and move again
    return (nextPos, d)

obstacles = set()
while True:    
    # find where he wants to go
    nextPos = move(pos)
    
    if lab[nextPos[0]] == '~': # if glouglou
        break
    lab[nextPos[0]] = '#' # place a wall
    
    posSet = set()
    while lab[pos[0]] != '~':
        pos = move(pos)
        if pos in posSet: # already been there ...
            obstacles.add(nextPos[0])
            break
        posSet.add(pos)
    
    lab[nextPos[0]] = '.' # remove wall
    pos = nextPos

print(len(obstacles))