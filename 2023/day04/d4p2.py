import re

input = open('./2023/day04/input.txt', 'r').readlines()
cards = [1 for _ in range(len(input))]
for i,line in enumerate(input):
    win, you = line.strip().split(':')[1].split('|')
    win = set(re.findall(r'\d+', win))
    you = set(re.findall(r'\d+', you))
    correct = len(you & win)
    if correct:
        for j in range(len(cards)):
            if j > i and j <= i + correct:
                cards[j] += cards[i]

print(sum(cards))