import numpy as np

grid = np.array([list(x) for x in open('./2024/day10/input.txt', 'r').read().split('\n')], dtype=int)
grid = np.pad(grid, 1, constant_values=-1)

def around(pos):
    y, x = pos
    return [(y-1,x), (y,x-1), (y,x+1), (y+1,x)]

def walk(pos):
    y, x = pos
    nbFinish = set()
    if grid[y,x] == 9:
        return {(y,x)}
    for a in around(pos):
        if grid[a] == grid[y,x] + 1:
            nbFinish.update(walk(a))
    return nbFinish
    
print(sum(len(walk(pos)) for pos in np.argwhere(grid == 0)))