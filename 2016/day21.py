
password = list("abcdefgh")
password = list("abcde")

instructions = [line.strip() for line in open('day21test.txt','r').readlines()]

def op6(password,x,y):
	letter = password[x]
	del password[x]
	password.insert(y,letter)
	return password

def op5(password,x,y):
	return password[:x] + password[x:y+1][::-1] + password[y+1:]

def op4(password,x,y):
	x_index = password.index(x)
	rot_amount = x_index + 2 if x_index >= 4 else x_index + 1
	password = op3(password,1 + rot_amount,'right')
	return password

def op3(password,x,direction):
	if x > len(password):
		x = x % len(password)
	if direction == 'left':
		return password[x:] + password[:x]
	else:
		return password[-x:] + password[:-x]

def op2(password,x,y):
	for i in range(0,len(password)):
		if password[i] == x:
			password[i] = 0
	
	for i in range(0,len(password)):
		if password[i] == y:
			password[i] = x
		if password[i] == 0:
			password[i] = y

	return password

def op1(password,x,y):
	temp = password[x]
	password[x] = password[y]
	password[y] = temp
	return password

"""
swap position X with position Y 
	means that the letters at indexes X and Y (counting from 0) should be swapped.
swap letter X with letter Y 
	means that the letters X and Y should be swapped (regardless of where they appear in the string).
rotate left/right X steps 
	means that the whole string should be rotated; for example, one right rotation would turn abcd into dabc.
rotate based on position of letter X 
	means that the whole string should be rotated to the right based on the index of letter X (counting from 0) 
	as determined before this instruction does any rotations. 
	Once the index is determined, rotate the string to the right one time, plus 
	a number of times equal to that index, plus one additional time if the index was at least 4.
reverse positions X through Y 
	means that the span of letters at indexes X through Y (including the letters at X and Y) should be reversed in order.
move position X to position Y 
	means that the letter which is at index X should be removed from the string, then inserted such that it ends up at index Y.
"""


operations = {
	('swap','position')		: op1,
	('swap','letter')		: op2,
	('rotate','left')		: op3,
	('rotate','right')		: op3,
	('rotate','based')		: op4,
	('reverse','positions')	: op5,
	('move','position')		: op6
}


print("Part I")
for instruction in instructions:
	components = instruction.split()
	op = operations[components[0],components[1]]

	X,Y = None,None
	for component in components:
		if component.isnumeric():
			if X == None:
				X = int(component)
			else:
				Y = int(component)

	if op == op3:
		password = op3(password,X,components[1])
	if op == op4:
		X = instruction[-1]
	if op == op2:
		X = instruction[2]
		Y = instruction[-1]
		print(instruction)
		print(instruction[2],instruction[-1])
	else:

		password = op(password,X,Y)
	print(op,X,Y,instruction)
	print(''.join(password))

print(''.join(password))
