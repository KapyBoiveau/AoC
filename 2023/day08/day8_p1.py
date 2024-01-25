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
    x = re.search(r'(\w{3}) = \((\w{3}), (\w{3})\)', line).groups()
    network[x[0]] = (x[1], x[2])

n = 0
current = 'AAA'
while(True):
    n += 1
    LRindex = 0 if next(LRiter) == 'L' else 1
    current = network[current][LRindex]
    if current == 'ZZZ':
       break

print(n)