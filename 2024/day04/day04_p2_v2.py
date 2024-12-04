
lines = open('./2024/day04/input.txt', 'r').read().split('\n')

def isCross(x, y):
    if 0 < x < len(lines)-1 and 0 < y < len(lines[0])-1:
        nw_se = lines[x-1][y-1] + lines[x][y] + lines[x+1][y+1]
        ne_sw = lines[x-1][y+1] + lines[x][y] + lines[x+1][y-1]
        if nw_se in ['MAS', 'SAM'] and ne_sw in ['MAS', 'SAM']:
            return True
    return False

nb = 0
for x in range(len(lines)):
    for y in range(len(lines[x])):
        nb += lines[x][y] == 'A' and isCross(x, y)

print(nb)