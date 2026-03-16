#Write a program that calculate sum of multiples of 10 between 1  to 20_000


#number = 10
#count = 1
sum = 0

for number in range(1, 20001, 10):
#    if(number % 10 == 0):
    sum += number
    print(sum, end=" ")
