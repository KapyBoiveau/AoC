
boxes = dict()
for step in open('./2023/day15/input.txt', 'r').read().split(','):
    p = step.find('=') if '=' in step else -1
    label, op = step[0:p], step[p]
    
    i = 0
    for x in label:
        i = ((i + ord(x)) * 17) % 256
    
    if op == '=':
        num = int(step[p+1:])
        if i not in boxes:
            boxes[i] = dict()
        boxes[i][label] = num
    else:
        if i in boxes:
            boxes[i].pop(label, None)
    
total = 0
for n in boxes:
    for i,x in enumerate(boxes[n]):
        total += (n+1) * (i+1) * boxes[n][x]
print(total)