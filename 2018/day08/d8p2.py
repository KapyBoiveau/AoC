
def getMetadata(subtree):
    idx = 0
    if len(subtree) > 0:
        idx = 2
        dataList = []
        nbChilds, nbData = subtree[0], subtree[1]
        if nbChilds:
            for _ in range(nbChilds):
                data, i = getMetadata(subtree[idx:])
                dataList.append(data)
                idx += i
            refs = subtree[idx:idx+nbData]
            subData = sum([0 if x > len(dataList) else dataList[x-1] for x in refs])
        else:
            subData = sum(subtree[idx:idx+nbData])
        idx += nbData
    return subData, idx

tree = [int(x) for x in open('./2018/day08/input.txt', 'r').read().split()]
print(getMetadata(tree))