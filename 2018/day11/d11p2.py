import numpy
import math

sn = 18
def powerlevel(x,y):
    id = x + 10
    pl = (id * y + sn) * id
    return -5 if pl < 100 else int(str(pl)[-3]) - 5

plList = dict()
for x in range(1,301):
    for y in range(1,301):
        plList[(x,y)] = powerlevel(x,y)

def getMaxi():
    maxi = 0
    a = numpy.array((0,0))
    for x in range(1,301):
        for y in range(1,301):
            pl = plList[(x,y)]
            for s in range(1,301-max((x,y))):
                pl += sum([plList[tuple(a+(x2,s)+(x,y))] for x2 in range(s)]) 
                pl += sum([plList[tuple(a+(s,y2)+(x,y))] for y2 in range(s)])
                pl += plList[tuple(a+(s,s)+(x,y))]
                if pl > maxi:
                    maxi = pl
                    result = x,y,s,maxi
                    if maxi == 36: # c'est le max, on sort
                        return result
    return result

x,y,s,maxi = getMaxi()
print('{},{},{},{}'.format(x,y,s,maxi))