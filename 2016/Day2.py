instructions = open('day2.txt','r').read().split('\n')

numpad1 = ((1,2,3),(4,5,6),(7,8,9))
x,y, = 1,1
code1 = ''
def process_instruction1(instruction):
    global x,y,code1
    for ch in instruction:
        if ch == 'U':
            x = x-1 if x > 0 else 0
        elif ch == 'D':
            x = x+1 if x < 2 else 2
        elif ch == 'L':
            y = y-1 if y > 0 else 0
        else:
            y = y+1 if y < 2 else 2
    code1 += str(numpad1[x][y])

numpad2 = ((0,0,1,0,0),(0,2,3,4,0),(5,6,7,8,9),(0,'A','B','C',0),(0,0,'D',0,0))
x,y = 0,0
code2 = ''
def process_instruction2(instruction):
    global x,y,code2
    for ch in instruction:
        t1,t2 = x,y
        if ch == 'U':
            x = x-1 if x > 0 else 0
        elif ch == 'D':
            x = x+1 if x < 4 else 4
        elif ch == 'L':
            y = y-1 if y > 0 else 0
        else:
            y = y+1 if y < 4 else 4
        if (not numpad2[x][y]):
            x,y = t1,t2
    code2 += str(numpad2[x][y])


print 'Part I'
for inst in instructions:
    process_instruction1(inst)
print code1
print 'Part II'
for inst in instructions:
    process_instruction2(inst)
print code2
