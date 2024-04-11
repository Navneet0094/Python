# not everyone knows this

pos_inf = float("inf")
neg_inf = float("-inf")
print(pos_inf)
print(neg_inf)
print(type(pos_inf))
#-------------
nan_value = float("nan")
print(nan_value)
#-------------
x = float("nan")
y = float("nan")
print(x == y)
#--------------
inf1 = float("inf")
inf2 = float("-inf")
nan_value = float("nan")
print(inf1 > inf2)  # True
print(inf1 < nan_value)  # False
print(inf2 < nan_value)  # False