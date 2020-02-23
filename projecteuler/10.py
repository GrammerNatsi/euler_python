import math
n = 2000000
sum = 0

primes = [True] * n #set all numbers to true

primes[0] = False
primes[1] = False

for i in range(2, n):
    if primes[i] == True: #is a prime number
        for j in range( i + i, len(primes), i): #set every multiple to false
            primes[j] = False

for id, p in enumerate(primes):
    if p:
        sum += id

print(sum)