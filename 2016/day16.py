prob_input = '01111010110010011'
disk_size = 272

# Call the data you have at this point "a".
# Make a copy of "a"; call this copy "b".
# Reverse the order of the characters in "b".
# In "b", replace all instances of 0 with 1 and all 1s with 0.
# The resulting data is "a", then a single 0, then "b".

def transform(a):
	b = a[::-1]
	b = b.replace('0','2')
	b = b.replace('1','0')
	b = b.replace('2','1')
	return a + '0' + b


test_cases_transform = {
	'1':'100',
	'0':'001',
	'11111':'11111000000',
	'111100001010':'1111000010100101011110000'
}

for test_case in test_cases_transform:
	assert(transform(test_case) == test_cases_transform[test_case])

def iter_checksum(x):
	out = []	
	for i in range(0,len(x),2):
		if x[i] == x[i+1]:
			out.append('1')
		else:
			out.append('0')
	return ''.join(out)

def calc_checksum(x):
	check_sum = iter_checksum(x)
	while (len(check_sum) % 2 == 0):
		check_sum = iter_checksum(check_sum)
	return check_sum


print("Part I")
while (len(prob_input) < disk_size):
	prob_input = transform(prob_input)
prob_input = prob_input[:disk_size]
checksum = calc_checksum(prob_input)
print(checksum)

prob_input = '01111010110010011'
disk_size = 35651584

print("Part II")
while (len(prob_input) < disk_size):
	prob_input = transform(prob_input)
prob_input = prob_input[:disk_size]
checksum = calc_checksum(prob_input)
print(checksum)
