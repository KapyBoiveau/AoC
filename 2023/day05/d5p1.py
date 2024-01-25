
mapping = dict()
input = open('./2023/day05/input.txt', 'r').readlines()
seeds = [int(x) for x in input[0].split()[1:]]
for line in input[2:]:
    if len(line) > 1:
        if line[0].isdigit():
            mapping[mode].append([int(x) for x in line.split()])
        else:
            mode = line.split('-')[0]
            mapping[mode] = []

mini = 9999999999
modes = list(mapping.keys())
for s in seeds:
    for mode in modes:
        for m in mapping[mode]:
            if s in range(m[1], m[1] + m[2]):
                s = m[0] + s - m[1]
                break
    if s < mini:
        mini = s
print(mini)