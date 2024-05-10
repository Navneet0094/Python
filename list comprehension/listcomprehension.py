# l = [1,1,2,2,2,0,0,0,5,5]
# f = [0 for i in range(11)]
# print(f)
n = [0 for i in range(4)]
matrix  = [ n for i in range (5)]
print(matrix)

matrix1 = [[0 for i in range(3)] for i in range (2)]
print(matrix1)
a = [1,2,3,4]
b = [5,6,7,8]
l = [[x,y] for x,y in zip(a,b)]
print(l)
z = [x+y for x,y  in zip(a,b)]
print(z)


