import numpy as np

input = open('./2023/day18/input.txt', 'r').read().split('\n')
pos = np.array((0,0))
posSet = set()
oldDir = 'U'

dirDic = {'R':np.array((0,1)), 
          'D':np.array((1,0)), 
          'L':np.array((0,-1)), 
          'U':np.array((-1,0))}

def removeDoublons():
    xSet, result = set(), list()
    for e in edges:
        if e[1] in xSet:
            d = [t for t in edges if t[1] == e[1]][0]
            result.remove(d)
        else:
            xSet.add(e[1])
            result.append(e)
    return result

for line in input:
    a, b, instr = line.split()
    dir = 'RDLU'[int(instr[-2])]
    dist = int('0x'+instr[2:-2], 16)
    posSet.add(tuple(pos))
    pos += dirDic[dir] * int(dist)
    oldDir = dir

nb = 0
edges = list()
posList = np.array(sorted(posSet))
prevY, prevLarg = posList[0][1], 0
for p in posList:
    if len(edges) % 2 == 0:
        edges.sort(key = lambda x: x[1])
        edges = removeDoublons()
        larg = np.float64()

        for i in range(len(edges)):
            if i % 2 == 0:
                larg += edges[i+1][1] - edges[i][1] + 1

        if larg - prevLarg > 0:
            nb += larg - prevLarg

        nb += (p[0] - prevY) * larg
        prevLarg, prevY = larg, p[0]

    edges.append(tuple(p))

print(int(nb))