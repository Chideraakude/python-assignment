

def odd_Word(vowel_Words):
    myWord = ""

    for index in range(len(vowel_Words)):
        if index % 2 == 0:
            myWord += vowel_Words[index]

    return myWord

vowel_Words = input("Enter a String: ")
myWord = odd_Word(vowel_Words)
print(myWord)



