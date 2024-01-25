import re

total = 0
wf = dict()
blank = False
input = open('./2023/day19/input.txt', 'r').read().split('\n')
for line in input:
    if len(line) == 0:
        blank = True
        continue

    if not blank:
        name, rules = re.match(r'(\w+)\{(.*)\}',line).groups()
        wf[name] = [rule.split(':') for rule in rules.split(',')]
    else:
        x, m, a, s = (int(x) for x in re.findall(r'(\d+)', line))
        name = 'in'
        while name not in 'AR':
            for rule in wf[name]:
                if len(rule) == 1:
                    name = rule[0]
                    break
                elif eval(rule[0]):
                    name = rule[1]
                    break
        if name == 'A':
            total += x + m + a + s

print(total)
