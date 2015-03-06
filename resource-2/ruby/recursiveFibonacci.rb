# Recursive way of computing fibonacci series
def recursiveFibonacci(n)
	if n == 0 or n == 1
		return n
	else
		return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)
	end
end
