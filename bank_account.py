import random


class BankAccount:
    def __init__(self, full_name, routing_number, account_type, account_number = random.randrange(10000000, 99999999)):
        self.full_name = full_name
        self.routing_number = routing_number
        self.balance = 0
        self.account_number = account_number
        self.account_type = account_type

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

        if self.account_type == "checking":
            interest = self.balance * 0.00083
        else:
            interest = self.balance * 0.01

        self.balance += interest

        print(f"Your {self.account_type}s account accumulated ${interest:.2f} this month. Your new balance is ${self.balance:.2f}.")

    def print_receipt(self):
        print(self.full_name)
        print(f"Account No.: ****{str(self.account_number)[-4:]}")
        print(f"Routing No.: {self.routing_number}")
        print(f"Balance: ${self.balance:.2f}")

account1 = BankAccount("Ca'Sandra Smith", 12356, "checking")
account1.deposit(100)
account1.withdraw(80)
account1.get_balance()

account2 = BankAccount("Mitchell", 39890, int("03141592"), "checking")
account2.deposit(400000)
account2.print_receipt()
account2.add_interest()
account2.print_receipt()
account2.withdraw(150)
account2.print_receipt()

account3 = BankAccount("James Marshall", 23074, "checking")
account3.deposit(20)
account3.withdraw(25)
account3.get_balance()

account4 = BankAccount("Randy Walsh", 11111, "checking")
account4.deposit(400)
account4.add_interest()
account4.get_balance()

account5 = BankAccount("Randy Walsh 2", 11111, "saving")
account5.deposit(400)
account5.add_interest()
account5.get_balance()