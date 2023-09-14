
gantt = dict()
parents, enfants = set(), set()
for instr in [l.split() for l in open('./2018/day07/input.txt', 'r').read().splitlines()]:
    p, e = instr[1], instr[7] # parent, enfant
    if p not in gantt:
        gantt[p] = []
    gantt[p].append(e)
    parents.add(p), enfants.add(e)
todo = parents - enfants # get the starting element
nbWorkers = 5
workJob = ['' for _ in range(nbWorkers)]
workTimer = [0 for _ in range(nbWorkers)]

def lowestAvailable(todo):
    todoList = list(todo)
    todoList.sort()
    for x in todoList: # test each element of the sorted set
        if not [True for y in parents if x in gantt[y] and y not in result]:
            return x
    return '?'

sec = 0
result = ''
fin = len(parents | enfants)
while len(result) < fin:    
    while 0 in workTimer and todo:
        x = lowestAvailable(todo)
        if x != '?':
            i = workTimer.index(0)
            workTimer[i] = ord(x) - ord('A') + 1 + 60
            workJob[i] = x
            todo.remove(x)
        else:
            break

    while 1 in workTimer:
        i = workTimer.index(1)
        x = workJob[i]
        workJob[i] = ''
        workTimer[i] = 0
        result += x
        if x in gantt:
            todo.update(gantt[x])

    sec += 1
    workTimer = [w-1 if w > 0 else 0 for w in workTimer]

print(result, sec)