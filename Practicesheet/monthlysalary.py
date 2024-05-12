#Calculate monthly salary for a given annual salary and tax rate

annual_salary = int(input("enter annual salary: "))
tax_rate = int(input("enter tax rate: "))
post_tax_annual_salary = annual_salary*(1-(tax_rate/100))
monthly_salary = post_tax_annual_salary/12
#print(190000/12)
print(monthly_salary)


