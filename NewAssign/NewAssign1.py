distance = float(input("Enter your distance: "))
fuel_efficiency = float(input("Enter the miles of the car: "))
price = float(input("Enter the price per gallon: "))

cost_of_driving = (distance / fuel_efficiency) * price

print("The cost of driving is $" + str(round(cost_of_driving, 1)))
