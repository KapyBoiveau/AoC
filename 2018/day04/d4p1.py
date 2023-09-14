from collections import Counter
import re

guards = dict()
input = open('./2018/day04/input.txt', 'r').readlines()
input.sort()
for line in input:
    if re.search(r'Guard', line):
        id = int(re.search(r'#(\d+)', line).group()[1:])
    else:
        m, zzz = re.search(r'(\d+)] (\w)', line).groups()
        if zzz == 'w':
            sleep = [x+start for x in range(int(m)-start)]
            guards[id] = sleep if id not in guards else guards[id] + sleep
        else:
            start = int(m)

maxi = 0
for id in guards:
    if len(guards[id]) > maxi:
        maxi = len(guards[id])
        result = id * Counter(guards[id]).most_common(1)[0][0]
print(result)