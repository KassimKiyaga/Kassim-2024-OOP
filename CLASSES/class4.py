class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def get_balance(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"
