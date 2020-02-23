import math
n = 10001
count = 0
sum = 0

nn = n ** 2 # set boundary for prime list
primes = [True] * nn #set all numbers to true

primes[0] = False
primes[1] = False

for i in range(2, nn):
    if primes[i] == True: #is a prime number
        for j in range( i + i, len(primes), i): #set every multiple to false
            primes[j] = False

for id, p in enumerate(primes):
    if p:
        sum += id
        count += 1
        if count == n:
            print(id, sum)

#old solution
'''import math
limitn = 10001
limit = limitn ** 2
composites = set()
primes = []


for i in range(2, int(math.sqrt(limit))):
    if i not in composites: #if i is a composite number, go to next iteration
        primes.append(i) #append to prime

        for j in range(i * 2, limit, i): #for every multiple of this number
            composites.add(j) # add to composite list
print(primes)'''