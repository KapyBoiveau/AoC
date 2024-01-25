import numpy as np

total = 0
frame = []
for line in open('./2023/day13/input.txt', 'r').readlines():
    if len(line) > 1:
        frame.append(list(line.strip()))
    else:
        terrain = np.array(frame)
        done = False
        frame = []

        n = len(terrain)
        for i in range(1,n): # horizontal
            size = i if i < n/2 else n-i # taille du tableau tronqué
            start = i - size 
            base = terrain[start:start+size,:] # tableau tronqué
            flip = np.flip(terrain[start+size:start+size*2,:], 0) # son mirroir maléfique
            if np.array_equal(base, flip):
                total += i*100
                done = True
                break

        if not done:
            n = len(terrain[0])
            for i in range(1,n): # vertical
                size = i if i < n/2 else n-i
                start = i - size
                base = terrain[:,start:start+size]
                flip = np.flip(terrain[:,start+size:start+size*2], 1)
                if np.array_equal(base, flip):
                    total += i
                    break

print(total)