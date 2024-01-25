
x = []
for i,line in enumerate(open('./2023/day06/input.txt', 'r').readlines()):
    x.append([int(x) for x in line.strip().split()[1:]])
times, distances = x[0], x[1]

total = 1
for i,t in enumerate(times):
    nb = 0
    for r in range(t+1):
        d = r * (t-r)
        if d > distances[i]:
            nb += 1
    total *= nb

print(total)