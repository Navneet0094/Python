#to check that a valid triangle or not

a,b,c = int(input("enter a : ")) , int(input("enter b : ")) , int(input("enter c : "))
if ( a+b > c and a+c > b and b+c>a):
    print("valid triangle")
else :
    print("invalid triangle")
