a = 999
b = 999
max = 0

while b > 0:

    while a > 0:
        
        if str(a * b) == ''.join(reversed(str(a * b))) and a * b > max:
            max = a * b
        a -= 1
    a = 999
    b -= 1

print(max)