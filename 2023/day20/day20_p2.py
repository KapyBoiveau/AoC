import queue as q

class modules:

    def __init__(self, n):
        self.name = n
        self.type = ''
        self.dest = []
        self.state = False
        self.lastInputs = dict()

    def setType(self, t):
        self.type = t

    def setDest(self, d):
        self.dest = d

    def setLastInputs(self, recep):
        if self.type == '&':
            self.lastInputs[recep] = False

    def receive(self, pulseIn=False, input=''):
        global low, high
        if self.type == '%': # Flip-flop
            if not pulseIn:
                self.state = not self.state
                pulseOut = self.state

        elif self.type == '&': # Conjunction 
            self.lastInputs[input] = pulseIn
            pulseOut = not(all(self.lastInputs.values()))

        else:
            pulseOut = pulseIn

        if not (self.type == '%' and pulseIn):
            for d in self.dest:
                pulses.put((mDict[d], pulseOut, self.name))
                if pulseOut:
                    high += 1
                else:
                    low += 1

    def getName(self):
        return self.name
    
    def __str__(self):
        return self.type + self.name + ' -> ' + str(self.dest)

b = 'button'
mDict = {b:modules(b)}
mDict[b].setDest(['broadcaster'])
for line in open('./2023/day20/input.txt', 'r').read().split('\n'):
    t = ''
    n, d = line.split(' -> ')
    if n[0] in '%&':
        t = n[0]
        n = n[1:]
    dest = d.split(', ')
    for x in [n] + dest:
        if x not in mDict:
            mDict[x] = modules(x)
    if t:
        mDict[n].setType(t)
    mDict[n].setDest(dest)

for m in mDict:
    for d in mDict[m].dest:
        mDict[d].setLastInputs(m)

low, high = 0, 0
pulses = q.Queue()
for i in range(100):
    mDict['button'].receive()
    while not pulses.empty():
        m, p, n = pulses.get()
        m.receive(p, n)

    x = ''
    for c_mod in ('qq', 'bx', 'bc', 'gj'): # for c_mod in ('jc', 'vm', 'qq', 'fj'):
        x += ''.join(['1' if val else '0' for val in mDict[c_mod].lastInputs.values()])
    print(i, x)

#print(low * high)