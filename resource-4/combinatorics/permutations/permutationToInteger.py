def permutationToInteger(perm):
	permLen = len(perm)
	elts = range(permLen)
	num = 0
	for i in range(permLen):
		digit = elts.index(perm[i])
		num += digit * math.factorial(permLen - i - 1)
		del elts(digit)
	return num
