import numpy as np
import re

input = open('./2023/day14/input.txt', 'r').readlines()
plateform = np.array([list(line.strip()) for line in input])

n, dir, rest = 0, -1, 0
prev = dict()
while True:
    dir = (dir + 1) % 4
    n += int(dir == 3)
    upLeft = dir < 2
    upDown = dir % 2 == 0
    l = len(plateform[0]) if upDown else len(plateform)
    
    for j in range(0,l):
        trunc = plateform[:,j] if upDown else plateform[j]
        line = ''.join(trunc)
        for m in re.finditer(r'([^#]+)', line):
            g = m.group(1)
            if upLeft:
                tilt = ['O' if i < g.count('O') else '.' for i in range(len(g))]
            else:
                tilt = ['.' if i < g.count('.') else 'O' for i in range(len(g))]
            if upDown:
                plateform[m.start(1):m.end(1), j] = np.array(tilt)
            else:
                plateform[j, m.start(1):m.end(1)] = np.array(tilt)
    
    if rest == 0:
        if dir == 3:
            pFlat = dir, tuple(plateform.flatten())
            if pFlat in prev:
                rest = (1000000000 - n) % ((n - prev[pFlat]))
            else:
                prev[pFlat] = n
    else:
        rest -= (dir == 3)
        if rest == 0:
            break

total = 0
for i,line in enumerate(np.flipud(plateform)):
    total += np.count_nonzero(line == 'O') * (i+1)
print(total)