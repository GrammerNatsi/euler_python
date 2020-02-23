import numpy #for matrices

f = open('<filename>', "r") #add file name
lines = f.readlines()
rows = []

f.close()

for ln in lines:
    rows.append(ln.split())
grid = numpy.array(rows)

matrices = []

#makes a sub matrices for every combination of adjacent numbers
for i in range(len(grid) - 3):
    for j in range(len(grid[0]) - 3):
        sub = []
        sub.append(grid[i][j:j + 4])
        sub.append(grid[i + 1][j:j + 4])
        sub.append(grid[i + 2][j:j + 4])
        sub.append(grid[i + 3][j:j + 4])
        matrices.append(sub) #appends matrix to list of possible


max = 0
for m in range(len(matrices)): #for every matrix
    for r in range(len(matrices[m])): #for every row
       
        t = 1
        if r == 0: #if top row
            for n in range(len(matrices[m][r])): #for each item in top row
                t *= int(matrices[m][0][n])
                t *= int(matrices[m][1][n])
                t *= int(matrices[m][2][n])
                t *= int(matrices[m][3][n])

                if t > max:
                    max = t
                t = 1
        
        for b in range(len(matrices[m][r])): #get every value in the row and multiply them
            t *= int(matrices[m][r][b])

        if t > max:
            max = t
        t = 1

    #in each matrix there are two matrix calc, so do each in matrix loop
    t *= int(matrices[m][0][0])
    t *= int(matrices[m][1][1])
    t *= int(matrices[m][2][2])
    t *= int(matrices[m][3][3])
    if t > max:
        max = t
    t = 1

    t *= int(matrices[m][0][3])
    t *= int(matrices[m][1][2])
    t *= int(matrices[m][2][1])
    t *= int(matrices[m][3][0])
    if t > max:
        max = t
    t = 1
    
print(max)