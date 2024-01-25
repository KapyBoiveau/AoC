import itertools as iter
import numpy as np

total = 0
frame = []
for line in open('./2023/day13/input.txt', 'r').readlines():
    if len(line) > 1:
        frame.append(list(line.strip()))
    else:
        done = False
        for p in iter.product(range(len(frame)), range(len(frame[0]))):
            terrain = np.array(frame)
            x = terrain[p[0]][p[1]]
            terrain[p[0]][p[1]] = '.' if x == '#' else '#'

            n = len(terrain)
            for i in range(1,n): # horizontal
                size = i if i < n/2 else n-i
                start = i - size
                if p[0] >= start and p[0] < start+size*2:
                    base = terrain[start:start+size,:]
                    flip = np.flip(terrain[start+size:start+size*2,:], 0)
                    if np.array_equal(base, flip):
                        total += i*100
                        done = True
                        break

            if not done:
                n = len(terrain[0])
                for i in range(1,n): # vertical
                    size = i if i < n/2 else n-i
                    start = i - size
                    if p[1] >= start and p[1] < start+size*2:
                        base = terrain[:,start:start+size]
                        flip = np.flip(terrain[:,start+size:start+size*2], 1)
                        if np.array_equal(base, flip):
                            total += i
                            done = True
                            break

            if done:
                break
        frame = []

print(total)