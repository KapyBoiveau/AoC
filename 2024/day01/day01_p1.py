import re

input = open('./2024/day01/input.txt', 'r').read()
numbers = list(map(int, re.findall(r'\d+', input)))
left = sorted(numbers[::2])
right = sorted(numbers[1::2])

print(sum([abs(left[x] - right[x]) for x in range(1000)]))