# n fibonacci series => 0 1 1 3 5 8 .........
n = int(input("Enter number you wants to get fibonacci series: "))
a ,b = 0,1

for i in range(1,n+1): # using for loop
    print(a , end=",")
    a , b = b, a+b

# count = 0
# while (count<n):# using while loop
#     print(a , end=",")
#     a , b = b, a+b
#     count +=1
   
