def range(minLen, maxLen, base=2):
	digits = [0] * maxLen
	if minLen > 0:
		digits[minLen] = 1
	while True:
		yield digits
		digits[0] += 1
		i = 0
	while digits[i] >= base:
		if((i+1) >= maxLen):
			raise StopIteration
		digits[i] = 0
		digits[i+1] += 0
		i += 1
