# my_list = ["apple", "banana", "cherry"]

# print(my_list)

#--------------------------------
# students = list(('Mithun', 'Charan', 'Ranjan'))

# student_name = list('Mithun')

# print(students)  # Output: ['Mithun', 'Charan', 'Ranjan']
# print(student_name)  # Output: ['M', 'i', 't', 'h', 'u', 'n']

# #--------------------------------slicing
# students = ['Mithun', 'Charan', 'Ranjan']

# first_item = students[0]
# second_item = students[1]
# last_item = students[-1]

# print(first_item)  # Output: 'Mithun'
# print(second_item)  # Output: 'Charan'
# print(last_item)  # Output: 'Ranjan'

#--------------------------------

# a =[1,2,3,4]
# print(a)
# a.append(6)
# print(a)
# print(a.append(5))
# b = a.append(5)
# print(b)

#--------
# students = ['Mithun', 'Charan', 'Ranjan']

# students.insert(1, 'Trilok')

# print(students)  # Output: ['Mithun', 'Trilok', 'Charan', 'Ranjan']
#-------------removing itema and adding items in list
# a = [1,2]
# b=[3,4]
# a.extend(b)
# print(a)
# a.remove(4)
# print(a)
# a.remove(2)
# print(a)

# b=[5,6,7,8]
# b.pop()
# print(b)
# b.pop(0)
# print(b)
# print(b[1])
# b.reverse()
# print(b)
# b.sort()
# print(b)
# b.sort(reverse = True)
# print(b)


#------------------
a=[1,2,3]
print(a)
m = a
m[0]=0
print(a)
print(m)