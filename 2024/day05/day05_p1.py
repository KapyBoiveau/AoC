
lines = open('./2024/day05/input.txt', 'r').read().split('\n')

total = 0
rules = dict()
firstPart = True
for line in lines:
    if not line:
        firstPart = False

    elif firstPart:
        pages = line.split('|')
        if pages[1] not in rules:
            rules[pages[1]] = []
        rules[pages[1]].append(pages[0])
        
    else:
        ok = True
        update = line.split(',')
        for i, page in enumerate(update):
            if page in rules:
                if any(x in update[i+1:] for x in rules[page]):
                    ok = False
                    break
        if ok:
            total += int(update[int(len(update)/2)])

print(total)