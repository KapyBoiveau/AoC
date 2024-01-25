
def getExtra(line):
    if len(set(line)) == 1: # si tous pareil
        return line[0]
    newLine = [line[i] - line[i-1] for i in range(1, len(line))]
    return line[-1] + getExtra(newLine)

extra = []
for line in open('./2023/day09/input.txt', 'r').readlines():
    line = [int(x) for x in line.strip().split()]
    extra.append(getExtra(line))

print(sum(extra))