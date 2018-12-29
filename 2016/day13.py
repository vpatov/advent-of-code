"""
Find x*x + 3*x + 2*x*y + y + y*y.
Add the office designer's favorite number (your puzzle input).
Find the binary representation of that sum; count the number of bits that are 1.
If the number of bits that are 1 is even, it's an open space.
If the number of bits that are 1 is odd, it's a wall.
"""

import Queue

def is_open(x,y):
    return ("{0:b}".format((x*x + 3*x + 2*x*y + y + y*y) + 1358)).count('1') % 2 == 0

target = 31,39

def get_open_neighbors(x,y):
    return list(
        filter(
            lambda c: (c[0] >= 0 and c[1] >= 0) and is_open(c[0],c[1]),
            [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
        )
    )

## Part I
queue = Queue.Queue()
cur = 1,1
visited = set([(1,1)])
for neighbor in get_open_neighbors(1,1):
    if neighbor not in visited:
        queue.put((neighbor,1))

while (not queue.empty()):
    cell,length = queue.get()
    visited.add(cell)
    if cell == target:
        print("Part I")
        print(length)
        break
    else:
        for neighbor in get_open_neighbors(cell[0],cell[1]):
            if neighbor not in visited:
                queue.put((neighbor,length + 1))


## Part II
queue = Queue.Queue()
cur = 1,1
visited = set([(1,1)])
for neighbor in get_open_neighbors(1,1):
    if neighbor not in visited:
        queue.put((neighbor,1))

while (not queue.empty()):
    cell,length = queue.get()
    
    if length > 50:
        break
    
    else:
        visited.add(cell)
        for neighbor in get_open_neighbors(cell[0],cell[1]):
            if neighbor not in visited:
                queue.put((neighbor,length + 1))

print("Part II")
print(len(visited))
