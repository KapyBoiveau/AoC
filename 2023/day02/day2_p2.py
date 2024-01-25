
nb = 0
for id,line in enumerate(open('./2023/day02/input.txt', 'r').readlines()):
    maxi = {'red':0, 'green':0, 'blue':0}
    balls = line.strip().replace(',', '').replace(';', '').split(':')[1].split()
    
    for i,b in enumerate(balls):
        if i%2 == 0:
            if int(b) > maxi[balls[i+1]]:
                maxi[balls[i+1]] = int(b)
    nb += maxi['red'] * maxi['green'] * maxi['blue']
print(nb)