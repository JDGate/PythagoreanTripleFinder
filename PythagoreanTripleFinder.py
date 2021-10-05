import math

max_a = 1000000
max_b = 10000

total = 0
for a in range(1, max_a):
    for b in range(a, max_b):
        c = math.sqrt(a**2 + b**2)
        #This next if statement checks whether the a and b values produce a pythagorean triple (if c is a whole number)
        if c % 1 == 0:
            print(a, b, c)
            total += 1
print(total)