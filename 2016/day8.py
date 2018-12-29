instructions = [line.strip() for line in open('day8.txt','r').readlines()]
screen = [[0 for i in range(0,50)] for j in range(6)]

"""
rect 1x1
rotate row y=0 by 10
"""
def shift_column(colnum,amount):
    global screen
    column = [screen[i][colnum] for i in range(len(screen))]
    column = column[len(column)  - amount:] + column[:len(column)  - amount]
    for i in range(len(screen)):
        screen[i][colnum] = column[i]

def shift_row(rownum,amount):
    global screen
    row = list(screen[rownum])
    row = row[len(row)  - amount:] + row[:len(row)  - amount]
    screen[rownum] = row


shift_column(2,1)




def process_instruction(instruction):
    global screen
    inst = instruction.split()
    if inst[0] == 'rect':
        coors = inst[1].split('x')
        x,y = int(coors[0]),int(coors[1])
        for i in range(x):
            for j in range(y):
                screen[j][i] = 1
    else:
        amount = int(inst[-1])
        coors = inst[2].split('=')
        x = int(coors[1]) if coors[0] == 'x' else None
        y = int(coors[1]) if coors[0] == 'y' else None
        if (x != None):
            shift_column(x,amount)
        elif(y != None):
            shift_row(y,amount)

for instruction in instructions:
    process_instruction(instruction)

print 'Part I'
print sum([sum(row) for row in screen])

print 'Part I'

for i in range(0,len(screen)):
    for j in range(0,len(screen[i])):
        if screen[i][j] == 0:
            screen[i][j] = '.'
        else:
            screen[i][j] = '#'


for row in screen:
    for i in range(0,25,5):
        print row[i:i+5],
    print('')

#RURUCEOEIL

print('\n')
for row in screen:
    for i in range(25,50,5):
        print row[i:i+5],
    print('')



# for i in range(0,50,5):
#     for row in screen:
#         print row[i:i+5]
#         break
    
#     print('')