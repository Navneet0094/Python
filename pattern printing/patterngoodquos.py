n = int(input("enter n: "))
for i in range (1 , n+1):
    #printing spaces
    print(" "*(n-i),end="")
# for printing digits
    for j in range(1, (2*i-1+1)):
        print(j,end="")
    print()
