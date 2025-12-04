x = float(input("Enter your Q1: "))
y = float(input("Enter your Q2: "))


if (x >  0 and y > 0):
    print("Q1")

if (x <  0 and y > 0):
    print("Q2")

if (x <  0 and y < 0):
    print("Q3")

if (x >  0 and y < 0):
    print("Q4")

if (x == 0 and y == 0):
    print("ORIGIN")

if (x != 0 and y == 0):
    print("X-axis")

if (x == 0 and y != 0):
    print("Y-axis")







