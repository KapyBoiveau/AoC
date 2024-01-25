import re

total = 0
for line in open('./2023/day01/input.txt', 'r').readlines():
    nb = re.findall(r'\d', line)
    total += int(nb[0]+nb[-1]) if len(nb) else 0
print(total)