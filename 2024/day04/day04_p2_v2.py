import numpy as np

file = open('./2024/day04/input.txt', 'r').read().split('\n')
grid = np.array([list(x) for x in file])

def isCross(pos):
    x, y = pos
    if 0 < x < grid.shape[0]-1 and 0 < y < grid.shape[1]-1:
        nw_se = grid[x-1,y-1] + grid[x,y] + grid[x+1,y+1]
        ne_sw = grid[x-1,y+1] + grid[x,y] + grid[x+1,y-1]
        if nw_se in ['MAS', 'SAM'] and ne_sw in ['MAS', 'SAM']:
            return True
    return False

As = np.argwhere(grid == 'A')
print(sum(isCross(a) for a in As))