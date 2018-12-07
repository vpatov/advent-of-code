with open('5.in') as f:
    polymer = list(f.read())

originalPolymer = list(polymer)


def reducedLength(polymer):
    i = 0
    while(i < len(polymer) - 1):
        if (polymer[i].islower() and polymer[i+1] == polymer[i].upper()) or \
           (polymer[i].isupper() and polymer[i+1] == polymer[i].lower()):
           # print(i)
           # print(polymer)
           del polymer[i]
           del polymer[i]
           # print(polymer)
           i -= 1
           if i < 0:
                i = 0
        else:
            i += 1

    return len(polymer)

print(reducedLength(list(polymer)))


lowestLength = float('inf')
for i in range(ord('a'),ord('z') + 1):
    ch = chr(i)
    chu = ch.upper()


    length = reducedLength([a for a in polymer if (a != ch and a != chu)])

    if length < lowestLength:
        lowestLength = length

print(lowestLength)



    
        