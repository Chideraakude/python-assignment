number1 = int(input('Enter First Integer: '))
number2 = int(input('Enter Second Integer: '))
number3 = int(input('Enter Third Integer: '))

largest = number1

if (number2 > largest):
    largest = number2
if (number3 > largest):
    largest = number3
print("The largest number is: ", largest)


