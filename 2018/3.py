# Part I

with open('3.in') as f:
    claims = f.readlines()



fabric_size = 1200

fabric = [[0] * fabric_size for i in range(fabric_size)]

for claim in claims:
    num,at,coors,dims = claim.split()
    x,y = (int(_) for  _ in coors[:-1].split(','))
    width,height = (int(_) for _ in dims.split('x'))


    for x_ in range(x,x+width):
        for y_ in range(y,y+height):
            fabric[x_][y_] += 1


count = 0
for row in fabric:
    for cell in row:
        if cell >= 2:
            count += 1

print(count)




# Part II

fabric = [[0] * fabric_size for i in range(fabric_size)]
undisputed_claims = set()

for claim in claims:
    num,at,coors,dims = claim.split()
    x,y = (int(_) for  _ in coors[:-1].split(','))
    width,height = (int(_) for _ in dims.split('x'))

    disputing_claim = False
    for x_ in range(x,x+width):
        for y_ in range(y,y+height):
            otherclaim = fabric[x_][y_]
            if otherclaim != 0:
                disputing_claim = True
                if otherclaim in undisputed_claims:
                    undisputed_claims.remove(otherclaim)
            fabric[x_][y_] = num

    if not disputing_claim:
        undisputed_claims.add(num)

print(undisputed_claims.pop())