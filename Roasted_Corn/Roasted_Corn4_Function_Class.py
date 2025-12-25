
def sample_Data_Of_Longest_Words(myWord):

    longest_Word =""
    max_Length = 0

    for word in myWord:
        if len (word) > max_Length:
            longest_Word = word
            max_Length = len (word)

    return(longest_Word, max_Length)

user_Input = int(input("Number of Words: "))

myWord = []

for count in range(user_Input):
    word = input("Enter a Word: ")
    myWord.append(word)

longest_Word, max_Length = sample_Data_Of_Longest_Words(myWord)

print("Longest Word is: ", longest_Word)
print("The Length is: ", max_Length)
