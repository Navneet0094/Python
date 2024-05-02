n=int(input(""))
while n>0:
    n-=1
    x = input()
    if len(x)>10:
        print(x[0],len(x)-2,x[-1],sep="")
    else:
        print(x)    
