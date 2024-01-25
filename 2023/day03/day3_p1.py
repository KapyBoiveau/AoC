import regex as re

def around(posX, posY):
    return set((posX+x, posY+y) for x in range(-1,2) for y in range(-1,2))

numbers, symbols = [], set()
for y,line in enumerate(open('./2023/day03/input.txt', 'r').readlines()):
    for m in re.finditer(r'(\d+)+|([^\d\.])', line.strip()):
        startPos, endPos = m.span()
        if m.group().isdecimal(): # add a tuple containing the number with the positions of the digits
            nb = int(m.group())
            digitsPos = set((int(x),y) for x in range(startPos, endPos))
            numbers.append((nb, digitsPos))
        else: # add the position of the symbol and every adjacent position
            symbols = symbols.union(around(startPos, y)) 

total = [nb[0] for nb in numbers if nb[1] & symbols] # intersec each number positions with symbols positions
print(sum(total))