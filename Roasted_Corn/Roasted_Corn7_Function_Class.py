
def find_Maximum_Number(numbers):

    maximum_Number = numbers[0]

    for num in numbers:
        if num > maximum_Number:
            maximum_Number = num

    return maximum_Number

numbers = []

for num in range(7):
    data_Input = int(input("Enter a number: "))
    numbers.append(data_Input)

print ("The maximum number is: ", find_Maximum_Number(numbers))
