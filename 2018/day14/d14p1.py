
elves, recipes, nb = [0,1], '37', 323081

while True:
    recipes += str(int(recipes[elves[0]]) + int(recipes[elves[1]]))
    elves = [(int(recipes[e])+e+1) % len(recipes) for e in elves]
    if len(recipes) >= nb+10:
        print(recipes[nb:nb+10])
        break