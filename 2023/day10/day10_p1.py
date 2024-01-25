import numpy as np

matrix = list()
input = open('./2023/day10/input.txt', 'r').readlines()
for i,line in enumerate(input):
    matrix.insert(0, [x for x in line.strip()])
    if 'S' in line:
        pos = np.array((line.find('S'), len(input)-i-1))


dir = (0,1) # on the right
l = 0 # tube length
while True:
    pos += dir # move
    l += 1

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

print(int(l/2))