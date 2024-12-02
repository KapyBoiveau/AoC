
input = open('./2024/day02/input.txt', 'r').read().split('\n')
reports = [list(map(int, line.split())) for line in input]

safes = 0
for r in reports:
    if r[0] > r[1]: # decreasing, check if steps are between 1 and 3
        safes += all(1 <= r[i]-r[i+1] <= 3 for i in range(len(r)-1))
    else: # increasing
        safes += all(1 <= r[i+1]-r[i] <= 3 for i in range(len(r)-1))

print(safes)