# args ->non keyword arguments 
def multiply(*args):
    product = 1 
    for i in args: 
        product = product*i
    print(args)
    print(*args)

    return product
print(multiply(1,2,3,4,5,10))

#kwargs -> keyword arguements
def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key , '->' ,value)
    print(kwargs)
# print(display(india = 'delhi',pakistan ='islamabad'))
# above line gives none as output dispaly function do not result anything explicitly -> means funcn rreturn nhi kr ra kch v

display(india = 'delhi',pakistan ='islamabad')
