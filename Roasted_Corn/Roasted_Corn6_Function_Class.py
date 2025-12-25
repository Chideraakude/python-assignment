

def find_Minimum_Number(numbers):

    minimum_Number = numbers[0]

    for num in numbers:
        if num < minimum_Number:
            minimum_Number = num

    return minimum_Number

numbers = []

for num in range(5):
    data_Input = int(input("Enter a number: "))
    numbers.append(data_Input)

print ("The minimum number is: ", find_Minimum_Number(numbers))





