import numpy as np

def isSafe(report):
    gaps = np.diff(report)
    return all(1 <= gap <= 3 for gap in gaps) or all(-3 <= gap <= -1 for gap in gaps)

input = open('./2024/day02/input.txt', 'r').read().split('\n')

safes = 0
for line in input:
    report = list(map(int, line.split()))
    safes += any(isSafe(report[:x] + report[x+1:]) for x in range(len(report)))

print(safes)