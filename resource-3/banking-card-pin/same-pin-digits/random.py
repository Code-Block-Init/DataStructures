# What is the probability of one specific person to have the same pin digits with the person next to him?
# Assume that the pin is four digits

# Generating a random process

from random import randint
 
def rand_pin_digits():
    a = '{0:04}'.format(randint(0, 10000))
    a = set(a)
    return a
 
match = 0
for i in range(10**6):
    a = rand_pin_digits()
    b = rand_pin_digits()
 
    if a == b:
        match += 1
         
print(match)
