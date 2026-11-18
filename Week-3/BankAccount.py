class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount")

    def display_balance(self):
        print("Current balance:", self.balance)


# Creating an object
account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)
account.display_balance()