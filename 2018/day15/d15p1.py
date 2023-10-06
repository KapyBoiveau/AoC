import numpy as np

class unit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 300
        self.race = map[y][x]

    def inRange(self):
        pos = np.array([self.x, self.y])
        return set(tuple(pos+dir) for dir in [(0,-1),(-1,0),(1,0),(0,1)] if map[tuple(pos+dir)[::-1]] == '.')

    def victime(self):
        self.hp -= 3

    def moveTo(self, pos):
        self.x = self.x
        self.y = self.y

map = list()
for line in open('./2018/day15/test.txt', 'r').readlines():
    map.append(list(line.strip()))

map = np.array(map)
unitList = list()
unitPos = np.where(np.logical_or(map == 'G', map == 'E'))
for i in range(len(unitPos[0])): 
    unitList.append(unit(unitPos[1][i], unitPos[0][i]))

def distance(pos1, pos2):
    return 0

def getClosest(range, u):
    minDist = 10000
    for r in range:
        dist = distance(r, (u.x, u.y))
        if dist < minDist:
            minDist = dist
            minPos = [r]
        elif dist == minDist:
            minPos.append(r)
    minPos.sort(key=lambda u: (u.y, u.x))
    return minPos[0]

def getUnit(pos):
    for u in unitList:
        if (u.x, u.y) == pos:
            return u

# while True:
unitList.sort(key=lambda u: (u.y, u.x))
for i in range(len(unitList)): # for each unit
    u = unitList[i]
    rangeSet = set()
    for u2 in unitList[:i]+unitList[i+1:]:
        rangeSet = rangeSet.union(u2.inRange())
    posVictime = getClosest(rangeSet, u)
    if distance((u.x, u.y), posVictime) == 1:
        getUnit(posVictime).victime()
    else:
        u.moveTo(posVictime)