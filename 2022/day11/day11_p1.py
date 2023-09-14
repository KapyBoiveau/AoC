
monkeyItems = []
monkeyOperations = []
monkeyThrows = []
monkeyInspects = []


with open('./Kapy/day11/input.txt', 'r') as f:
    for i, l in enumerate(f.readlines()):
        line = l.strip().split(' ')
        if i % 7 == 0: # Monkey number
            monkeyID = int(line[1][:-1])
            monkeyInspects.append(0)
        if (i-1) % 7 == 0: # Starting items
            startingItems = [int(x[:2]) for x in line[2:]]
            monkeyItems.append(startingItems)
        if (i-2) % 7 == 0: # Operation
            monkeyOperations.append([line[4], line[5]])
        if (i-3) % 7 == 0: # Divisibility
            monkeyThrows.append([int(line[3])])
            # if divisible by n then monkey 1 else monkey 2 
            # will look like : [n, 1, 2]
        if (i-4) % 7 == 0 or (i-5) % 7 == 0: # if True or if False
            monkeyThrows[monkeyID].append(int(line[5]))

def operation(worryLevel, op, nb):
    nb = worryLevel if nb == 'old' else int(nb)
    return worryLevel * nb if op == '*' else worryLevel + nb

for _ in range(0, 20):
    for monkeyID in range(0, len(monkeyItems)):
        monkeyInspects[monkeyID] += len(monkeyItems[monkeyID])
        for worryLevel in monkeyItems[monkeyID][::-1]: # reverse order, so we can pop()
            ops = monkeyOperations[monkeyID]
            worryLevel = operation(worryLevel, ops[0], ops[1])
            worryLevel = int(worryLevel / 3)
            throws = monkeyThrows[monkeyID]
            newID = throws[1] if worryLevel % throws[0] == 0 else throws[2]
            monkeyItems[newID].append(worryLevel)
            monkeyItems[monkeyID].pop()

monkeyInspects.sort(reverse=True)
print(monkeyInspects[0]*monkeyInspects[1])