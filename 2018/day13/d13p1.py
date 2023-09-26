import world

carList = list()
t = world.tracks()
for y,line in enumerate(t.space):
    for x,tile in enumerate(line):
        if tile in ('>','v','^','<'):
            carList.append(world.car(x,y,tile))

crash = False
while not crash:
    for i,car in enumerate(carList):
        car.move(t)
        if tuple(car.pos) in [tuple(c.pos) for c in carList if c != car]:
            print('{},{}'.format(car.pos[0], car.pos[1]))
            crash = True
            break