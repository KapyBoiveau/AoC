import re

input = open('./2024/day01/input.txt', 'r').read()
numbers = list(map(int, re.findall(r'\d+', input)))
left = numbers[::2]
right = numbers[1::2]

print(sum([x * right.count(x) for x in left]))