
instr = open('./2018/day12/input.txt', 'r').read().splitlines()
state = instr[0][15:]

rules = dict()
for r in instr[2:]:
    r = r.split()
    rules[r[0]] = r[2]

for _ in range(20):
    newState = ''.join([rules['.'*i + state[:5-i]] for i in range(3,0,-1)]) # extend on the left
    newState += ''.join([rules[state[i-2:i+3]] for i in range(2,len(state)-2)]) # every pot except the ones at the start & end
    newState += ''.join([rules[state[-(5-i):] + '.'*i] for i in range(1,4)]) # extend on the right
    state = newState

print(sum([i-20 for i in range(len(state)) if state[i]=='#']))