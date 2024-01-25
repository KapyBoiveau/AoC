
mapping = dict()
input = open('./2023/day05/input.txt', 'r').readlines()
seeds = input[0].split()[1:]
seeds = [[(int(seeds[i]), int(seeds[i])+int(seeds[i+1]))] for i in range(len(seeds)) if i%2 == 0]
for line in input[2:]:
    if len(line) > 1:
        if line[0].isdigit():
            mapping[mode].append([int(x) for x in line.split()])
        else:
            mode = line.split('-')[0]
            mapping[mode] = []

def intersec(r1, r2):
    if not(r1[1] < r2[0] or r2[1] < r1[0]): # not no overlap
        return (max((r1[0], r2[0])), min((r1[1], r2[1])))

mini = 9999999999
modes = list(mapping.keys())
for s in seeds: # pour chaque range de seed
    for mode in modes: # pour chaque mode
        sTemps = list()
        for subS in s: # pour chaque bloc de range, si jamais c'est split
            for m in mapping[mode]: 
                overlap = intersec(subS , (m[1], m[1] + m[2])) # on trouve l'intersection des ranges
                if overlap:
                    sTemps.append(destination(overlap)) # on met l'overlap dans une liste temporaire
                    subS -= overlap # on enlève cet overlap et on continue avec les autres ranges du mode
            if subS:
                sTemps.append(subS) # on rajoute dans la liste ce qu'il reste
        s = sTemps # la liste de nouvelles ranges devient la nouvelle "seed"
    if min(s) < mini:
        mini = min(s)
print(mini)