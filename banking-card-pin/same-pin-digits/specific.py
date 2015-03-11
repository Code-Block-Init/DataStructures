# What is the probability of one specific person to have the same pin digits with the person next to him?
# Assume that the pin is four digits

# Generating a specific one

pins = ['{0:04}'.format(i) for i in range(0, 10000)]
 
counter1, counter2, counter3, counter4 = 0, 0, 0, 0
for p in pins:
    p = set(p)
    if len(p) == 1:
        counter1 += 1
    elif len(p) == 2:
        counter2 += 1
    elif len(p) == 3:
        counter3 += 1
    elif len(p) == 4:
        counter4 += 1
 
print(counter1, counter2, counter3, counter4)
