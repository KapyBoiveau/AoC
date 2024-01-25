import regex as re

total = 0
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in open('./2023/day01/input.txt', 'r').readlines():
    nb = re.findall(r'\d|'+'|'.join(digits), line, overlapped=True)
    nb = [x if x.isdigit() else str(digits.index(x)+1) for x in nb]
    total += int(nb[0]+nb[-1]) if len(nb) else 0
print(total)