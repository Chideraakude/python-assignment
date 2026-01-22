evenIndex = []

def even_Index_Element(array):
    for count in range (1, len(array), 2):
        evenIndex.append(array[count])
    return evenIndex


scores = []

for counter in range(10):
    score = int(input("Enter a number between 1 and 10: "))
    scores.append(score)
print("The Even Indexes are: ", scores)

evenNumbers = even_Index_Element(scores)

print("The Even Index Are: ", evenNumbers)
print("The Sums Are: ", sum(evenNumbers))

