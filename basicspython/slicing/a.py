fruit ="mango"
len(fruit)
print(fruit[:5])
print(fruit[1:4])
print(fruit[:])
print(fruit[:-3])
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit)-3]) # not work as 4->2
print(fruit[-3:-1])  # 2->4

nm='harry'
print(nm[-4:-2 ])