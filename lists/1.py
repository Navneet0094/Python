l=['Navneet',1,2,3,4]
print(l)
print(type(l))
for i in l:
    print(i)

print(l[-3]) #=> length of list -3 -> 5-3 =2

if 'Navneet' in l:
    print('yes')
else:
    print('no')
if 'eet' in 'Navneet':
    print('yes')
else:
    print('no')
#--------------------------
print(l)
print(l[:])
