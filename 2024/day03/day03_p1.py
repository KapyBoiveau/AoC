import re

memory = open('./2024/day03/input.txt', 'r').read()
tuples = re.findall(r'mul\((\d+),(\d+)\)', memory)

print(sum(int(x) * int(y) for x, y in tuples))