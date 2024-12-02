
input = open('./2024/day02/input.txt', 'r').read().split('\n')
reports = [list(map(int, line.split())) for line in input]

safes = 0
for report in reports:
    for x in range(len(report)):
        r = report[:x] + report[x+1:] # remove indice x
        if r[0] > r[1]: # decreasing
            if all(1 <= r[i]-r[i+1] <= 3 for i in range(len(r)-1)):
                safes += 1
                break
        else: # increasing
            if all(1 <= r[i+1]-r[i] <= 3 for i in range(len(r)-1)):
                safes += 1
                break

print(safes)