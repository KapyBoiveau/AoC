import numpy as np
from itertools import combinations as combi

def isInCity(pos):
    return 0 <= pos[0] < city.shape[0] and 0 <= pos[1] < city.shape[1]

file = open('./2024/day08/input.txt', 'r').read()
antennas = list(set(file.replace('\n', '')).difference({'.'}))
city = np.array([list(x) for x in file.split('\n')])
antinodes = set()
for a in antennas:
    pos = np.argwhere(city == a)
    for c in combi(pos, 2):
        for i in range(-city.shape[0], city.shape[0]):
            temp = i * (c[0]-c[1]) + c[0]
            if isInCity(temp):
                antinodes.add(tuple(temp))

print(len(antinodes))