#Write a python program that accept scores of 15 students from a #teacher(user) and determine the number of students that pass or #fail. Pass mark is 45.
score = []
passed = 0
failed = 0

for scores in range (15):
    scores = int (input("Enter a Score: "))
    score.append(scores)
    if (scores >= 45):
        print("Pass")
        passed += 1
    elif(scores == 45):
        print("Pass")
    elif(scores < 45):
        print("Fail")
        failed += 1
    else:
        print("Fail")
print(score)
print("The Total Passed", passed)
print("The Total Failed", failed)
