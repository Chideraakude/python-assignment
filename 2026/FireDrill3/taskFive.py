oddIndex = []

def odd_Index_Element(array):
    for count in range (0, len(array), 2):
        oddIndex.append(array[count])
    return oddIndex


scores = []

for counter in range(10):
    score = int(input("Enter a number between 1 and 10: "))
    scores.append(score)
print("The Odd Indexes are: ", scores)

oddNumbers = odd_Index_Element(scores)

print("The Odd Index Are: ", oddNumbers)
