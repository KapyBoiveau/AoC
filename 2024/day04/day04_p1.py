import numpy as np

lines = open('./2024/day04/input.txt', 'r').read().split('\n')
x = np.array([list(l) for l in lines])

nb = 0
goal = 'XMAS'
laog = goal[::-1]
for i in range(len(x)):
    nb += ''.join(x[i]).count(goal) # ligne
    nb += ''.join(x[i]).count(laog) # ligne inversée
    nb += ''.join(x[:,i]).count(goal) # colonne
    nb += ''.join(x[:,i]).count(laog) # colonne inversée

for i in range(-len(x)+1, len(x)):
    nb += ''.join(np.diag(x, i)).count(goal) # diagonale
    nb += ''.join(np.diag(x, i)).count(laog) # diagonale inversée
    nb += ''.join(np.diag(np.flipud(x), i)).count(goal) # autre diagonale
    nb += ''.join(np.diag(np.flipud(x), i)).count(laog) # autre diagonale inversée

print(nb)