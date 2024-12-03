import re

memory = open('./2024/day03/input.txt', 'r').read()
tuples = re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", memory)

total = 0
mult = True
for x, y, do, dont in tuples:
    if do or dont:
        mult = bool(do)
    elif mult:
        total += int(x) * int(y)

print(total)