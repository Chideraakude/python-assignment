#write a program to read a number from the command prompt and print a right angle trangle"*"


enter = int(input("Enter number: "))

for number in range(enter):
    for num in range(0, number + 1):
        print("*", end=" ")
    print()
