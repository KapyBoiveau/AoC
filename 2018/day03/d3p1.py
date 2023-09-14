import re

overlaps, cuts = set(), set()
for claim in open('./2018/day03/input.txt', 'r').readlines():
    left, top, width, height = [int(x) for x in re.search(r'(\d+),(\d+): (\d+)x(\d+)', claim).groups()]
    cut = set([(x+left,y+top) for x in range(width) for y in range(height)])
    overlaps.update(cuts.intersection(cut))
    cuts.update(cut)
print(len(overlaps))