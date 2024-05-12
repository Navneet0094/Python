<<<<<<< HEAD
def is_even(num):     # function creation 
    '''
    this funcn will tell that a number is even or odd
    input - valid int
    out - even/odd
    '''
    if type(num) == int:
        if (num & 1) == 1:
            return 'odd'
        else :
            return 'even'
    else: 
        return 'akal k andhe even odd int hotA HAI '
# #     if  num%2==0 :
# #         return 'even'
# #     else:
# #         return 'odd'
for i in range (1,11):  # function call
    x = is_even(i)
    print(x)

print(is_even('hello'))


=======
def is_even(num):
    '''
    this funcn will tell that a number is even or odd
    input - valid int
    out - even/odd
    '''
    if  num%2==0 :
        return 'even'
    else:
        return 'odd'
for i in range (1,11):
    x = is_even(i)
    print(x)
>>>>>>> c278aed (Python)
