#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. 
#If the string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected output : 'abcing'
#Sample String : 'string'
#Expected output : 'stringly'
#Sample string: ‘on’
#Expected output: ‘on

text = input("Enter a String: ")

if len(text) < 3:
    new_Word = text

elif text.endswith("ing"):
    new_Word = text + "ly"
else:
    new_Word = text + "ing"

print(new_Word)


