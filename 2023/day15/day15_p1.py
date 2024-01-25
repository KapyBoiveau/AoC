
total = 0
for step in open('./2023/day15/input.txt', 'r').read().split(','):
    val = 0
    for x in step:
        val = ((val + ord(x)) * 17) % 256
    total += val
print(total)