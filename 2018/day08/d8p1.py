
def getMetadata(subtree):
    idx = 0
    subData = 0
    if len(subtree) > 0:
        idx = 2
        nbChilds, nbData = subtree[0], subtree[1]
        for _ in range(nbChilds):
            data, i = getMetadata(subtree[idx:])
            subData += data
            idx += i
        idx += nbData
        subData += sum(subtree[idx:idx+nbData])
    return subData, idx
    
tree = [int(x) for x in open('./2018/day08/input.txt', 'r').read().split()]
print(getMetadata(tree))