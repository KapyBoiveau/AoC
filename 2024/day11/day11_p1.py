import numpy as np
import math

def blink(stone, n):
    if n == 25:
        return 1
    if stone == 0:
        return blink(1, n+1)
    nbDigits = len(str(stone))
    if nbDigits % 2 == 0:
        left = int(str(stone)[:nbDigits//2])
        right = int(str(stone)[nbDigits//2:])
        return blink(left, n+1) + blink(right, n+1)
    return blink(stone * 2024, n+1)
     
stones = np.array(open('./2024/day11/input.txt', 'r').read().split(), dtype=int)
print(sum(blink(stone, 0) for stone in stones))
