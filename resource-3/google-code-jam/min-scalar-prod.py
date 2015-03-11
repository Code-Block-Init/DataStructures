# The solution is based on the fact that the maximum area of a rectangle is when it is square and generalizing to R. 
# It can be proved by taking the derivative of f(x) = (x – a)(x – b). f'(x) = 0 x = (a + b)/2. 
# Therefore, if we have two numbers with a constant sum, their product is maximized when they are as close as possible. 
# Intuitively, if we select the number, say 8, 4 * 4 is bigger than 5 * 3 or 6 * 2 or 7 * 1 and so on…

# Simpler explanation: We want to maximize \vec{A}\vec{B} = -\frac{1}{2}\left((\vec{A} - \vec{B})^2 - \vec{A}^2 - \vec{B}^2\right). 
# We know that \vec{A}^2 and \vec{B}^2 (the measure of the vectors) are the same no matter how we rearrange the coordinates.

# http://code.google.com/codejam/contest/32016/dashboard#s=p0

testcases = int(input())
for t in range(1, testcases + 1):
    n1 = int(input())
    num1 = [int(n) for n in input().split()]
    num2 = [int(n) for n in input().split()]
    num1.sort()
    num2.sort(reverse=True)
    res = 0
    for i in range(n1):
        res += num1[i] * num2[i]
    print('Case #' + str(t) + ': ', end='')
    print(res)
