
def d1p2(input):
    freqSet = set()
    y = 0
    while True:
        for i in input:
            y += i
            if y in freqSet:
                return y
            else:
                freqSet.add(y)
            
input = [int(x) for x in open('./2018/day01/input.txt', 'r').readlines()]
print(d1p2(input))