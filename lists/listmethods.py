a= [1,2,13,4,5]
#-----------------------------------------------
a.append(8)   #ye list me element add krr dega
print(a)

#----------------------------------------------
a.sort()
print(a)        #ye list ko ascending order me krr dega

#------------------------------------------------

a.sort(reverse = True)
print(a)

#------------------------------------------------

a.reverse()
print(a)
# print(a.reverse()) ya fir print(a.sort()) ye none print krege kunki ye reverse ya sort to kr dega par new list return nhi krega

#------------------------------------------------

print(a.index(13)) # isko print me dala kunki ye value return krr rha hai
# ye jo b no. dalege uska 1st occurence ka index dedega

#------------------------------------------------
print(a.count(1))
# ye jis bhi element ko daloge uska count dedega
#-------------------------------------------------
 #copy method

# m=a
# print(m)
# m[0]=9
# print(m)
# print(a)

#----------------------------------------------------

m=a.copy()
print(m)
m[0]=89
print(m,a)  # ye list li  copy bana dega

#-----------------------------------------------------

a.insert(1,56)
print(a)  # ye 1st index par 56 ko rkh dega or bakio ko slide krr dega
#-----------------------------------------------------

p=[900,800,1000]
a.extend(p)
# p.extend(a)
print(p)
print(a)
# iska mtlb hai ki p ko kholo or a me daldo
#-------------------------------------------------------

c=[900,800,1000]
e=[34,54,35,46,5]
d= e+c  # ye concatenare kr dega
print(d)





