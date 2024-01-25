import re


total = 0
for line in open('./2023/day04/input.txt', 'r').readlines():
    win, you = line.strip().split(':')[1].split('|')
    win = set(re.findall(r'\d+', win))
    you = set(re.findall(r'\d+', you))
    if you & win:
        total += 2 ** (len(you & win)-1)

print(total)