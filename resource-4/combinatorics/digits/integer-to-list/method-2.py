def integerToList(num, listlen=0, base=2):
	return [(num//base**i)%base for i in range(max(listlen,int(math.ceil(math.log(num,base)))))]
