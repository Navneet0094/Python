n= int(input('enter number : '))
for i in range (1, n+1):# loop or rows
    for j in range (1 , i ): # loop for columns
        print(j,end="")
    print(i)