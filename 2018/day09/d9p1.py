
rules = open('./2018/day09/input.txt', 'r').read().split()
nbPlayers, nbMarbles = int(rules[0]), int(rules[6])*100
scores = [0 for _ in range(nbPlayers)]
board, pos, player, i = [0], 0, 0, 1

while(i <= nbMarbles):
    if i%23 == 0:
        toRemove = (pos - 7) % len(board)
        scores[player] += i + board.pop(toRemove)
        pos = toRemove
    else:
        pos = (pos+2) % len(board)
        board.insert(pos, i)
    i += 1
    player = (player + 1) % nbPlayers

print(max(scores))