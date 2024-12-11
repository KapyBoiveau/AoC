import numpy as np

def blink(stone, n):
    if n == 25:
        return 1
    if stone == 0:
        return blink(1, n+1)
    # check number of digits of stone using log 10
    nbDigits = int(np.log10([stone])[0]) + 1
    if nbDigits % 2 == 0:
        return blink(int(str(stone)[:nbDigits//2]), n+1) + blink(int(str(stone)[nbDigits//2:]), n+1)
    return blink(stone * 2024, n+1)
     
stones = np.array(open('./2024/day11/input.txt', 'r').read().split(), dtype=int)
print(sum(blink(stone, 0) for stone in stones))
