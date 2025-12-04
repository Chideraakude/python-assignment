number1 = int(input("Enter a number"))
number2 = int(input("Enter another number"))
number3 = int(input("Enter another"))

sum = number1 + number2 + number3
ave = sum/3
prod = number1 * number2 * number3
largest = max(number1, number2, number3)
smallest = min(number1, number2, number3)

print("The Sum: ", sum , "The Average: ", ave , "The Product: ", prod , "The Largest: ", largest , "The Smallest", smallest)
