import itertools

# Part one
ints = [int(num.strip()) for num in open('1.in').readlines() if len(num) > 0]
print(sum(ints))

# Part two
freqs = set()
freq = 0
for num in itertools.cycle(ints):
    if freq in freqs:
        print(freq)
        break
    freqs.add(freq)
    freq += num

