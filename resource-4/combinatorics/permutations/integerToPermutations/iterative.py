def iterative(num, permLen):
	perm = []
	num = num % math.factorial(permLen)
	elts = range(permLen)
	for i in range(l, permLen):
		digit = (num // math.factorial(permLen - i))
		num = (num % math.factorial(permLen - i))
		perm += [elts[digit]]
		elts = elts[:digit] + elts[digit+1:]
	return perm + elts
