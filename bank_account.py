import random


class BankAccount:
    def __init__(self, full_name, routing_number):
        self.full_name = full_name
        self.routing_number = routing_number
        self.balance = 0
        self.account_number = random.randrange(10000000, 99999999)

    def deposit(self, amount):
        # increase deposit by amount
        # print new balance

        self.balance += amount
        print(f"Amount deposited: ${amount:.2f} new balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        # subtract amount from balance
        # print new balance
        # if new balance is less than zero
            # print insufficient funds message
            # subtract overdraft fee
        
        self.balance -= amount
        print(f"Amount withdrawn: ${amount:.2f} new balance: ${self.balance:.2f}")

        if self.balance < 0:
            print("Insufficient funds.")
            self.balance -= 10

    def get_balance(self):
        print(f"Your current balance is ${self.balance:.2f}.")
        return self.balance

    def add_interest(self):
        # multiply to get interest for month
        # Add interest to balance
        # Print message to user about new balance and accumulated interest

        interest = self.balance * 0.00083
        self.balance += interest

        print(f"You accumulated ${interest:.2f} this month. Your new balance is ${self.balance:.2f}.")

    def print_receipt(self):
        pass

account1 = BankAccount("Ca", 123)
print(account1.balance)
account1.deposit(100)
account1.withdraw(40)
account1.add_interest()
print(account1.balance)
