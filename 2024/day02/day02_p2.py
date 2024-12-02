
input = open('./2024/day02/input.txt', 'r').read().split('\n')
reports = [list(map(int, line.split())) for line in input]

safes = 0
for report in reports:
    inc, dec = 0, 0
    for i in range(len(report)-1):
        inc += report[i] < report[i+1]
        dec += report[i] > report[i+1]

    for x in range(len(report)):
        r = report[:x] + report[x+1:] # check without one element
        if dec > inc: # mainly decreasing
            if all(1 <= r[i]-r[i+1] <= 3 for i in range(len(r)-1)):
                safes += 1
                break
        else:
            if all(1 <= r[i+1]-r[i] <= 3 for i in range(len(r)-1)):
                safes += 1
                break

print(safes)