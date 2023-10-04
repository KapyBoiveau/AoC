
elves, recipes, nb = [0,1], '37', '323081'

while True:
    recipes += str(int(recipes[elves[0]]) + int(recipes[elves[1]]))
    elves = [(int(recipes[e])+e+1) % len(recipes) for e in elves]
    if nb in recipes[-7:]:
        print(recipes.index(nb))
        break