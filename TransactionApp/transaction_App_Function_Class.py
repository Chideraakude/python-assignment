


def deposit(amount, account_Balance, transactions):
    account_Balance += amount
    transactions.append(f"Deposited: N{amount} | New Balance: N{account_Balance}")
    print(f"Deposited: N{amount} | New Balance: N{account_Balance}")
    return account_Balance


def withdrawal(amount, account_Balance, transactions):
    if amount <= account_Balance:
        account_Balance -= amount 
        transactions.append(f"Withdrew: N{amount} | New Balance: N{account_Balance}")
        print(f"Withdrew: N{amount} | New Balance: N{account_Balance}")

    else:
        transactions.append("Failed Withdrawal!!: Insufficient Funds")
        print("Failed Withdrawal!!: Insufficient Funds")
    return account_Balance







def transaction_History(transactions):
    

    if len(transactions) == 0:
        print("No transaction yet!!.")
    else:
        print("The Folowing Transactions Are:")
        for count in range(len(transactions)):
            print(f"{count + 1}. {transactions[count]}")



account_Balance = 0
transactions = []

print("Welcome to Transaction Log App")


while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Transaction History")
    print("4. Exit")

    myChoice = input("Enter your choice: ")

    if myChoice == "1":
        amount = int(input("Enter amount deposited: "))
        account_Balance = deposit(amount, account_Balance, transactions)


    elif myChoice == "2":
        amount = int(input("Enter the amount withdrawn"))
        account_Balance = withdrawal(amount, account_Balance, transactions)

    elif myChoice == "3":
        transaction_History(transactions)       

    elif myChoice == "4": 
        print(f"\nClosing Balance: ${account_Balance}")4
        print("Thank you for using Transaction Log App!!")
        break

    else:
        print("Invaid Choice. Please Try Again!.")
        





