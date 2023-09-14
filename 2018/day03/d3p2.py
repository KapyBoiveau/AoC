import re

overlaps, cuts = set(), set()
input = open('./2018/day03/input.txt', 'r').readlines()
for claim in input:
    left, top, width, height = [int(x) for x in re.search(r'(\d+),(\d+): (\d+)x(\d+)', claim).groups()]
    cut = set([(x+left,y+top) for x in range(width) for y in range(height)])
    overlaps.update(cuts.intersection(cut))
    cuts.update(cut)

for i,claim in enumerate(input):
    left, top, width, height = [int(x) for x in re.search(r'(\d+),(\d+): (\d+)x(\d+)', claim).groups()]
    cut = set([(x+left,y+top) for x in range(width) for y in range(height)])
    if not overlaps.intersection(cut):
        print(i+1)
        break