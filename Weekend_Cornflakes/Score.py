passed = 0
failed = 0

for student in range(1,16):
    user = int(input("Enter your score: "))
    if user >= 45:
                passed += 1
    else:
                failed += 1

print("Good work my lad: ", passed)
print("You are the handicapped you must face: ", failed)
