import numpy as np

bricks = list()
for line in open('./2023/day22/input.txt', 'r').read().split('\n'):
    start, end = [np.array(x.split(','), dtype=int) for x in line.split('~')]
    diff = end - start
    nb = sum(diff)
    diff[np.where(diff != 0)] = 1
    bricks.append([tuple(start + (diff * x)) for x in range(nb + 1)])

def colision(bList, brick):
    flatB = [x for b in bList for x in b]
    for b in brick:
        if b in flatB:
            return True
    return False

bricks.sort(key=lambda b: b[0][2])
for i,brick in enumerate(bricks):

    while(True):
        if brick[0][2] == 1:
            break

        lower = [tuple(x) for x in brick + np.array([0,0,-1])]

        if colision(bricks[:i] + bricks[i+1:], lower):            
            break

        brick = lower

    bricks[i] = brick
    print(brick)
