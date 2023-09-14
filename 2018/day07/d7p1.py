
gantt = dict()
parents, enfants = set(), set()
for instr in [l.split() for l in open('./2018/day07/input.txt', 'r').read().splitlines()]:
    p, e = instr[1], instr[7] # parent, enfant
    if p not in gantt:
        gantt[p] = []
    gantt[p].append(e)
    parents.add(p), enfants.add(e)
todo = parents - enfants # get the starting element

def lowestAvailable(todo):
    todoList = list(todo)
    todoList.sort()
    for x in todoList: # test each element of the sorted set
        if not [True for y in parents if x in gantt[y] and y not in result]:
            return x

result = ''
while todo:
    x = lowestAvailable(todo)
    todo.remove(x)
    result += x
    if x in gantt:
        todo.update(gantt[x])
print(result)