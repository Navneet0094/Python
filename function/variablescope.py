# def g(y):
#     print(x)
#     print(x+1) #local
# x= 5 # global 
# g(x)
# print(x)
#------------
# def f(y):
#     x = 1
#     x+=1
#     print(x)
# x = 5
# f(x)
# print(x)
#----------
# def h(y):
#     x+=1
# x = 5
# h(x)
# print(x)

# ------
def h(y):
    global x
    x+=1
x = 5
h(x)
print(x)
