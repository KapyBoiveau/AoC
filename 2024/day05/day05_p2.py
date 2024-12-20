
lines = open('./2024/day05/input.txt', 'r').read().split('\n')

def swapThis(i, page): 
    # return the first rule that doesn't work
    if page in rules:
        for x in rules[page]:
            if x in update[i+1:]:
                return (page, x)
    return False

total = 0
rules = dict()
firstPart = True
for line in lines:
    if not line:
        firstPart = False

    elif firstPart: # same as part 1
        pages = list(map(int, line.split('|')))
        if pages[1] not in rules:
            rules[pages[1]] = []
        rules[pages[1]].append(pages[0])

    else:
        update = list(map(int, line.split(',')))
        ok = False
        modif = False
        while not ok:

            ok = True
            for i, page in enumerate(update):

                toSwap = swapThis(i, page)
                if toSwap: # swap until all good
                    update[update.index(toSwap[1])] = toSwap[0]
                    update[i] = toSwap[1]
                    modif = True
                    ok = False
                    break

        if modif:
            total += update[int(len(update)/2)]

print(total)