fum = 0
count = 1

while count < 1000:
    if count % 3 == 0:
       fum += count
    elif count % 5 == 0:
        fum += count

    count += 1

print("the sum is: " + str(fum))