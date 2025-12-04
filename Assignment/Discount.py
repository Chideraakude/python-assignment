total_bill = int(input("Enter your bill: "))
is_member = input("Are you a member: ")

if total_bill >= 1000 and is_member == "Yes":
    print("10% off")

elif total_bill >= 1000 and is_member == "No":
    print("5% off")
else:
    print("No discount, print final amount and discount message")
