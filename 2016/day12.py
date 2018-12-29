instructions = [line.strip() for line in open('day12.txt','r').readlines()]




# cpy x y copies x (either an integer or the value of a register) into register y.
# inc x increases the value of register x by one.
# dec x decreases the value of register x by one.
# jnz x y jumps to an instruction y away 
    # (positive means forward; negative means backward), but only if x is not zero.

def cpy(x,y):
    global registers
    if x in registers.keys():
        registers[y] = registers[x]
    else:
        registers[y] = int(x)
def inc(x,_):
    global registers
    registers[x] += 1
def dec(x,_):
    global registers
    registers[x] -= 1
def jnz(x,y):
    global pc
    if x in registers.keys():
        if (registers[x]):
            pc += int(y)
        else:
            pc += 1
    else:
        if int(x):
            pc += int(y)
        else:
            pc += 1


operations = {
    'cpy': cpy,
    'inc': inc,
    'dec': dec,
    'jnz': jnz
}

# jnz 1 5
def process_instruction(instruction):
    global registers, pc
    parts = instruction.split()
    opcode = parts[0]
    op1 = parts[1]
    op2 = None
    if (opcode == 'cpy' or opcode == 'jnz'):
        op2 = parts[2]
    operations[opcode](op1,op2)
    if opcode != 'jnz':
        pc += 1



print 'Part I'
registers = {'a':0,'b':0,'c':0,'d':0}
pc = 0
while (pc < len(instructions)):
    process_instruction(instructions[pc])
print registers['a']

print 'Part II'
registers = {'a':0,'b':0,'c':1,'d':0}
pc = 0
while (pc < len(instructions)):
    process_instruction(instructions[pc])
print registers['a']