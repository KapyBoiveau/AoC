
resp = {}
instr = []
input = open('./2016/day10/input.txt', 'r').read().splitlines()
for line in input:
    line = line.split()
    if line[0] == 'value':
        bot = line[-2] + line[-1]
        if bot not in resp:
            resp.update({bot : set()})
        values = resp[bot]
        values.add(int(line[1]))
        resp.update({bot : values})
    else:
        instr.append((line[0]+line[1], line[5]+line[6], line[10]+line[11]))

keepGoing = True
while(keepGoing):
    for i in instr:
        bot, lowTo, highTo = i
        if bot not in resp:
            resp.update({bot:set()})
        values = resp[bot]
        if len(values) < 2:
            continue
        low, high = min(values), max(values)
        if lowTo not in resp:
            resp.update({lowTo:set()})
        if highTo not in resp:
            resp.update({highTo:set()})
        valLow, valHigh = resp[lowTo], resp[highTo]
        valLow.add(low)
        resp.update({lowTo : valLow})
        valHigh.add(high)
        resp.update({highTo : valHigh})
    
    keepGoing = any(e not in resp for e in ['output0','output1','output2'])

output0 ,= resp['output0']
output1 ,= resp['output1']
output2 ,= resp['output2']
print(output0*output1*output2)