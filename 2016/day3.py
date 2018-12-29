print 'Part I'
data = [(int(a),int(b),int(c)) for a,b,c in [i.split() for i in open('day3.txt','r').read().split('\n')]]
valid = lambda t : t[0]+t[1]>t[2] and t[0]+t[2]>t[1] and t[1]+t[2]>t[0]
print len(filter(valid, data))
print 'Part II'
count_valid = 0
for i in range(0,len(data) - 2,3):
    for j in range(3):
        count_valid += valid((data[i][j],data[i+1][j],data[i+2][j]))
print count_valid