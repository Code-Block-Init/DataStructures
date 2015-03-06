# Non-recursive style of computing the fibonacci series
def NonRecFibo(n)
	prev = -1
	result = 1
	i = 0
	while i <= n
		sum = result + prev
		prev = result
		result = sum
		i += 1
	end
	return result
end
