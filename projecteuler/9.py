n = 1000

for a in range(1, int(n/3 + 1)):
    for b in range(a, int(n/2 + 1)):
        c = n - a - b #c is remainder so that a + b + c == 1000

        if a * a + b * b == c * c:
            print(a * b * c)