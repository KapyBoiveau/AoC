import world as w

carList = list()
t = w.tracks()
for y,line in enumerate(t.space):
    for x,tile in enumerate(line):
        if tile in ('>','v','^','<'):
            carList.append(w.car(x,y,tile))

finish = False
while not finish:
    carList.sort(key=lambda car: (car.pos[1], car.pos[0]))
    for i,car in enumerate(carList):
        if not car.crashed:
            car.move(t)
            if tuple(car.pos) in [tuple(c.pos) for c in carList if c != car]:
                crashPos = tuple(car.pos)
                for c in carList:
                    if tuple(c.pos) == crashPos:
                        c.crash()

    remain = [c.pos for c in carList if not c.crashed]
    if len(remain) == 1:
        print('{},{}'.format(remain[0][0], remain[0][1]))
        finish = True
        break