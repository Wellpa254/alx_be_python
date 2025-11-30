# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance  # Encapsulated balance

    def deposit(self, amount):
        """Add money to the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Subtract money if enough balance, otherwise fail."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print current balance."""
        print(f"Current Balance: ${self.account_balance}")
