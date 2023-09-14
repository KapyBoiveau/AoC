import numpy
import math

sn = 7989
def powerlevel(x,y):
    id = x + 10
    pl = (id * y + sn) * id
    return -5 if pl < 100 else int(str(pl)[-3]) - 5

plList = dict()
a = numpy.array((0,0))
for x in range(1,301):
    for y in range(1,301):
        plList[(x,y)] = powerlevel(x,y)

def getMaxi():
    maxi = 0
    for x in range(1,299):
        for y in range(1,299):
            pl = sum([plList[tuple(a+(x2,y2)+(x,y))] for x2 in range(3) for y2 in range(3)])
            if pl > maxi:
                maxi = pl
                result = x,y
    return result

print(getMaxi())