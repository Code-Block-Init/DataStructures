# counting partitions
def partition1(n,k=-1):
	if (k == -1):
		return sum([partition1(n,i) for i in range(1,n+1)])
	if (n < k):
		return 0
	if((n==0) or (n==1)):
		return 1
	if((k==1) or (n==k)):
		return 1
	return sum([partition1(n-k,i) for i in range(1,min(k,n-k)+1)])
