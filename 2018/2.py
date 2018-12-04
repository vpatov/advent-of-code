from collections import Counter

# Part I
codes = [line.strip() for line in open('2.in').readlines()]

exactly_two = 0
exactly_three = 0

for code in codes:
    counter = Counter(code)
    if 3 in counter.values():
        exactly_three += 1
    if 2 in counter.values():
        exactly_two += 1

print(exactly_two * exactly_three)


# Part II

for a in range(0,len(codes)):
    code1 = codes[a]
    for b in range(a,len(codes)):
        code2 = codes[b]
        count = 0
        index = None
        for i in range(0,len(code1)):
            if code1[i] != code2[i]:
                count += 1
                index = i

        if count == 1:
            print(code1[:index]+code1[index+1:])
            exit()
