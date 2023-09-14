
coord = [(int(x[0]),int(x[1])) for x in [c.strip().split(', ') for c in open('./2018/day06/input.txt', 'r').readlines()]]
xMin, xMax, yMin, yMax = min([x for x,_ in coord]), max([x for x,_ in coord]), min([y for _,y in coord]), max([y for _,y in coord])
print(len([0 for x in range(xMin, xMax+1) for y in range(yMin, yMax+1) if sum([abs(y2-y) + abs(x2-x) for x2,y2 in coord]) < 10000]))