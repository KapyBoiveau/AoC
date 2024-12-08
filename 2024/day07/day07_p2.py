import re
from itertools import product

ADD = lambda x, y: x + y
MUL = lambda x, y: x * y
CONCAT = lambda x, y: int(str(x) + str(y))
ops = [ADD, MUL, CONCAT]
  
tot = 0
for equ in open('./2024/day07/input.txt', 'r').read().split('\n'):
    nbs = list(map(int, re.findall(r'\d+', equ)))
    goal, vals = nbs[0], nbs[2:]
    for prod in product(ops, repeat=len(nbs)-2):
        calc = nbs[1]
        for i, op in enumerate(prod):
            calc = op(calc, vals[i])
        if calc == goal:
            tot += goal
            break

print(tot)