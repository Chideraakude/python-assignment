
def length_Calculator(sample_String):

    count = 0

    for char in sample_String:
        count +=1

    return count

sample_String = input("Enter a string: ")

length = length_Calculator(sample_String)

print(length)


