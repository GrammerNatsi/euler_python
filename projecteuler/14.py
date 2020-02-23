def find_chain(t): #literally just does what the spec says
    arr = []

    while t > 1:
        arr.append(int(t))

        if t % 2 == 0:
            t = t / 2
        else:
            t = (t * 3) + 1

    arr.append(1)
    return arr

limit = 1000000

max_len = 0
max_start = 0
for i in range(limit, int((limit / 1.8) - 1), -1): # range decreased to only largest numbers for efficiency
    ar = find_chain(i)
    if max_len < len(ar):
        max_len = len(ar)
        max_start = ar[0]

print(max_start)