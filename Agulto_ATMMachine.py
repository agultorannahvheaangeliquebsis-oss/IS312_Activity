print(" ________________________________________ ")
print("|             ATM MACHINE                |")
print("|________________________________________|")


agulto_balance = 500
agulto_active = True

while agulto_active:

    print("\nMain Menu")
    print("1 - Check Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Exit")

    agulto_option = input("Enter an option (1-4): ")

    if agulto_option == "1":
        print(f"Your current balance is: ₱{agulto_balance}")

    elif agulto_option == "2":
        try:
            agulto_deposit = float(input("Amount to deposit: ₱"))
            if agulto_deposit > 0:
                agulto_balance += agulto_deposit
                print("Deposit successful!")
            else:
                print("Invalid amount. Please enter a positive value.")
        except:
            print("Invalid input. Numbers only.")

    elif agulto_option == "3":
        try:
            agulto_withdraw = float(input("Amount to withdraw: ₱"))
            if agulto_withdraw <= 0:
                print("Invalid amount.")
            elif agulto_withdraw < 20:
                print("Minimum withdrawal is ₱20.")
            elif agulto_withdraw > agulto_balance:
                print("Not enough balance.")
            else:
                agulto_balance -= agulto_withdraw
                print("Withdrawal successful!")
        except:
            print("Invalid input. Numbers only.")

    elif agulto_option == "4":
        print("Transaction ended. Thank you!")
        agulto_active = False

    else:
        print("Invalid selection. Try again.")