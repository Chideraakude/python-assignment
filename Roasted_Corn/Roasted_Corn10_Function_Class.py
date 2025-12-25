
def string_And_Number(words, numbers):

   if type(numbers) == int:
        return words * numbers
   else:
        return words


words = input("Enter a string: ")
numbers = input("Enter a number: ")

if "." in numbers:
    numbers = float(numbers)
else:
    numbers = int(numbers)

print(string_And_Number(words, numbers))

