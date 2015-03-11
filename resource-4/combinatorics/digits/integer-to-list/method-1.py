def integerToList:
	digits = [];
	temp = num
	while temp > 0:
		digits.append(temp % base)
		temp = temp // base
		digits.extend((listlen - len(digits)) * [0])
		return digits
