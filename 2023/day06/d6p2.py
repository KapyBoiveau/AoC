
x = []
for line in open('./2023/day06/input.txt', 'r').readlines():
    x.append(int(''.join(line.strip().split()[1:])))
time, dist = x

print(len([0 for i in range(time+1) if i * (time-i) > dist]))