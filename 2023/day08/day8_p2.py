import re

input = open('./2023/day08/input.txt', 'r').readlines()
leftright = input[0].strip()

class MyLeftRights:
  def __iter__(self):
    self.i = 0
    self.a = leftright[self.i]
    return self

  def __next__(self):
    x = self.a
    self.i = (self.i + 1) % len(leftright)
    self.a = leftright[self.i]
    return x

myLR = MyLeftRights()
LRiter = iter(myLR)

network = dict()
for line in input[2:]:
    x = re.search(r'(.{3}) = \((.{3}), (.{3})\)', line).groups()
    network[x[0]] = (x[1], x[2])

n = 0
currents = [elem for elem in network.keys() if elem.endswith('A')]
tricks = [0 for _ in currents]
while(True):
  n += 1
  LRindex = 0 if next(LRiter) == 'L' else 1
  for i,c in enumerate(currents):
    currents[i] = network[c][LRindex]
    if currents[i].endswith('Z'):
      if tricks[i] == 0:
        tricks[i] = n
  if all(t > 0 for t in tricks):
    break

def primeFactors(n):
  f = []
  while n % 2 == 0:
    n /= 2
    f.append(2)
  for i in range(3, n+1, 2):
    while n % i == 0:
      n /= i
      f.append(i)
  return f

factors = set()
for t in tricks:
  factors = factors.union(set(primeFactors(t)))

x = 1
for f in factors:
  x *= f
print(x)