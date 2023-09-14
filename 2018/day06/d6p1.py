from collections import Counter

coord = open('./2018/day06/input.txt', 'r').readlines()
coord = [(int(x[0]),int(x[1])) for x in [c.strip().split(', ') for c in coord]]

xMin, xMax, yMin, yMax = 1000, 0, 1000, 0
for x,y in coord:
    if x<xMin:
        xMin = x
    elif x>xMax:
        xMax = x
    if y<yMin:
        yMin = y
    elif y>yMax:
        yMax = y

def getClosest(x,y):
    global areas
    mini = xMax
    for i, pair in enumerate(coord):
        cX, cY = pair
        dist = abs(cX-x) + abs(cY-y)
        if dist < mini:
            mini = dist
            closest = i
        elif dist == mini:
            closest = -1
    return closest

edges = set()
closestPoints = []
for y in range(yMin, yMax+1):
    for x in range(xMin, xMax+1):
        closest = getClosest(x,y)
        closestPoints.append(closest)
        if y in (yMin,yMax) or x in (xMin, xMax):
            edges.add(closest)

for point, combien in Counter(closestPoints).most_common():
    if point not in edges:
        print(combien)
        break