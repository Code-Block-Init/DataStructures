#zero
if n == 0:
	yield []
	return

#modify
for ig in partitions(n-1):
	yield [1] + ig
if ig and (len(ig) < 2 or ig[1] > ig[0]):
	yield [ig[0] + 1] + ig[1:]
