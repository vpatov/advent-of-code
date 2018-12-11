import re
with open('10.in') as f:
    lines = f.readlines()
    pat = re.compile(r'position=<\s*(-?\d+),\s*(-?\d+)>\s*velocity=<\s*(-?\d+),\s*(-?\d+)>')
    positions, velocities = [],[]
    for line in lines:
        match = pat.match(line)
        positions.append((int(match.group(1)), int(match.group(2))))
        velocities.append((int(match.group(3)), int(match.group(4))))



def printpositions(positions):

    minx = min(positions,key=lambda x: x[0])[0]
    miny = min(positions,key=lambda y: y[1])[1]

    normalized = set([(x-minx,y-miny) for x,y in positions])
    
    maxx = max(normalized,key=lambda x: x[0])[0]
    maxy = max(normalized,key=lambda y: y[1])[1]

    for y in range(0,maxy+1):
        for x in range(0,maxx+1):
            if (x,y) in normalized:
                print("#",end='')
            else:
                print(" ",end='')
        print()

    print("="*(maxx+1))
    return True


def iterpositions(positions,velocities):
    newpositions = []
    for i in range(0,len(positions)):
        newpositions.append((positions[i][0]+velocities[i][0],positions[i][1]+velocities[i][1]))

    return newpositions

def get_density(positions):
    minx = min(positions,key=lambda x: x[0])[0]
    miny = min(positions,key=lambda y: y[1])[1]

    maxx = max(positions,key=lambda x: x[0])[0]
    maxy = max(positions,key=lambda y: y[1])[1]

    return len(positions) / ((maxx - minx) * (maxy - miny))




seconds = 0
max_density = 0
max_positions = None
max_seconds = 0
count_descent = 0
prev_density = 0
while (True):

    density = get_density(positions)

    if density < prev_density:
        count_descent += 1
    else:
        count_descent = 0

    if count_descent > 30:
        break

    if density > max_density:
        max_density = density
        max_positions = positions
        max_seconds = seconds


    prev_density = density
    positions = iterpositions(positions,velocities)
    seconds += 1


printpositions(max_positions)
print(max_seconds)

