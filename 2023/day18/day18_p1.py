import numpy as np

turn = {'UR':'F', 'LD':'F', 
        'UL':'7', 'RD':'7', 
        'DR':'L', 'LU':'L', 
        'DL':'J', 'RU':'J'}

oldDir = 'U'
trench = dict()
pos = np.array((0,0))
input = open('./2023/day18/input.txt', 'r').read().split('\n')
dirDic = {'R':np.array((0,1)), 'L':np.array((0,-1)), 'D':np.array((1,0)), 'U':np.array((-1,0))}

for line in input:
    dir, dist, osef = line.split()
    trench[tuple(pos)] = turn[oldDir+dir]
    for i in range(int(dist)-1):
        trench[tuple(pos + dirDic[dir] * (i+1))] = '|' if dir in 'UD' else '-'
    pos += dirDic[dir] * int(dist)
    oldDir = dir

posSet = set(trench.keys())
posList = np.array(list(posSet))
xmin, ymin = np.amin(posList[:,1]), np.amin(posList[:,0])
xmax, ymax = np.amax(posList[:,1]), np.amax(posList[:,0])

nb = len(trench)
for y in range(ymin, ymax+1):
    lf, cross = '.', 0
    for x in range(xmin, xmax+1):    
        if (y,x) not in posSet:
            nb += cross % 2
        else:
            if trench[(y,x)] != '-':
                if lf in ('.','|'):
                    lf = trench[(y,x)]
                elif (lf + trench[(y,x)]) in ('FJ', 'L7'):
                    lf = '|'
                elif lf in ('F','L'): 
                    lf = '.'
                cross += int(lf == '|')

print(nb)