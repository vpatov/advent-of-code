import math
instructions = [i.strip() for i in open('day1.txt','r').read().split(',')]

x,y = 0,0
facing = 0
visited = set([(x,y)])
first_x,first_y = None,None
for inst in instructions:
    if len(inst) <= 1:
        continue

    x_was,y_was = x,y
    direction = inst[0]
    num = int(inst[1:])
    if direction == 'L':
        if facing:
            facing = (facing - 1)
        else:
            facing = 3
    else:
        facing = (facing + 1) % 4

    if (facing == 0):
        addend = num / abs(num)
        for i in range(0,num):
            if (x,y) in visited and not first_x:
                first_x,first_y = x,y
            visited.add((x,y))
            y += addend
    elif (facing == 1):
        addend = num / abs(num)
        for i in range(0,num):
            if (x,y) in visited and not first_x:
                first_x,first_y = x,y
            visited.add((x,y))
            x += addend
    elif (facing == 2):
        addend = num / abs(num)
        for i in range(0,num):
            if (x,y) in visited and not first_x:
                first_x,first_y = x,y
            visited.add((x,y))
            y -= addend
    else:
        addend = num / abs(num)
        for i in range(0,num):
            if (x,y) in visited and not first_x:
                first_x,first_y = x,y
            visited.add((x,y))
            x -= addend

print 'Part I'
print abs(x) + abs(y)
print 'Part II'
print abs(first_x) + abs(first_y)