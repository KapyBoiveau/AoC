import numpy as np
import re

input = open('./2023/day14/input.txt', 'r').readlines()
plateform = np.array([list(line.strip()) for line in input])

for j in range(0,len(plateform[0])):
    col = ''.join([x for x in plateform[:,j]])
    for m in re.finditer(r'([^#]+)', col):
        nbO = m.group(1).count('O')
        tilt = ['O' if i < nbO else '.' for i in range(len(m.group(1)))]
        plateform[m.start(1):m.end(1), j] = np.array(tilt)

total = 0
for i,line in enumerate(np.flipud(plateform)):
    total += np.count_nonzero(line == 'O') * (i+1)
print(total)