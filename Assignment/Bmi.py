weight = float(input("Enter your weight: "))
height = float(input("Enter your height"))

bmi = weight / (height * height)

if (weight < 18.5):
    print("Underweight")

if (weight <= 24.9 ):
    print("Underweight")

if (weight <= 29.9):
    print("Overweight")

if (weight >= 30):
    print("Obese")
