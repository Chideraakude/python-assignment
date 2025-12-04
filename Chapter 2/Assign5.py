
year1 = 10
year2 = 20
year3 = 30

principal = 1000
rate = 0.07

#a = p(n+r)n

a1 = principal * ((1 + rate) ** year1)
a2 = principal * ((1 + rate) ** year2)
a3 = principal * ((1 + rate) ** year3) 

print("The amount of the first year is: ", round(a1, 2))
print("The amount of the second year is: ", round(a2, 2))
print("The amount of the third year is: ", round(a3, 2))
