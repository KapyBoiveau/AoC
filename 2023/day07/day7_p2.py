from collections import Counter

def isWorse(ranked, toRank):
    h1 = list(Counter(jokerThis(ranked)).values())
    h2 = list(Counter(jokerThis(toRank)).values())
    h1.sort(reverse=True), h2.sort(reverse=True)
    return (h1 > h2) or (h1 == h2 and ranked > toRank)

def jokerThis(hand):
    if '0' in hand and hand != '00000':
        most = Counter(hand).most_common()
        maxLetter = most[0][0] if most[0][0] != '0' else most[1][0]
        return hand.replace('0', maxLetter)
    return hand

hands = dict()
for line in open('./2023/day07/input.txt', 'r').readlines():
    hand, bid = line.strip().split()
    hand = hand.replace('A', 'F').replace('K', 'E').replace('Q', 'D').replace('J', '0').replace('T', 'B')
    hands[hand] = int(bid)

ranks = []
for hand in hands:
    inserted = False
    for i, rankedHand in enumerate(ranks):
        if isWorse(rankedHand, hand):
            ranks.insert(i, hand)
            inserted = True
            break
    if not inserted:
        ranks.append(hand)

print(sum([(i+1)*hands[h] for i,h in enumerate(ranks)]))