class Savings:

    def __init__(self):

        self.balance = 0

    def deposit(self, amount):

        self.balance += amount

    def withdraw(self, amount):

        self.balance -= amount

    def __str__(self):

        return f"₦{self.balance:,.2f}"