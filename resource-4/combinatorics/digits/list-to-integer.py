def listToInt(listt,base=2):
	return reduce(lambda x,y:base*x+y,reversed(listt), 0)
