import random


class BankAccount:
    def __init__(self, full_name, routing_number, balance = 0):
        self.full_name = full_name
        self.routing_number = routing_number
        self.balance = balance
        self.account_number = random.randrange(10000000, 99999999)

    def deposit(self):
        pass

account1 = BankAccount("Ca", 123)
print(account1.full_name)
print(account1.routing_number)
print(account1.balance)
print(account1.account_number)

account2 = BankAccount("Smith", 111, 3)
print(account2.full_name)
print(account2.routing_number)
print(account2.balance)
print(account2.account_number)