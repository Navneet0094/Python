n = int(input('Enter n : '))
if n <=0 or n==1:
      print('n is neither prime nor compisite')  
elif n ==2:
      print('n is prime')  

for i  in range(2,n):
    if n%i ==0 :
      
      print('n is not prime')

      break
    else :
      print('n is prime ')
      break