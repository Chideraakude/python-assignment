my_integers = int (input("Enter number of integers: "))

#print("Enter your number")

counter = 1
even = 0
odd = 0

while (counter <= my_integers):
    print("Enter your number")
    number = int(input())
    if (number % 2 == 0):
            even = number + even
    else:
        odd = number + odd 

    counter = counter + 1
print("The sum of even numbers and the sum of odd numbers are", even , "and" , odd , "respectively")
