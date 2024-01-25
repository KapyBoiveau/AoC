import numpy as np

dirs = [np.array((0,1)), np.array((1,0)), np.array((0,-1)), np.array((-1,0))] # right, down, left, up
input = open('./2023/day16/input.txt', 'r').readlines()
grid = np.array([list(line.strip()) for line in input])

starts = {((y,-1),0) for y in range(len(grid))} # left column
starts = starts.union({((-1,x),1) for x in range(len(grid[0]))}) # top row
starts = starts.union({((y,len(grid)),2) for y in range(len(grid))}) # right column
starts = starts.union({((len(grid[0]),x),3) for x in range(len(grid[0]))}) # bottom row
maxi = 0
for s in starts:
    energ, beams = set(), {s} # position + direction of the starting beam

    while True:
        if beams:
            pos, dir = beams.pop()
        else:
            break

        pos = tuple(pos + dirs[dir])
        if pos[0] in (-1, len(grid)) or pos[1] in (-1, len(grid[0])):
            continue

        match grid[pos[0]][pos[1]]:
            case '|':
                if dir % 2 == 0:
                    dir = [dir+1, dir-1]
            case '-':
                if dir % 2 == 1:
                    dir = [dir+1, dir-1]
            case '/':
                dir = [dir-1 if dir % 2 == 0 else dir+1] 
            case '\\':
                dir = [dir+1 if dir % 2 == 0 else dir-1] 
        if type(dir) == int: # this is like an else case
            dir = [dir]
        
        for d in dir:
            if (pos, d%4) not in energ:
                beams.add((pos, d%4))
                energ.add((pos, d%4))

    energ = set([x for x,_ in energ]) # remove doublons
    if len(energ) > maxi:
        maxi = len(energ)

print(maxi)