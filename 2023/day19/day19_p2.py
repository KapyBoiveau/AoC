import numpy as np
import re

def intersec(a, b):
    c = dict()
    for k in a:
        if k in b:
            mini, maxi = max(a[k][0], b[k][0]), min(a[k][1], b[k][1])
            if mini <= maxi:
                c[k] = (mini, maxi)
        else:
            c[k] = a[k]
    
    for k in b:
        if k not in c:
            c[k] = b[k]
    
    return c


total = 0
wf = dict()
blank = False
input = open('./2023/day19/input.txt', 'r').read().split('\n')
for line in input:
    if len(line) == 0:
        break

    prev = dict()
    name, rules = re.match(r'(\w+)\{(.*)\}',line).groups()
    split = rules.split(',')
    for i, rule in enumerate(split):
        t = rule.split(':')
        d = dict()

        if i > 0:
            prev = intersec(prev, {cond[0]:notFourch})

        if i < len(split) - 1:
            n = t[1]

            cond = re.match(r'(\w)([<>])(\d+)', t[0]).groups()
            if cond[1] == '<':
                fourch = (1, int(cond[2])-1)
                notFourch = (int(cond[2]), 4000)
            else:
                fourch = (int(cond[2])+1, 4000)
                notFourch = (1, int(cond[2]))
            d = {cond[0]:fourch}
            
        else:
            n = t[0]
        
        if i == 0:
            redirects = np.array((n,d))
        else:
            redirects = np.append(redirects, (n, intersec(d, prev)))

    wf[name] = redirects.reshape(int(len(redirects)/2), 2)


xmas = 'xmas'
def parkour(name, parentRules):
    p = np.float64()
    
    for branch in wf[name]:
        bName, bRules = branch
        
        if bName == 'R':
            continue
        
        fourch = intersec(parentRules, bRules)
        if bName == 'A':
            x = np.float64(1)
            for n in xmas:
                if n in fourch:
                    x *= fourch[n][1] - fourch[n][0] + 1
                else:
                    x *= 4000
            p += x
        else:
            p += parkour(bName, fourch)
    
    return p


print(int(parkour('in', dict())))