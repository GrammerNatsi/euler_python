import math
def get_nth_tri(a): # nth triangle number formula: T(n) = n(n+1)/2
    tn = (a*(a+1))//2 # added // so that it becomes integer (floor division)
    return tn

def get_divisors(n): # to get divisors of number, iterating 1, sqrt(n) + 1 and adding 1 count for each number that goes into n
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1): #loop through 1 to sqrt of n + 1 using a floor of sqrt so output does not get two consecutive product (3,4 and 4,3)
        if n % i == 0:
            count += 2 #add 1 count for both products 
        if i * i == n: #if square number remove as theyre same number
            count -= 1
    #print(str(n) + ' has ' + str(count) + ' divisors')
    return count


# Main
for i in range(1,1000000):
    a = get_nth_tri(i)
    b = get_divisors(a)
    if b >= 500:
        print(str(a) + ' is the ' + str(i) + ' triangle number and has ' + str(b) + ' divisors')
        break    
print('end')  #end of program, gives feedback in case number cannot be found in range