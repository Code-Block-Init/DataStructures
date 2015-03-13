def partition2(n):
	sum1 = [1] * (n+1)
	for i in range(2, n+1):
		for j in range(i, n+1):
			sum1[j] += sum1[j-i]
	return sum1[n]
