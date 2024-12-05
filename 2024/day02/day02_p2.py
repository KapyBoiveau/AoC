
input = open('./2024/day02/input.txt', 'r').read().split('\n')
reports = [list(map(int, line.split())) for line in input]

safes = 0
for report in reports:
    for x in range(len(report)):
        ok = True
        r = report[:x] + report[x+1:] # remove report[x]
        for i in range(len(r)-1):
            if r[0] > r[1]: # decrease
                diff = r[i]-r[i+1]
            else: # increase
                diff = r[i+1]-r[i]
            if not(1 >= diff >= 3):
                ok = False
                break
        if ok:
            safes += 1
            break

print(safes)