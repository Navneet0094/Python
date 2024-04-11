cp=int(input("enter cost price: "))
sp= int(input("enter selling price: "))
if cp>sp:
   print("there is loss that is :" , cp -sp)
elif cp < sp :
   print("there is profit  that is : ",sp-cp )
else:
   print("there is no profit  no loss")   

