n = int(input('Enter number of prime no you wants: '))
prime = 0
num = 2
while prime<n :
    is_prime  = True
    i = 2
    while  (i<num):
        if (num%i==0):
            is_prime = False
            break
    if is_prime == True:
        print(num)
        prime +=1
    num+=1
        