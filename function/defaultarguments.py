# def average(a=9,b=1):
#     print("the average is ",(a+b)/2)
# average(5,5)
# average(5)
# average(b=4)
# average(b=4,a=8 ) #if we write like this we have not to care of order => keyword argument

#-------------------------------------------------------------------------------------

# def name(fname,mname ='Navneet',lname='Sharma'):
#     print('hello',fname,mname , lname )
# name('bhai')
# name('bhai','dushyant')
# name('bhai','natansh','khurana')
# name(mname ='rohit',fname='bhai')
# name('bhai',lname='hemant')

#---------------------------------------------------------------------------

#required argments => order does not mater
# def average(a,b,c=1):
#     print("the average is ",(a+b+c)/2)
# #if we give average(b=1) it will give us error as a is not passed
# average(1,2)

#------------------------------------------------------------------------------
#variable length arguments

# def average(*numbers):  #=> * will give tuple
#     print(type(numbers))
#     sum=0
#     for i in numbers:sum =sum+i
#     print("the average is ",sum/len(numbers))
# average(1,2,3,4,5,6) # kitne bhi le skte ho

#------------------------------------------------------------------------------

#def name(** name):    #=>** ye dictionary dedega
#     print('hello',name['fname'] ,name['mname'],name['lname'])

# name(mname ='how are',lname='you',fname='navneet')

# -----------------------------------------------------------------------------
def average(*number):
    sum=0
    for i in number :
        sum = sum+i
    # return 7 # agar 2 return krr de to phle wala mana jata hai
    return sum/len(number) # agar isko return na kre to none dega 
    
c= average(5,6,7,1)  # ye c is function ki value store krr lega
print(c) 

