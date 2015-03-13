def generator(sett):
	if(len(sett) <= 1):
		yield sett
	else:
		for i in range(len(sett)):
			for perm in generator(sett[:i] + sett[i+1:]):
				yield[sett[i]] + perm
