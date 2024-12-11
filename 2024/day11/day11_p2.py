import numpy as np
import math

def split_number(n, nbDigits):
    half = 10 ** (nbDigits // 2)  # Puissance de 10 pour séparer
    return n // half, n % half # left, right


def blink(key):
    stone, n = key
    global dico
    if n == 75:
        return 1
    if key not in dico:
        if stone == 0:
            dico[key] = blink((1, n+1))
        else:
            nbDigits = int(math.log10(stone)) + 1
            if nbDigits % 2 == 0:
                left, right = split_number(stone, nbDigits)
                dico[key] = blink((left, n+1)) + blink((right, n+1))
            else:
                dico[key] = blink((stone * 2024, n+1))
    return dico[key]
    
dico = {}   
stones = np.array(open('./2024/day11/input.txt', 'r').read().split(), dtype=int)
print(sum(blink((stone, 0)) for stone in stones))
