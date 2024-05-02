x , y , z = int(input('Enter x: ')),int(input('Enter y: ')),int(input('Enter z: '))
if x > y:
    if x > z:
        print('x is largest')
    else:
        print('z is larget')
else: 
    if y>z:
        print('y is largest')
    else: 
        print('z is largest')