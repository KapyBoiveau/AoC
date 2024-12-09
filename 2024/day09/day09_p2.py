
oldDisk = open('./2024/day09/input.txt', 'r').read().strip()
newDisk = [int(x) for x in oldDisk]

id = 0
cs = 0
n = 0 # n th block
while n < len(oldDisk):
    block = int(oldDisk[n])
    if n%2 == 0: # if file
        for _ in range(block):
            newDisk.append(id)
        id += 1

    else: # if empty space
        for _ in range(block):
            lastBlock = int(oldDisk[-1])
            while not lastBlock:
                oldDisk = oldDisk[:-2]
                lastBlock = int(oldDisk[-1])
            if n == len(oldDisk):
                break
            idLastBlock = int(len(oldDisk) / 2)
            newDisk.append(idLastBlock)
            oldDisk = oldDisk[:-1] + str(lastBlock-1)
    n += 1

print(sum(i * x for i, x in enumerate(newDisk)))