fs = frozenset([1, 2, 3])
fs1 = frozenset({1, 2, 3})

print(fs)
print(fs1)#same output frozenset({1, 2, 3})


#Frozensets are handy when you need to use a set as a key in a dictionary, store a set in another set, or ensure that a set's contents do not change accidentally.
my_dict = {}
my_set = frozenset([1, 2, 3])
my_dict[my_set] = "Value associated with the set"

print(my_dict)