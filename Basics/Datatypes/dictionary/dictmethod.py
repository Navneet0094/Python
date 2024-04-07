# student_details = {'name': 'Mithun', 'age': 21, 'city': 'Bengaluru'}

# print(student_details.keys())
# Output: dict_keys(['name', 'age', 'city'])
#------------------values()

# ent_details = {'name': 'Mithun', 'age': 21, 'city': 'Bengaluru'}

# print(student_details.values()) # Output: dict_values(['Mithun', 21, 'Bengaluru'])

#-------------------------

# student_details = {'name': 'Mithun', 'age': 21, 'city': 'Bengaluru'}

# print(student_details.items())
# # Output: dict_items([('name', 'Mithun'), ('age', 21), ('city', 'Bengaluru')])

#--------------------- adding items to a list


# student_details = {'name': 'Mithun', 'age': 21, 'city': 'Bengaluru'}

# student_details['country'] = 'India'

# print(student_details)
# # Output: {'name': 'Mithun', 'age': 21, 'city': 'Bengaluru', 'country': 'India'}


#------------------------------concatenation of dictionaries
# student_details = {'name': 'Mithun', 'age': 21, 'city': 'Bengaluru'}

# marks_details = {'English': 100, 'Maths': 99, 'Science': '98'}

# student_details.update(marks_details)

# print(student_details)
# # Output: {'name': 'Mithun', 'age': 21, 'city': 'Bengaluru', 'English': 100, 'Maths': 99, 'Science': '98'}


#--------------removing items from dict

# pop

# student_details = {'name': 'Mithun', 'age': 21, 'city': 'Bengaluru'}

# student_details.pop('city')

# print(student_details)
# # Output: {'name': 'Mithun', 'age': 21}
#--------

# popitem()

# student_details = {'name': 'Mithun', 'age': 21, 'city': 'Bengaluru'}

# student_details.popitem()

# print(student_details)
# # Output: {'name': 'Mithun', 'age': 21}

#--------------del 
# student_details = {'name': 'Mithun', 'age': 21, 'city': 'Bengaluru'}

# del student_details['age']

# print(student_details)
# # Output: {'name': 'Mithun', 'city': 'Bengaluru'}


#------------- clear()
student_details = {'name': 'Mithun', 'age': 21, 'city': 'Bengaluru'}

student_details.clear()

print(student_details)  # Output: {}
