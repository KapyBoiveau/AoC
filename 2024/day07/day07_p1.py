import re
from itertools import product

tot = 0
for equ in open('./2024/day07/input.txt', 'r').read().split('\n'):
    nbs = list(map(int, re.findall(r'\d+', equ)))
    goal, vals = nbs[0], nbs[2:]
    for prod in product('*+', repeat=len(nbs)-2):
        calc = nbs[1]
        for i, p in enumerate(prod):
            if p == '*':
                calc = calc * vals[i]
            else:
                calc = calc + vals[i]

                
        if calc == goal:
            tot += goal
            break

print(tot)