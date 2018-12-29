import time
import sys
from collections import Counter
import operator
data = [line.strip() for line in open('day6.txt','r')]

part1 = ''
part2 =''
for i in range(0,len(data[0])):
    cnt = Counter()
    for j in range(0,len(data)):
        cnt[data[j][i]] += 1
    part1 += str(max(cnt.iteritems(), key=operator.itemgetter(1))[0])
    part2 += str(min(cnt.iteritems(), key=operator.itemgetter(1))[0])

print 'Part I'
print part1
print 'Part II'
print part2