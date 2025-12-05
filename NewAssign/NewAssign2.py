speed = float(input("Enter speed and acceleration: "))
acceleration = float(input("Enter the acceleration: "))


length = speed **2  / 2 * acceleration

print("The minimum runway for the airplane is: ", round(length, 2))
