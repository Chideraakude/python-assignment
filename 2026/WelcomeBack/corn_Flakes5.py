#Write a python program tocreate the multiplication table (from 1 to 10) of a given number.

number = int(input("Enter a Number"))

for num in range(1,15):
    result = number * num
    print(f"{number} * {num} = {result}")
