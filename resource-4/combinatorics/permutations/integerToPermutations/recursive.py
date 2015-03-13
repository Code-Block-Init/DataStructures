def recursive(num, listt):
	if len(listt) <= 1:
		return listt
	num = num % math.factorial(len(listt))
	nextElement = listt[num // math.factorial(len(listt) - 1)]
	return[nextElement] + recursive(num, [x for x in listt if x!=nextElement])
