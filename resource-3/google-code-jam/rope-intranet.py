# This problem attends a solution using dynamic programming. 
# We sort according to the numbers on the first building. 
# Then, we start from the lowest window in this building. 
# We check how many ropes from lower windows go higher than the rope from the current window in respect to the other building. 
# And the answer is the sum of the number of ropes that go higher for every window. 

# http://code.google.com/codejam/contest/619102/dashboard#s=p0

from bisect import bisect
 
testcases = int(input())
for t in range(1, testcases + 1):
    n1 = int(input())
     
    wires = []
    for k in range(n1):
        w1 = input().split()
        w1 = (int(w1[0]), int(w1[1]))
        wires.append(w1)
     
    wires.sort(key=lambda wir: wir[0])
    other_building = []
    crossings = 0
    for a, b in wires:
        i = bisect(other_building, b)
        crossings += len(other_building) - i
        other_building.insert(i, b)
     
    print('Case #' + str(t) + ': ', end='')
    print(crossings)
