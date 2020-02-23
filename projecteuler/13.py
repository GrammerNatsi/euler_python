
sum = 0 #total of all numbers

try:
    f = open("D:\\NodeJs\\applications\\python\\projecteuler\\files\\13data.txt", "r") #add file 
except FileNotFoundError as err:
    print('file not found')
else:

    for x in f: #for each row x in file
        sum += int(x) #convert row which is one big string to one big int, then add it to sum
    f.close() #always close your files when you are finished with them
    
print(str(sum)[0:10]) #print substring of sum