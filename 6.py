nn = 100 #natural numbers
ssq = 0 #sum of squares
sqs = 0 #square sum


for i in range(1, nn + 1):
    ssq += (i ** 2)
    sqs += i

sqs = sqs ** 2

print(sqs - ssq)