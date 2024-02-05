a= float(input("enter a "))
b= float(input("enter b "))
operator = input("enter operator")
match operator:
 case '+' :
    print("addn is : ",a+b)
 case '-' :
    print("sub is : ", a-b)
 case '*' :
    print("mul. is : ", a*b)
 case '/' :
    print("div. is : ",a/b)
 case '%' :
    print("remainder is : ", a% b)
 case '**' :
    print(" a to power b is : ", a**b)
 case '//' :
    print("floor division is : ", a//b)
 case _ :
    print("enter a valid operator")
 