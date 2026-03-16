
#Print the following pattern
#53421
#4321
#321
#21
#1



enter = int(input("Enter number: "))

for number in range(5,0,-1):
    for num in range(number,0, -1):
        print(num, end=" ")
    print()
