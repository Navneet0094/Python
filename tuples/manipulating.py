countries = ('spain','italy','india','england','geramany')
temp = list(countries)
temp.append('russia')
temp.pop(3)
temp[2]='finland'
countries=tuple(temp)
print(temp)

#---------------------------------

country1=('pakistan','afghanistan','bangladesh','shrilanka')
country2=('vietnam ','india','china')
southeastasia = country1+country2
print(southeastasia)