n = 600851475143      
primefactors = 0
i = 2

while n > 1:
    if n % i == 0:
        primefactors = i 
        n /= i
    i = i + 1

print(primefactors)

