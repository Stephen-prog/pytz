# Python Banking Program

def show_balance(balance):
    print("*********************")
    print(f"Your current balance is €{balance:.2f}")
    print("*********************")

def deposit():
    print("*********************")
    amount = float(input("Please enter an amount: "))
    print("*********************")
    if amount < 0:
        print("*********************")
        print("Invalid amount! Amount must be greater than 0!")
        print("*********************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("*********************")
    amount = float(input("Please enter withdrawal amount: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient funds!")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("Invalid amount! Amount must be greater than 0!")
        print("*********************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*********************")
        print("   Don-don Banking   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")
        service = input("Enter the service of your choice: ")

        if service == '1':
            show_balance(balance)
        elif service == '2':
            balance += deposit()
        elif service == '3':
            balance -= withdraw(balance)
        elif service == '4':
            is_running = False
        else:
            print("*********************")
            print("Service is Invalid")
            print("*********************")

    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")

if __name__ == '__main__':
    main()