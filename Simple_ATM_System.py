# Simple ATM System - Basic Python

balance = 5000

while True:
    print("\n====== ATM MENU ======")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print("Amount deposited successfully")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Please collect your cash")
        else:
            print("Insufficient balance")

    elif choice == "4":
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")