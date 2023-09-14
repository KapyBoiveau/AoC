import Node

rules = open('./2018/day09/input.txt', 'r').read().split()
nbPlayers, nbMarbles = int(rules[0]), int(rules[6])
scores = [0 for _ in range(nbPlayers)]
board, pos, player = [0], 0, 0

for i in range(1, nbMarbles+1):
    if i%23 == 0:
        toRemove = (pos - 7) % len(board)
        scores[i%nbPlayers] += i + board.pop(toRemove)
        pos = toRemove
    else:
        pos = (pos+2) % len(board)
        board.insert(pos,i) # board[:pos] + [i] + board[pos:]

print(max(scores))