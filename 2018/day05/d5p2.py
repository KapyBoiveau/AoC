
def react(poly):
    newPoly = ''
    i = 0
    while i < len(poly):
        x = poly[i]
        nope = False
        if i > 0:
            if (x.isupper() and poly[i-1].islower()) or (x.islower() and poly[i-1].isupper()):
                if x.lower() == poly[i-1].lower():
                    nope = True
                    i += 1
            if not nope:
                newPoly += poly[i-1] if i < len(poly)-1 else poly[i-1]+x
        i += 1
    return newPoly

mini = 12000
input = open('./2018/day05/input.txt', 'r').read()
for x in ''.join(set(input.lower())):
    poly = input.replace(x,'').replace(x.upper(),'')
    while True:
        newPoly = react(poly)
        if newPoly != poly:
            poly = newPoly
        else:
            if len(poly) < mini:
                mini = len(poly)
            break
print(mini)