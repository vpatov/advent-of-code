from collections import defaultdict, Counter
import heapq
import pprint


with open('6.in') as f:
    coors = [tuple(int(i) for i in line.split(',')) for line in f.readlines()]

maxwidth = max(coors)[0]
maxheight = max(coors,key=lambda x: x[1])[1]

grid    = [([0] * maxheight) for _ in range(maxwidth)]
grid2   = [([0] * maxheight) for _ in range(maxwidth)]


manhattan_distances = defaultdict(dict)

def get_distance(coor1,coor2):
    x1,y1 = coor1
    x2,y2 = coor2
    return abs(x2 - x1) + abs(y2 - y1)

for coor1 in coors:
    for coor2 in coors:
        manhattan_distances[coor1][coor2] = get_distance(coor1,coor2)



# for coor in coors:
#     pprint.pprint((coor, sum(manhattan_distances[coor].values())))


count_distances = 0


for x in range(0,len(grid)):
    for y in range(0,len(grid[x])):
        dists = [get_distance((x,y),coor) for coor in coors]



        res = heapq.nsmallest(2,dists)

        if sum(dists) < 10000:
            grid2[x][y] = "!"
            count_distances += 1

        if res[0] == res[1]:
            grid[x][y] = '.'
        else:
            grid[x][y] = dists.index(res[0])


cnt = Counter()

for row in grid:
    cnt.update(row)


edge_set = set()
for i in range(0,len(grid[0])):
    edge_set.add(grid[0][i])
    edge_set.add(grid[-1][i])
for i in range(0,len(grid)):
    edge_set.add(grid[i][0])
    edge_set.add(grid[i][-1])


print([el for el in cnt.most_common() if el[0] not in edge_set][0][1])

print(count_distances)