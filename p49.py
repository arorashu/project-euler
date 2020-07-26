# p49
# prime permutations
#
# steps:
# 1. generate prime numbers
# 2. sort the digits and update hash table with count
# 3. scan for the hash table for all counts
# 

import time

start = time.time()

# list of primes
prime = [-1]*10000

# sieve of erathones` to get list of primes 

for i in range (2, 10000):
    if prime[i] == -1:
        z = int(10000/i )
        prime[i] = i
#        print(i)
        for j in range(i, z):
            prime[i*j] = 0

# all numbers in prime[] that are not zero are primes

countMap = {}
related = {}

for i in range (1000, 10000):
    if prime[i] != 0:
        sortedList = sorted(list(str(i)))
        sortedStr = "".join(sortedList)
        if sortedStr not in countMap:
            countMap[sortedStr] = 0
        if sortedStr not in related:
            related[sortedStr] = []
        countMap[sortedStr] += 1
        related[sortedStr].append(i)
#        if countMap[sortedStr] == 3:
#            print(f'count is 3, sortedStr={sortedStr}')
        
res = []
for k,primes in related.items():
    for i in range(len(primes)):
        for j in range(i+1, len(primes)):
            check = int((primes[i]+primes[j])/2)
            if check in primes:
                res.append((check, primes[i], primes[j]))
                    

end = time.time()
#print(related)
print(res)
print(f'exec time: {end-start} sec')

