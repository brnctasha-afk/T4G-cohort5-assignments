class BankAccount:
    """
    A class that represents a custumer's bank account.
    """

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the account."""
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

            self.balance += amount
            print(f"GHS {amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        """Withdraws money from the account if funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient funds.")
            return

            self.balance -= amount
            print(f"GHS {amount:.2f} withdraw successfully.")

    def get_balance(self):
        """Returns the current account balance."""
        return self.balance

    def __str__(self):
        return f"Account[{self.account_holder}]  Balance: GHS {self.balance:.2f}"


#Demonstration

account1 = BankAccount("Bernice Tekpor", 1000)
account2 = BankAccount("Emmanuel Drah", 600)

# Transactions
account1.deposit(300)
account1.withdraw(250)
account2.deposit(150)

print("\nFinal Account Details")
print(account1)
print(account2)

print("\nAttempting an invalid withdrawal...")
account2.withdraw(1000)
