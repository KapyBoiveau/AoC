
used = dict()
for line in open('./2016/day22/input.txt', 'r').readlines():
    info = line.split()
    pos = tuple([int(x[1:]) for x in info[0].split('-')[1:]])
    used[pos] = int(info[2][:-1])
    if info[2][:-1] == '0':
        empty = pos
    goal = (36,0) # (2,0) for test

def getAround(pos, goal, emptySet):
    p1 = (pos[0], pos[1]+1)
    p2 = (pos[0], pos[1]-1)
    p3 = (pos[0]+1, pos[1])
    p4 = (pos[0]-1, pos[1])
    return [x for x in [p1, p2, p3, p4]
            if x[0]>=0 and x[1]>=0 and x[0]<=36 and x[1]<=27 # x[0]<=2 and x[1]<=2
            and x not in emptySet and x != goal
            and used[x]<400]

def d22(goal, empty):
    n = 0
    newEmptySet = set()
    emptySet = {empty}
    while True:
        n += 1
        for pos in emptySet:
            dispoSet = set(getAround(pos, goal, emptySet))
            if (goal[0]-1, goal[1]) in dispoSet:
                n += 1
                empty = goal
                emptySet = {empty}
                newEmptySet = set()
                goal = (goal[0]-1, goal[1])
                if goal == (0,0):
                    return n
                break
            else:
                newEmptySet = newEmptySet.union(dispoSet)
        emptySet = emptySet.union(newEmptySet)
        newEmptySet = set()

print(d22(goal, empty))