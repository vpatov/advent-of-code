ips = [[int(i) for i in line.strip().split('-')] for line in open('day20.txt','r').readlines()]

ips.sort()

# What is the first IP that is not blocked?
print("Part I")
prev = 0
for pair in ips:
	first,second = pair
	if first > prev + 1:
		print(prev + 1)
		break
	prev = second



# What is the total number of allowed IPs?
print("Part II")

def combine_ranges(start1,end1,start2,end2):
	if (start2 <= end1 + 1):
		if (end2 > end1):
			return (start1,end2)
		else:
			return (start1,end1)
	else:
		return False

def size_gap_ranges(start1,end1,start2,end2):
	return start2 - end1 - 1



combined_ranges = []
i = 1
cur = None
prev = ips[0][0],ips[0][1]
while(i < len(ips)):
	start1,end1 = prev
	start2,end2 = ips[i][0],ips[i][1]
	combined_range = combine_ranges(start1,end1,start2,end2)

	if combined_range:
		prev = combined_range
		cur = combined_range
	else:
		prev = start2,end2
		combined_ranges.append(cur)
		cur = start2,end2
	i += 1
if cur != combined_ranges[-1]:
	combined_ranges.append(cur)


num_allowed_ips = 0
i = 1
prev = combined_ranges[0]
while(i < len(combined_ranges)):
	cur = combined_ranges[i]
	num_allowed_ips += cur[0] - prev[1] - 1
	prev = cur
	i += 1



print(num_allowed_ips)


