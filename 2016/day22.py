"""
root@ebhq-gridcenter# df -h
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     85T   66T    19T   77%
"""

info = [line.split() for line in open('day22.txt','r').readlines() if line.startswith('/dev')]
nodes = {}
for node in info:
	filename = node[0].split('-')
	x,y = int(filename[-2][1:]),int(filename[-1][1:])
	nodes[(x,y)] = (int(node[1][:-1]),int(node[2][:-1]),int(node[3][:-1]))


## Node = (x,y): (Size, Used, Available)

def adjacent_nodes(coors):
	x,y = coors
	return list(
		filter(
			lambda coors: coors in nodes,
			[
				(x+1,y),
				(x,y+1),
				(x-1,y),
				(x,y-1)
			]
		)
	)


"""
To do this, you'd like to count the number of viable pairs of nodes. A viable pair is any two nodes (A,B), regardless of 
whether they are directly connected, such that:

Node A is not empty (its Used is not zero).
Nodes A and B are not the same node.
The data on node A (its Used) would fit on node B (its Avail).
"""
def viable(a,b):
	if a == b:
		return False
	if not nodes[a][1]:
		return False
	return nodes[a][1] <= nodes[b][2]


print("Part I")
count_viable = 0
for node_a in nodes:
	for node_b in nodes:
		count_viable += viable(node_a,node_b)
print(count_viable)










