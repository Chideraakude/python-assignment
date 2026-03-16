#Write a program to print the first 15 multiples of 3 in a straight line

number = 15
count = 1

for number in range(1, 16):
    if(number % 3 == 0):
        print("\n", number)
