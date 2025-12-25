

def find_Total_Of_Square_Of_Numbers(numbers):

    total = 0

    for num in numbers:
        total= total + (num * num)

    return  total

numbers = []

for num in range(7):
    data_Input = int(input("Enter a number: "))
    numbers.append(data_Input)

print("The total of the square of the list is: ", find_Total_Of_Square_Of_Numbers(numbers))

