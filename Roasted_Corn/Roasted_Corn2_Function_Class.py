
def new_Word(text):
    if len(text) < 2:
        return ""

    first_Two_Words = text[:2]
    last_Two_Words = text[-2:]
 

    return first_Two_Words + last_Two_Words
#text = input("Enter a string: ")
print(new_Word("semicolon"))
print(new_Word("on"))
print(new_Word("o"))
#print(text)



