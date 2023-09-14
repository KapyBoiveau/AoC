from collections import Counter

cs = (0,0)
for id in open('./2018/day02/input.txt', 'r').readlines():
    duplicates = set([j for i,j in Counter(id).items() if j in (2,3)])
    cs = (cs[0] + int(2 in duplicates), cs[1] + int(3 in duplicates))

print(cs[0] * cs[1])