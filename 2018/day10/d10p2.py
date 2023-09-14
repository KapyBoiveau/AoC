import numpy as np
import re

posList, velList = list(), list()
input = open('./2018/day10/input.txt', 'r').read().splitlines()
for line in input:
    posX, posY, velX, velY = re.search(r'<((?: |-)*\d+),((?: |-)*\d+)>.*<((?: |-)*\d+),((?: |-)*\d+)>', line).groups()
    posList.append(np.array((int(posX),int(posY))))
    velList.append(np.array((int(velX), int(velY))))

nb = 0
while(True):
    posXmin, posXmax = 100000, -100000
    posYmin, posYmax = 100000, -100000

    for i, pos in enumerate(posList):
        posList[i] = pos + velList[i]
        if posList[i][1] < posYmin:
            posYmin = posList[i][1]
        if posList[i][1] > posYmax:
            posYmax = posList[i][1]
        if posList[i][0] < posXmin:
            posXmin = posList[i][0]
        if posList[i][0] > posXmax:
            posXmax = posList[i][0]
    
    nb += 1
    if posYmax - posYmin < 10:
        break

print(nb)