import itertools as iter
import difflib

input = [x.strip() for x in open('./2018/day02/input.txt', 'r').readlines()]
for pair in iter.combinations(input, 2):
    x,y = [],[]
    for i,s in enumerate(difflib.ndiff(pair[0], pair[1])):
        if s[0]=='-':
            x.append(i)
            goal = pair[0][:i] + pair[0][i+1:]
        elif s[0]=='+':
            y.append(i)
    if len(x) == 1 and len(y) == 1 and y[0] == x[0] + 1:
        print(goal)
        break