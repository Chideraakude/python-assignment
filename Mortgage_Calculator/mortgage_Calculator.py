

principal_Amount = int(input("Enter your principlal Amount: "))
rate = float(input("Enter Your Rate Please: "))
duration = int(input("Please Enter the duration: "))

monthly_Payment = (principal_Amount * rate * (1 + rate) ** duration / ((1 + rate) ** duration - 1))

print("The Principal Amount Is: ", principal_Amount)
print("The Annual Interest Rate Is: ", rate)
print("Your Monthly Payment is : $", round(monthly_Payment, 2))
