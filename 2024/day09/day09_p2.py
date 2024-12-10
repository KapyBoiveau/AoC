import numpy as np

oldDisk = open('./2024/day09/input.txt', 'r').read().strip()
nbs = [int(x) for x in oldDisk[::2]]
oldNbs = [int(x) for x in oldDisk[::2]]
free = np.array([int(x) for x in oldDisk[1::2]], dtype=object)
freent = [np.array([0 for _ in range(x)], dtype=object) for x in free]

# print(nbs) # [5, 3, 1]
# print(free) # [4 2]
# print(freent) # [[0, 0, 0, 0], [0, 0]]

l = len(nbs)
for i in range(l):
    tailleBlock, id = nbs[-i-1], l-i-1 # nb sera [1,3,5], val sera [2,1,0]
    x = np.argwhere(free >= tailleBlock) # le spot dans free assez grand
    if len(x): # si trouvé
        free[x[0,0]] -= tailleBlock # on décroit ce spot dans free
        nbs[-i-1] = 0 # on 0 dans nbs pour ce bloc
        y = np.argwhere(freent[x[0,0]] == 0)[0,0] # on trouve le freent correspondant
        freent[x[0,0]][y:y+tailleBlock] = id # on rempli freent

# print(nbs)
# print([list(x) for x in freent])

cs = 0
i = nbs[0]
for j in range(len(nbs)-1):
    cs += sum(n*(i+k) for k, n in enumerate(freent[j]))
    # print([(n,(i+k)) for k, n in enumerate(freent[j])])
    i += len(freent[j])

    cs += sum((j+1)*(i+k) for k in range(nbs[j+1]))
    # print([((j+1),(i+k)) for k in range(nbs[j+1])])
    i += oldNbs[j+1]

print(cs)