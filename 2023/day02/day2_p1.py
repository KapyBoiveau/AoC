
nb = 0
game = {'red':12, 'green':13, 'blue':14}
for id,line in enumerate(open('./2023/day02/input.txt', 'r').readlines()):
    balls = line.strip().replace(',', '').replace(';', '').split(':')[1].split()
    nb += id+1
    for i,b in enumerate(balls):
        if i%2 == 0:
            if int(b) > game[balls[i+1]]:
                nb -= id+1
                break        
print(nb)