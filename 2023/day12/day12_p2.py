import re

def getRgx():
    for i,x in enumerate(patern):
        if i == 0:
            rgx = '\.*#{' + str(x) + '}'
        else:
            rgx += '\.+#{' + str(x) + '}'
    return rgx + '\.*'

def isValid(s):
    if not '?' in s:
        match = re.search(rgx, s)
        if match:
            start, end = match.span()
            return end - start == len(s)
        else:
            return False

    c, i = 0, 0 # c = compteur des springs collés, i = numéro du groupe de springs
    for x in s:
        if x == '#':
            c += 1
            if c > patern[i]:
                return False
        elif x == '.':
            if c == patern[i]:
                c = 0
                i += 1
                if i == len(patern):
                    return True
            elif c != 0:
                return False
        else:
            return True

def build(argmt):
    if not isValid(argmt):
        return 0
    
    pos = argmt.find('?')
    if pos >= 0:
        return build(argmt[:pos] + '#' + argmt[pos+1:]) + build(argmt[:pos] + '.' + argmt[pos+1:])
    else:
        return 1

total = 0
for i,line in enumerate(open('./2023/day12/input.txt', 'r').readlines()):
    print(i)
    springs, patern = line.strip().split()
    springs = (springs + '?') * 5
    springs = springs[:-1]
    patern = tuple([int(x) for x in patern.split(',')] * 5)
    rgx = getRgx()
    total += build(springs)
    #print(springs, patern, b)

print(total)