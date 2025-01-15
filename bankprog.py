# Python Banking Program

def show_balance():
    pass

def deposit():
    pass

def withdraw():
    pass

balance = 0
is_running = True

while is_running:
    print("Don-don Banking")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    service = input("Enter the service of your choice: ")

    if service == '1':
        show_balance()
    elif service == '2':
        deposit()
    elif service == '3':
        withdraw()
    elif service == '4':
        is_running = False
    else:
        print("Service is Invalid")