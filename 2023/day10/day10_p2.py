import numpy as np

matrix = list()
input = open('./2023/day10/input.txt', 'r').readlines()
for i,line in enumerate(input):
    matrix.insert(0, [x for x in line.strip()])
    if 'S' in line:
        start = np.array((line.find('S'), len(input)-i-1))

pos = start
dir = (0,-1) # go down
tubeSet = set()
while True:
    pos += dir # move
    tubeSet.add(tuple(pos))

    match matrix[pos[1]][pos[0]]:
        #case '-': # same direction
        #case '|': # same direction
        case 'L':
            dir = (1,0) if dir == (0,-1) else (0,1)
        case 'J':
            dir = (-1,0) if dir == (0,-1) else (0,1)
        case '7':
            dir = (-1,0) if dir == (0,1) else (0,-1)
        case 'F':
            dir = (1,0) if dir == (0,1) else (0,-1)
        case 'S':
            break

nb = 0
matrix[start[1]][start[0]] = '|' # cheat code
for y,line in enumerate(matrix):
    lf, cross = '.', 0
    for x in range(len(line)):    
        if (x,y) not in tubeSet:
            nb += cross % 2
        elif matrix[y][x] != '-':
            if lf in ('.','|'):
                lf = matrix[y][x]
            elif (lf, matrix[y][x]) in (('F','J'), ('L','7')):
                lf = '|'
            elif lf in ('F','L'): 
                lf = '.'
            cross += int(lf == '|')
print(nb)