def errorFunction(xx):
	#constants
	a1 =  0.254829592
	a2 = -0.284496736
	a3 =  1.421413741
	a4 = -1.453152027
	a5 =  1.061405429
	p  =  0.3275911
	#saving the xx sign 
	sign = 1
	if xx < 0:
		sign = -1
	xx = abs(xx)
	t = 1.0/(1.0 + p*xx)
	y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*math.exp(-xx*xx)
	return sign*y
