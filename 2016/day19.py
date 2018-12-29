from math import log
elves = 3017957
test_cases = {1:1,2:1,3:3,4:1,5:3,6:5,7:7,8:1,9:3,10:5,11:7}


def ff(n):
	up = 2
	cur = 1
	i = 0
	while (i < n):
		while(cur < up and i < n):
			yield cur
			i += 1
			cur += 2
		cur = 1
		up *= 2

def f(n):
	return list(ff(n))[-1]

for x in test_cases:
	assert(test_cases[x] == f(x))

print("Part I")
print(f(elves))



# nums = [1,2,3,4,5,6]



print("Part II")
# Inefficient but simple way to do it.
def erase_presents(n):
	nums = list(range(1,n+1))
	start_len = len(nums)
	while (len(nums) != 1):
		# removed.append(nums[len(nums) // 2])
		nums.remove(nums[len(nums) // 2])
	
		nums = nums[1:] + nums[0:1]
		
		
	return nums[0]

test_cases = {1:1,2:1,3:3,4:1,5:2,6:3,7:5,8:7,9:9,10:1,11:2,12:3,13:4}
for x in test_cases:
	assert(test_cases[x] == erase_presents(x))



# exploit the pattern 
def ff2(n):
	x = 3
	y = 0
	exp = 1
	while (x != n):
		first = 3 ** exp
		second = 3 ** (exp + 1)
		exp += 1
		while (y < first and x != n):
			x += 1
			y += 1
			yield y
		while (y < second and x != n):
			x += 1
			y += 2
			yield y
		y = 0

def f2(n):
	return list(ff2(n))[-1]

print(f2(elves))
