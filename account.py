class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance = self.balance - amount
            print('Insufficient funds')

    def deposit(self, amount):
        self.balance += amount

