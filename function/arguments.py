#default arg
def power(a = 1, b = 1):
    return a**b
print(power())
print(power(2))
print(power(2,3))

#positional arguements
# jis position par arg diye jate hai usi parameter par jate hai

print(power(3,2))
print(power(2,3))

#keyword arg

print(power(a=12, b =2))
print(power(b=12, a =2))
