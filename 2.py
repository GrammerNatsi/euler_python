fum = 2
a = 1
b = 2
temp = 0

while b < 4000000:
    temp = a + b
    a = b
    b = temp

    if b % 2 == 0:
        fum += temp
    
print("the sum is: " + str(fum))