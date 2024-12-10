import numpy as np

oldDisk = open('./2024/day09/input.txt', 'r').read().strip()
nbs = [int(x) for x in oldDisk[::2]]
oldNbs = [int(x) for x in oldDisk[::2]]
free = np.array([int(x) for x in oldDisk[1::2]], dtype=object)
freent = [[0 for _ in range(x)] for x in free]

for i in reversed(range(len(nbs))):
    blockLen, id = nbs[i], i
    x = np.argwhere(free[:id] >= blockLen) # on cherche un spot dans free assez grand, à gauche du block
    if len(x):
        pos = x[0,0]
        free[pos] -= blockLen # on décroit ce spot dans free
        nbs[i] = 0 # on vide ce bloc
        y = freent[pos].index(0) # on trouve le freent correspondant
        freent[pos][y:y+blockLen] = [id] * blockLen # on rempli freent

i, cs = nbs[0], 0
for j in range(len(nbs)-1):
    cs += sum(n*(i+k) for k, n in enumerate(freent[j])) # somme de freent
    i += len(freent[j])

    cs += sum((j+1)*(i+k) for k in range(nbs[j+1])) # somme de ce qu'il reste dans nbs
    i += oldNbs[j+1] # oldNbs car nbs peut être vide

print(cs)