
# integer right triangles

import math

p = 10

# a^2 + b^2 = c^2
# a + b + c = p = 120
# how many solutions for a, b, and c ?

a = 1
b = 1
c = 1
count = 0
bestP = 1

# a^2 + b^2 = (p - (a+b))^2
# a^2 + b^2 = p^2 + a^2 + b^2 + 2ab + - 2ap - 2bp 
# 
for p in range(10, 1001, 2):
    res = set()
    for a in range(1, int(p/2)):
        for b in range(a, p):
            if (p*p - 2*p*(a+b) + 2*a*b) == 0:
                tempC = int(math.sqrt(a*a + b*b))
#               print(f'found a: {a}, b: {b}, c: {tempC}\n')
                y = [a, b, tempC]
                y.sort()
#               print (type(y))
                res.add(tuple(y))

            # print(f'tried with a: {a}, b: {b}\n')

#    print(f'p: {p}, count: {len(res)}')
    if len(res) > count:
        count = len(res)
        bestP = p

print(bestP)
print(f'bestCount: {count}, bestP: {bestP}')



