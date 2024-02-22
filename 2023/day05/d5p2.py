
mapping = dict()
input = open('./2023/day05/input.txt', 'r').readlines()
seeds = input[0].split()[1:]
seeds = [(int(seeds[i]), int(seeds[i]) + int(seeds[i+1]) - 1) for i in range(len(seeds)) if i%2 == 0]
for line in input[2:]:
    if len(line) > 1:
        if line[0].isdigit():
            mapping[mode].append([int(x) for x in line.split()])
        else:
            mode = line.split('-')[0]
            mapping[mode] = []

def intersec(r1, r2):
    if not(r1[1] < r2[0] or r2[1] < r1[0]): # not no overlap
        overlap = (max((r1[0], r2[0])), min((r1[1], r2[1])))
        remain = set()
        if r1[0] < r2[0]:
            remain.add((r1[0], r2[0] - 1))
        if r1[1] > r2[1]:
            remain.add((r2[1] + 1, r1[1]))
        return overlap, remain
    else:
        return None, {r1} # no overlap, and remain = range1

minis = []
for seed in seeds: # pour chaque range de seed
    seed = {seed}
    for mode in mapping.keys(): # pour chaque mode
        nextSeeds = set()
        for m in mapping[mode]: 
            rest = list()
            
            for s in seed:
                overlap, s = intersec(s , (m[1], m[1] + m[2] - 1)) # on trouve l'intersection des ranges
                if overlap:
                    dest = (m[0] - m[1] + overlap[0], m[0] - m[1] + overlap[1]) # la destination correspondant à l'overlap
                    nextSeeds.add(dest) # on met ça dans une liste temporaire
                for subR in s:
                    rest.append(subR)
            seed = set(rest)

        # on rajoute dans la liste ce qui reste
        seed = nextSeeds.union(seed) # la liste de nouvelles ranges devient la nouvelle seed pour les mods suivants
    
    minis.append(sorted(list(seed))[0][0])

print(min(minis))