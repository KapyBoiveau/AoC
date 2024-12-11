import numpy as np

grid = np.array([list(x) for x in open('./2024/day10/input.txt', 'r').read().split('\n')], dtype=int)
grid = np.pad(grid, 1, constant_values=-1)

def around(pos, val):
    y, x = pos
    posAround = [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]
    return [(ny, nx) for ny, nx in posAround if grid[ny, nx] == val + 1]

def walk(pos):
    y, x = pos
    if grid[y,x] == 9:
        return {(y,x)}
    return set().union(*(walk(a) for a in around(pos, grid[y,x])))
    
print(sum(len(walk(pos)) for pos in np.argwhere(grid == 0)))