# Python program to illustrate the use
# of 'is' identity operator
#x = 5
#y = 5
# #print(x is y)
# print(id(x))
# print(id(y))
x = ["Geeks", "for", "Geeks"]
y = ["Geeks", "for", "Geeks"]
z = x

# Returns False because z is the same object as x
print(x is not z)

# Returns True because x is not the same object as y,
# even if they have the same content
print(x is not y)

# To demonstrate the difference between "is not" and "!=":
# This comparison returns False because x is equal to y
print(x != y)


# # Define two variables with the same value
# num1 = [1, 2, 3]
# num2 = num1  # Making num2 reference the same object as num1

# # Identity (is): Returns True if both operands are the same object.

# result_is_true = num1 is num2
# print("Identity (is) True Condition:", result_is_true)  # Output: True




# # Define two variables with different objects but the same values
# num1 = [1, 2, 3]
# num2 = [1, 2, 3]

# # Identity (is): Returns True if both operands are the same object.

# result_is_false = num1 is num2
# print("Identity (is) False Condition:", result_is_false)  # Output: False





# # Define two variables with different objects but the same values
# num1 = [1, 2, 3]
# num2 = [1, 2, 3]

# # Identity (is not): Returns True if both operands are not the same object.

# result_is_not_true = num1 is not num2
# print("Identity (is not) True Condition:", result_is_not_true)

# Output: True





# Define two variables with the same value
num1 = [1, 2, 3]
num2 = num1  # Making num2 reference the same object as num1

# Identity (is not): Returns True if both operands are not the same object.

result_is_not_false = num1 is not num2
print("Identity (is not) False Condition:", result_is_not_false)

# Output: False