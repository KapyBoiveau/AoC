import regex as re




numbers, gears = [], set()
for y,line in enumerate(open('./2023/day03/input.txt', 'r').readlines()):
    for m in re.finditer(r'(\d+)+|([^\d\.])', line.strip()):
        if m.group().isdecimal(): # add a tuple containing the number with the positions of the digits
            numbers.append((int(m.group()), {(int(x),y) for x in range(m.span()[0], m.span()[1])}))
        elif m.group() == '*': # add the position of the gear and every adjacent position
            gears.add(tuple((m.span()[0]+x, y+y2) for x in range(-1,2) for y2 in range(-1,2))) 

total = 0
for g in gears:
    i, subTotal = 0, 1
    for n in numbers:
        if set(g) & n[1]:
            i += 1
            subTotal *= n[0]
    if i == 2:
        total += subTotal
print(total)