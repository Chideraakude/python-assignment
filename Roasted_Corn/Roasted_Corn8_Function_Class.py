#Write a python function that takes a list as parameter and returns a list with every elements of the list squared.
#Sample data: [2, 3, 4, 5, 7]
#Expected output: [4, 9, 16, 25, 49]


def find_Square_Of_Numbers(numbers):

    square_Of_Numbers = []

    for num in square:
        square_Of_Numbers.append(num * num)

    return square_Of_Numbers

square = []

for num in range(7):
    data_Input = int(input("Enter a number: "))
    square.append(data_Input)
print("The Square of the list are: ", find_Square_Of_Numbers(square))




