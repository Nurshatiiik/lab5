class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance is ${self.balance}"
        else:
            return "Invalid deposit amount."
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdrew ${amount}. New balance is ${self.balance}"
            else:
                return "You're poor, you have no money"
        else:
            return "Invalid withdrawal amount."
    def get_balance(self):
        return f"Account balance for {self.owner}: ${self.balance}"

owner_name = input("What is you're name? ")
initial_balance = float(input("The initial balance: "))
my_account = Account(owner_name, initial_balance)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("What you wanna see? (1/2/3/4): ")

    if choice == "1":
        amount = float(input("The deposit amount: "))
        print(my_account.deposit(amount))
    elif choice == "2":
        amount = float(input("The withdrawal amount: "))
        print(my_account.withdraw(amount))
    elif choice == "3":
        print(my_account.get_balance())
    elif choice == "4":
        print("Exiting your account.")
        break