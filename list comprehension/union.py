a = [1,2,3,4]
b = [1,5,3,6]
# set_a = set(a)
# set_b = set(b)
# union = set_a.union(set_b)# this becomes set so we have to convert it in list
# result = list(union)
# print(result)



newlist = a.copy()  # Create a copy of list a to preserve its original contents

# Extend list a with elements from list b if they are not already in list a
newlist.extend(i for i in b if i not in a)

print(newlist)