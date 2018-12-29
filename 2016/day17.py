from hashlib import md5
from queue import Queue

def hash(x):
	return md5(x.encode('ascii')).hexdigest()

# up, down, left, and right
def get_door_status(hash):
	return tuple([ord(i) > ord('a') for i in hash[:4]])

def valid(i,j):
	return i >= 0 and i < 4 and j >= 0 and j < 4

def get_options(door_status,i,j):
	options = []
	if door_status[0]:
		if valid(i-1,j):
			options.append(((i-1,j),'U'))
	if door_status[1]:
		if valid(i+1,j):
			options.append(((i+1,j),'D'))
	if door_status[2]:
		if valid(i,j-1):
			options.append(((i,j-1),'L'))
	if door_status[3]:
		if valid(i,j+1):
			options.append(((i,j+1),'R'))
	return options

puzzle = [
	['-','-','-','-'],
	['-','-','-','-'],
	['-','-','-','-'],
	['-','-','-','V']
]


def find_route(password):
	"""
	Breadth-first search
	"""
	x,y = (0,0)
	queue = Queue()
	code = password
	path = ''
	options = get_options(get_door_status(hash(code)),x,y)

	for option in options:
		queue.put((option,code,path))

	while(not queue.empty()):
		option,code,path = queue.get()
		coors,direction = option

		if coors == (3,3):
			return path+direction
			break
		options = get_options(get_door_status(hash(code+direction)),coors[0],coors[1])
		for opt in options:
			queue.put((opt,code+direction,path+direction))


def find_longest_route(password):
	"""
	Breadth-first search
	"""
	paths = []
	x,y = (0,0)
	queue = Queue()
	code = password
	path = ''
	options = get_options(get_door_status(hash(code)),x,y)

	for option in options:
		queue.put((option,code,path))

	while(not queue.empty()):
		option,code,path = queue.get()
		coors,direction = option

		if coors == (3,3):
			paths.append(path+direction)
		else:
			options = get_options(get_door_status(hash(code+direction)),coors[0],coors[1])
			for opt in options:
				queue.put((opt,code+direction,path+direction))


	return len(max(paths,key=len))


## Test cases from problem description
print("Part I")
assert(find_route("ihgpwlah") == "DDRRRD")
assert(find_route("kglvqrro") == "DDUDRLRRUDRD")
assert(find_route("ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR")
print(find_route("vwbaicqe"))

print("Part II")
assert(find_longest_route("ihgpwlah") == 370)
assert(find_longest_route("kglvqrro") == 492)
assert(find_longest_route("ulqzkmiv") == 830)
print(find_longest_route("vwbaicqe"))