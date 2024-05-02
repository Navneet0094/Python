def display_info(name, *args, **kwargs):
    print("Name:", name)
    print("Additional Arguments (*args):", args)
    print("Keyword Arguments (**kwargs):", kwargs)
display_info("John", "Male", 30, country="USA", city="New York")
# display_info("Alice", country="Canada", city="Toronto", "Female", 25)
print("-----------------------------")
# ex 2 name args ,normal ,kwargs

def func(a,b,*args,**kwargs):
  print(a,b,args,kwargs)
func(5,6,7,8,9,10,name="Vishwa",age=99)
print('---------------')

#ex 3 
# def func1(**kwargs ,a,b):
#   print(kwargs,a,b)

# func1(name="Vishwa", age=99, 7,9) # we cannot use positional arg after kwargs

# args and normal
# ex 1

def f1(*args,a=5,b=6):
  print(args, a, b)
f1(1,2,3,4,5,6)
print('---------------')

 # ex 2
def f(*args,a,b):
  print(a,b,args)
  print(*args)
#f(5,6,7,8,9,10)
result = f(6,7,7,8,a=9,b=10)
print(result)



